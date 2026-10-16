"""Evaluate a trained motion-tracking policy: N rollouts of the full clip, pass/fail + tracking errors.

Milestone 1 asks: does the K1 play the whole gesture without falling, every time? Training charts
can't answer that (episodes there start mid-clip, get pushed, and are averaged over thousands of
robots), so this runs a clean, repeatable test:

- N robots (default 50) run in parallel, one rollout each, from frame 0 to the last frame.
- Each robot gets its own randomized physics (friction, PD gains, masses, encoder bias: the
  task's startup domain randomization) and a slightly jittered start pose, so the N rollouts
  differ the way N tries on slightly different real robots would. Pushes and observation noise
  are off unless --push is given.
- A rollout fails if the task's own termination checks fire before the clip ends: trunk height
  or tilt, or a hand/foot height, more than the training thresholds away from the reference.
- Failures count from the first step, but tracking errors skip the first --settle-s seconds:
  the jittered start pose makes the hands jump ~15 cm while the robot catches up, which says
  nothing about how well it plays the gesture.

Usage:
    uv run eval-tracking --wandb-run-path bmcox2-university-of-illinois-urbana-champaign/mjlab/<run-id>
    uv run eval-tracking --wandb-run-path ... --push            # stress test with training pushes
    uv run eval-tracking --checkpoint-file logs/.../model_3000.pt --registry-name <artifact>:v3

Results print as a table and are saved to logs/eval/<run>_<motion>[_push].json.
"""

from __future__ import annotations

import json
import math
import time
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np
import torch
import tyro

import booster_mjlab.tasks  # noqa: F401, ensure task registry is populated.
from mjlab.envs import ManagerBasedRlEnv
from mjlab.rl import MjlabOnPolicyRunner, RslRlVecEnvWrapper
from mjlab.tasks.registry import load_env_cfg, load_rl_cfg, load_runner_cls
from mjlab.tasks.tracking.mdp import MotionCommandCfg
from mjlab.utils.os import get_wandb_checkpoint_path

HANDS = ("left_hand_end_ball", "right_hand_end_ball")
FEET = ("left_foot_link", "right_foot_link")
# A foot counts as "on the floor" (for the tilt check) within this height of its lowest reference height.
STANCE_HEIGHT = 0.03


@dataclass(frozen=True)
class Config:
    task: str = "Mjlab-Tracking-Flat-Booster-K1"
    wandb_run_path: str | None = None
    """entity/project/run_id. Gives the checkpoint and, unless overridden, the motion it trained on."""
    checkpoint_name: str | None = None
    """Checkpoint within the W&B run, e.g. model_3000.pt (default: latest)."""
    checkpoint_file: str | None = None
    """Local checkpoint instead of a W&B run (then also pass --motion-file or --registry-name)."""
    motion_file: str | None = None
    registry_name: str | None = None
    """Motion artifact to evaluate on, e.g. <entity>/motion_upload/wave_000508-tracking:v3."""
    num_rollouts: int = 50
    push: bool = False
    """Keep the training-time random pushes (robustness stress test)."""
    settle_s: float = 0.5
    """Seconds at the start excluded from tracking errors (failures still count)."""
    seed: int = 0
    device: str = "cuda:0" if torch.cuda.is_available() else "cpu"
    out_dir: Path = Path("logs/eval")


def wilson_lower(successes: int, n: int, z: float = 1.96) -> float:
    """95% lower confidence bound on the true success rate (Wilson score interval)."""
    if n == 0:
        return 0.0
    p = successes / n
    centre = p + z * z / (2 * n)
    spread = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (centre - spread) / (1 + z * z / n)


