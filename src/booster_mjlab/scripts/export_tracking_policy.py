"""Export a trained tracking checkpoint as ``policy.onnx``: the policy alone, for a robot or sim2sim.

The ONNX that mjlab's tracking runner exports bundles the whole reference motion (and is skipped for
full BEAT2, which is over ONNX's 2 GB limit). This one holds only the policy network and its
observation normalizer: ``obs`` (1, N) -> ``actions`` (1, 22). The deploy code builds ``obs`` from
the robot's sensors plus the current reference frame, and sends joint targets
``default_joint_pos + action_scale * actions`` to PD controllers with ``joint_stiffness`` /
``joint_damping``, every ``control_dt`` seconds. All of these are in the file's metadata, along with
the observation terms in order and their sizes (``observation_names`` / ``observation_dims``).

New runs write the same file next to every checkpoint (``K1MotionTrackingRunner``); use this for
older checkpoints. No motion data is downloaded: the env is built on a tiny standing reference, which
only has to exist for the env to start (the policy's weights don't depend on it).

Usage:
    uv run export-tracking-policy --wandb-run-path <entity>/mjlab/<run-id> --checkpoint-name model_5999.pt
    uv run export-tracking-policy --checkpoint-file logs/rsl_rl/k1_tracking/<run>/model_5999.pt
    uv run --with onnxruntime export-tracking-policy ...   # also checks the ONNX against PyTorch
"""

from __future__ import annotations

import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path

import mujoco
import numpy as np
import torch
import tyro
from tensordict import TensorDict

import booster_mjlab.tasks  # noqa: F401, ensure task registry is populated.
from mjlab.envs import ManagerBasedRlEnv
from mjlab.rl import RslRlVecEnvWrapper
from mjlab.tasks.registry import load_env_cfg, load_rl_cfg, load_runner_cls
from mjlab.tasks.tracking.mdp import MotionCommandCfg

from booster_mjlab.robots.booster_k1.k1_constants import HOME_KEYFRAME, K1_XML
from booster_mjlab.scripts.eval_tracking import resolve_checkpoint
from booster_mjlab.tasks.tracking.runner import DEPLOY_POLICY_FILE, K1MotionTrackingRunner


@dataclass(frozen=True)
class Config:
    task: str = "Mjlab-Tracking-Flat-Booster-K1-No-State-Estimation"
    """The task the checkpoint was trained on (its observation layout must match)."""
    wandb_run_path: str | None = None
    """entity/project/run_id: download the checkpoint from this W&B run."""
    checkpoint_name: str | None = None
    """Checkpoint within the W&B run, e.g. model_5999.pt (default: latest)."""
    checkpoint_file: str | None = None
    """Local checkpoint instead of a W&B run."""
    out_dir: Path | None = None
    """Where to write policy.onnx (default: next to the checkpoint)."""


def standing_reference(path: Path, frames: int = 10, fps: float = 50.0) -> Path:
    """A few frames of the K1 standing in its home pose, in the combined-motion .npz layout."""
    model = mujoco.MjModel.from_xml_path(str(K1_XML))
    data = mujoco.MjData(model)
    data.qpos[:3] = HOME_KEYFRAME.pos
    data.qpos[3:7] = (1.0, 0.0, 0.0, 0.0)
    for j in range(1, model.njnt):  # joint 0 is the floating base
        data.qpos[model.jnt_qposadr[j]] = HOME_KEYFRAME.joint_pos.get(model.joint(j).name, 0.0)
    mujoco.mj_kinematics(model, data)
    nb, nj = model.nbody - 1, model.njnt - 1
    tile = lambda a: np.repeat(a[None].astype(np.float32), frames, axis=0)  # noqa: E731
    np.savez(
        path,
        fps=np.array([fps]),
        joint_pos=tile(data.qpos[7:]),
        joint_vel=np.zeros((frames, nj), np.float32),
        body_pos_w=tile(data.xpos[1:]),
        body_quat_w=tile(data.xquat[1:]),
        body_lin_vel_w=np.zeros((frames, nb, 3), np.float32),
        body_ang_vel_w=np.zeros((frames, nb, 3), np.float32),
    )
    return path


def check_against_torch(onnx_path: Path, policy, obs_dim: int) -> None:
    """Compare ONNX and PyTorch outputs on random observations (needs onnxruntime)."""
    try:
        import onnxruntime as ort
    except ImportError:
        print("[export] onnxruntime not installed: skipped the ONNX vs PyTorch check (uv run --with onnxruntime ...)")
        return
    sess = ort.InferenceSession(str(onnx_path))
    obs = torch.randn(32, obs_dim)
    with torch.no_grad():  # rsl_rl's policy reads observation groups by name
        ref = policy(TensorDict({"actor": obs}, batch_size=[32])).numpy()
    out = np.concatenate([sess.run(None, {sess.get_inputs()[0].name: o[None].numpy()})[0] for o in obs])
    err = float(np.abs(out - ref).max())
    print(f"[export] ONNX vs PyTorch on 32 random observations: max |diff| {err:.2e}")
    if err > 1e-4:
        raise SystemExit("[export] ONNX output differs from PyTorch")


def main() -> None:
    cfg = tyro.cli(Config)
    env_cfg = load_env_cfg(cfg.task, play=True)
    agent_cfg = load_rl_cfg(cfg.task)
    env_cfg.scene.num_envs = 1
    motion_cmd = env_cfg.commands["motion"]
    assert isinstance(motion_cmd, MotionCommandCfg)

    ckpt_path, _ = resolve_checkpoint(cfg, agent_cfg.experiment_name)
    run_path = cfg.wandb_run_path or "local"
    with tempfile.TemporaryDirectory() as tmp:
        motion_cmd.motion_file = str(standing_reference(Path(tmp) / "standing.npz"))
        env = RslRlVecEnvWrapper(ManagerBasedRlEnv(cfg=env_cfg, device="cpu"), clip_actions=agent_cfg.clip_actions)
        runner = (load_runner_cls(cfg.task) or K1MotionTrackingRunner)(env, asdict(agent_cfg), device="cpu")
        if not isinstance(runner, K1MotionTrackingRunner):
            raise SystemExit(f"{cfg.task} does not use K1MotionTrackingRunner")
        runner.load(str(ckpt_path), load_cfg={"actor": True}, strict=True, map_location="cpu")
        out = runner.export_deploy_policy(cfg.out_dir or ckpt_path.parent, run_path)
        obs_dim = int(sum(np.prod(d) for d in env.unwrapped.observation_manager.group_obs_term_dim["actor"]))
        check_against_torch(out, runner.get_inference_policy(device="cpu"), obs_dim)
        env.close()
    print(f"[export] {ckpt_path} -> {out} (obs {obs_dim} -> actions 22)")
    assert out.name == DEPLOY_POLICY_FILE


if __name__ == "__main__":
    main()