def resolve_motion(cfg: Config) -> tuple[str, str]:
    """Return (local motion.npz path, label)."""
    if cfg.motion_file:
        return cfg.motion_file, Path(cfg.motion_file).parent.name or Path(cfg.motion_file).stem
    import wandb

    api = wandb.Api()
    if cfg.registry_name:
        name = cfg.registry_name if ":" in cfg.registry_name else cfg.registry_name + ":latest"
        art = api.artifact(name)
    elif cfg.wandb_run_path:
        art = next((a for a in api.run(cfg.wandb_run_path).used_artifacts() if a.type == "motions"), None)
        if art is None:
            raise SystemExit("No motion artifact found in the run; pass --registry-name or --motion-file.")
    else:
        raise SystemExit("Pass --wandb-run-path, or --checkpoint-file with --motion-file/--registry-name.")
    return str(Path(art.download()) / "motion.npz"), art.name


def resolve_checkpoint(cfg: Config, experiment_name: str) -> tuple[Path, str]:
    """Return (checkpoint path, label)."""
    if cfg.checkpoint_file:
        path = Path(cfg.checkpoint_file)
        if not path.exists():
            raise SystemExit(f"Checkpoint not found: {path}")
        return path, f"{path.parent.name}_{path.stem}"
    if not cfg.wandb_run_path:
        raise SystemExit("Pass --wandb-run-path or --checkpoint-file.")
    log_root = (Path("logs/rsl_rl") / experiment_name).resolve()
    path, _ = get_wandb_checkpoint_path(log_root, Path(cfg.wandb_run_path), cfg.checkpoint_name)
    return path, f"{cfg.wandb_run_path.split('/')[-1]}_{path.stem}"


def foot_tilt_deg(quat_wxyz: torch.Tensor) -> torch.Tensor:
    """Angle between the foot's up axis and world up (feet are level in the zero pose)."""
    x, y = quat_wxyz[..., 1], quat_wxyz[..., 2]
    up_z = 1.0 - 2.0 * (x * x + y * y)  # z component of the rotated z axis
    return torch.rad2deg(torch.arccos(up_z.clamp(-1.0, 1.0)))


def main() -> None:
    cfg = tyro.cli(Config)
    torch.manual_seed(cfg.seed)
    np.random.seed(cfg.seed)

    env_cfg = load_env_cfg(cfg.task, play=True)  # play: start at frame 0, no pushes, no obs noise
    agent_cfg = load_rl_cfg(cfg.task)
    motion_cmd = env_cfg.commands["motion"]
    assert isinstance(motion_cmd, MotionCommandCfg), "eval-tracking only works on tracking tasks"
    if cfg.push:
        env_cfg.events["push_robot"] = load_env_cfg(cfg.task).events["push_robot"]
    env_cfg.scene.num_envs = cfg.num_rollouts
    env_cfg.seed = cfg.seed

    motion_cmd.motion_file, motion_label = resolve_motion(cfg)
    ckpt_path, ckpt_label = resolve_checkpoint(cfg, agent_cfg.experiment_name)
    print(f"[eval] checkpoint {ckpt_path}\n[eval] motion     {motion_label}")

    env = RslRlVecEnvWrapper(
        ManagerBasedRlEnv(cfg=env_cfg, device=cfg.device), clip_actions=agent_cfg.clip_actions
    )
    runner = (load_runner_cls(cfg.task) or MjlabOnPolicyRunner)(env, asdict(agent_cfg), device=cfg.device)
    runner.load(str(ckpt_path), load_cfg={"actor": True}, strict=True, map_location=cfg.device)
    policy = runner.get_inference_policy(device=cfg.device)

    base = env.unwrapped
    cmd = base.command_manager.get_term("motion")
    terms = base.termination_manager
    fail_terms = [t for t in terms.active_terms if not terms.get_term_cfg(t).time_out]
    joint_names = list(cmd.robot.joint_names)
    groups = {
        "arms": [i for i, n in enumerate(joint_names) if "Shoulder" in n or "Elbow" in n],
        "head": [i for i, n in enumerate(joint_names) if "Head" in n],
        "legs": [i for i, n in enumerate(joint_names) if "Hip" in n or "Knee" in n or "Ankle" in n],
    }
    hand_ids = [cmd.cfg.body_names.index(n) for n in HANDS]
    foot_ids = [cmd.cfg.body_names.index(n) for n in FEET]
    stance_z = cmd.motion.body_pos_w[:, foot_ids, 2].min(dim=0).values + STANCE_HEIGHT  # (2,)

    n = cfg.num_rollouts
    dt = base.step_dt
    settle_steps = round(cfg.settle_s / dt)
    dev = base.device
    alive = torch.ones(n, dtype=torch.bool, device=dev)
    fail_step = torch.full((n,), -1, dtype=torch.long, device=dev)
    fail_reason = [""] * n
    sums = {k: torch.zeros(n, device=dev) for k in ("body_cm", "hand_cm", "arms", "head", "legs", "height_cm")}
    max_hand_cm = torch.zeros(n, device=dev)
    max_tilt = torch.zeros(n, 2, device=dev)
    steps_alive = torch.zeros(n, device=dev)

    obs, _ = env.reset()
    # Stop on the clip's last frame: one more step and the motion wraps and teleports the robot to frame 0.
    num_steps = int(cmd.motion.time_step_total) - 1 - int(cmd.time_steps.max())
    t0 = time.time()
    with torch.inference_mode():
        for step in range(num_steps):
            obs, _, dones, _ = env.step(policy(obs))
            done = dones.bool() & alive
            if done.any():
                # The env auto-resets finished robots; record why, then stop counting them.
                for i in torch.nonzero(done).flatten().tolist():
                    fail_step[i] = step + 1
                    fail_reason[i] = ",".join(t for t in fail_terms if bool(terms.get_term(t)[i])) or "unknown"
                alive &= ~done
            if not alive.any():
                break
            if step < settle_steps:
                continue
            a = alive.float()
            # Body / hand errors use the reference re-anchored to the robot's current xy and heading
            # (same as training's error_body_pos), so slow drift across the floor doesn't count here.
            body_err = torch.linalg.norm(cmd.body_pos_relative_w - cmd.robot_body_pos_w, dim=-1)  # (n, bodies)
            hand_err = body_err[:, hand_ids].max(dim=-1).values
            sums["body_cm"] += a * body_err.mean(dim=-1) * 100
            sums["hand_cm"] += a * hand_err * 100
            max_hand_cm = torch.maximum(max_hand_cm, a * hand_err * 100)
            jerr = torch.rad2deg((cmd.joint_pos - cmd.robot_joint_pos).abs())
            for g, idx in groups.items():
                sums[g] += a * jerr[:, idx].mean(dim=-1)
            sums["height_cm"] += a * (cmd.robot_anchor_pos_w[:, 2] - cmd.anchor_pos_w[:, 2]) * 100
            on_floor = cmd.robot_body_pos_w[:, foot_ids, 2] < stance_z
            tilt = foot_tilt_deg(cmd.robot_body_quat_w[:, foot_ids]) * on_floor
            max_tilt = torch.maximum(max_tilt, tilt * a[:, None])
            steps_alive += a
    elapsed = time.time() - t0

    # Per-rollout results (errors are averages over the steps that rollout was alive).
    denom = steps_alive.clamp(min=1)
    drift_cm = torch.linalg.norm(cmd.robot_anchor_pos_w[:, :2] - cmd.anchor_pos_w[:, :2], dim=-1) * 100
    rollouts = []
    for i in range(n):
        ok = bool(alive[i])
        rollouts.append({
            "success": ok,
            "fail_time_s": None if ok else round(float(fail_step[i]) * dt, 3),
            "fail_reason": None if ok else fail_reason[i],
            "body_err_cm": float(sums["body_cm"][i] / denom[i]),
            "hand_err_cm": float(sums["hand_cm"][i] / denom[i]),
            "hand_err_max_cm": float(max_hand_cm[i]),
            "arm_joint_err_deg": float(sums["arms"][i] / denom[i]),
            "head_joint_err_deg": float(sums["head"][i] / denom[i]),
            "leg_joint_err_deg": float(sums["legs"][i] / denom[i]),
            "height_err_cm": float(sums["height_cm"][i] / denom[i]),
            "final_drift_cm": float(drift_cm[i]) if ok else None,
            "max_foot_tilt_deg": [float(v) for v in max_tilt[i]],
        })

    k = sum(r["success"] for r in rollouts)
    ok_runs = [r for r in rollouts if r["success"]] or rollouts

    def stat(key, fn=np.mean):
        return float(fn([r[key] for r in ok_runs]))

    summary = {
        "successes": k,
        "rollouts": n,
        "success_rate": k / n,
        "success_rate_95_lower": wilson_lower(k, n),
        "passed": k == n,
        "clip_seconds": round(num_steps * dt, 2),
        "hand_err_cm_mean": stat("hand_err_cm"),
        "hand_err_cm_worst": stat("hand_err_max_cm", np.max),
        "body_err_cm_mean": stat("body_err_cm"),
        "arm_joint_err_deg_mean": stat("arm_joint_err_deg"),
        "head_joint_err_deg_mean": stat("head_joint_err_deg"),
        "leg_joint_err_deg_mean": stat("leg_joint_err_deg"),
        "height_err_cm_mean": stat("height_err_cm"),
        "final_drift_cm_mean": float(np.mean([r["final_drift_cm"] for r in rollouts if r["success"]] or [float("nan")])),
        "max_foot_tilt_deg": [float(max(r["max_foot_tilt_deg"][j] for r in ok_runs)) for j in range(2)],
    }

    # Report.
    print(f"\n=== {ckpt_label} on {motion_label}{' (with pushes)' if cfg.push else ''} ===")
    print(f"{n} rollouts x {summary['clip_seconds']} s clip, simulated in {elapsed:.1f} s"
          f" (errors skip the first {cfg.settle_s} s)\n")
    verdict = "PASS" if summary["passed"] else "FAIL"
    print(f"Full clip, no falls:   {k}/{n}  -> {verdict}")
    print(f"  95% confident the true success rate is at least {summary['success_rate_95_lower']:.1%}")
    if k < n:
        reasons: dict[str, int] = {}
        for r in rollouts:
            if not r["success"]:
                reasons[r["fail_reason"]] = reasons.get(r["fail_reason"], 0) + 1
        times = [r["fail_time_s"] for r in rollouts if not r["success"]]
        print(f"  failures by reason: {reasons}; at t = {min(times):.2f}-{max(times):.2f} s")
    which = "successful rollouts" if k else "all rollouts, none succeeded"
    print(f"\nTracking quality ({which}; lower is better):")
    print(f"  hand position error    mean {summary['hand_err_cm_mean']:5.1f} cm   worst moment {summary['hand_err_cm_worst']:5.1f} cm")
    print(f"  all-body position err  mean {summary['body_err_cm_mean']:5.1f} cm")
    print(f"  joint angle error      arms {summary['arm_joint_err_deg_mean']:4.1f} deg   head {summary['head_joint_err_deg_mean']:4.1f} deg   legs {summary['leg_joint_err_deg_mean']:4.1f} deg")
    print(f"  trunk height vs ref    {summary['height_err_cm_mean']:+5.1f} cm   (negative = robot lower)")
    print(f"  drift across floor     {summary['final_drift_cm_mean']:5.1f} cm at clip end")
    print(f"  max foot tilt on floor L {summary['max_foot_tilt_deg'][0]:4.1f} deg   R {summary['max_foot_tilt_deg'][1]:4.1f} deg")

    cfg.out_dir.mkdir(parents=True, exist_ok=True)
    motion_slug = motion_label.replace("/", "_").replace(":", "_")
    out = cfg.out_dir / f"{ckpt_label}_{motion_slug}{'_push' if cfg.push else ''}.json"
    report = {
        "config": {k2: str(v) for k2, v in asdict(cfg).items()},
        "checkpoint": str(ckpt_path),
        "motion": motion_label,
        "summary": summary,
        "rollouts": rollouts,
    }
    out.write_text(json.dumps(report, indent=2))
    print(f"\nsaved -> {out}")
    env.close()


if __name__ == "__main__":
    main()
