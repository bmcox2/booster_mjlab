"""Sim2sim: run an exported tracking policy in plain MuJoCo, the way the robot will run it.

No mjlab managers: the robot is plain MuJoCo (the K1 with the training actuators, floor and solver
settings), and everything the policy sees is built by ``booster_mjlab.deploy`` from what a robot can
measure: joint encoders, IMU orientation and gyro. The robot starts standing in its home pose (like
the real one under Booster's controller), the reference leads in from that pose, plays the clip,
and holds the last frame. A policy that passes here is ready for the robot code, which swaps this
file's MuJoCo backend for the Booster SDK and keeps the rest.

Checks on the way: the actuator gains in the model match the ONNX metadata (what the robot will be
sent), and the policy's observations don't need state estimation.

Usage:
    uv run sim2sim --policy logs/rsl_rl/k1_tracking/<run>/policy.onnx --motion-file <combined.npz> --clip <name>
    uv run sim2sim --wandb-run-path <entity>/mjlab/<run-id> --motion-file ... --clip ...   # policy.onnx from W&B
    uv run sim2sim ... --obs-delay-steps 1 --push --runs 10    # stress: 20 ms sensor delay, pushes
    uv run sim2sim ... --video logs/videos/sim2sim.mp4
"""

from __future__ import annotations

import re
from collections import deque
from dataclasses import dataclass
from pathlib import Path

import mujoco
import numpy as np
import tyro

import booster_mjlab.tasks  # noqa: F401, ensure task registry is populated.
from booster_mjlab.deploy import Reference, RobotState, TrackingPolicy, build_observation
from booster_mjlab.deploy import observation as ob
from booster_mjlab.robots.booster_k1.k1_constants import HOME_KEYFRAME, K1_XML
from booster_mjlab.scripts.export_web_demo import (
    CCD_ITERATIONS,
    FLOOR_SOLIMP,
    FLOOR_SOLREF,
    LS_ITERATIONS,
    SIM_TIMESTEP,
    SOLVER_ITERATIONS,
)
from mjlab.tasks.registry import load_env_cfg

HANDS = ("left_hand_end_ball", "right_hand_end_ball")


@dataclass(frozen=True)
class Config:
    motion_file: Path
    """Motion .npz (combine-motions / upload-motion layout, 50 fps)."""
    clip: str | None = None
    """Clip name in a combined file (default: the first clip)."""
    policy: Path | None = None
    """policy.onnx (written next to each checkpoint, or by export-tracking-policy)."""
    wandb_run_path: str | None = None
    """Instead of --policy: download policy.onnx from this W&B run's files."""
    task: str = "Mjlab-Tracking-Flat-Booster-K1-No-State-Estimation"
    """Task whose robot (actuators) to simulate."""
    start: str = "stand"
    """stand: robot in its home pose, reference leads in (the demo). reference: robot placed exactly on
    frame 0 (like eval-tracking)."""
    settle_s: float = 0.0
    """stand: seconds holding the home pose with plain PD before the policy starts. These are the policy's
    gains, too soft to balance without it: the K1 tips ~22 deg in 1 s, so keep this near 0. The real robot
    is held upright at much stiffer prepare gains until the policy starts."""
    blend_s: float = 2.0
    """Lead-in: seconds blending the reference from the home pose to the clip's first frame."""
    hold_start_s: float = 1.0
    """Lead-in: seconds holding the clip's first frame before it plays."""
    hold_end_s: float = 2.0
    """Seconds holding the clip's last frame after it ends."""
    obs_delay_steps: int = 0
    """Sensor latency in control steps (20 ms each) between measuring and the policy seeing it."""
    push: bool = False
    """Random trunk pushes like training (every 1.5-4 s, up to 0.14 m/s)."""
    runs: int = 1
    """Repeat with different push timing (seeds 0..runs-1)."""
    privileged: bool = False
    """Sim only: give the policy the true motion_anchor_pos_b / base_lin_vel, so a state-estimation
    policy (the plain tracking task) can run. Checks this simulator against eval-tracking; never
    possible on the robot. Needs --start reference (the reference's world position must be the robot's)."""
    video: Path | None = None
    """Write an mp4 of run 0 (needs a working MuJoCo renderer, e.g. MUJOCO_GL=egl)."""


@dataclass
class Sim:
    model: mujoco.MjModel
    data: mujoco.MjData
    qadr: np.ndarray
    dadr: np.ndarray
    ctrl: np.ndarray
    trunk: int
    gyro: slice
    linvel: slice
    peak: np.ndarray
    speed: np.ndarray
    width: np.ndarray
    decimation: int


def build_sim(task: str, policy: TrackingPolicy) -> Sim:
    """The task's K1 (its actuators, gains, armature) + a floor, with the training solver settings."""
    robot_cfg = load_env_cfg(task).scene.entities["robot"]
    spec = robot_cfg.build().spec  # BoosterEntity: its actuators require it
    for texture in list(spec.textures):
        spec.delete(texture)
    floor = spec.worldbody.add_geom(name="floor", type=mujoco.mjtGeom.mjGEOM_PLANE, size=[0, 0, 0.05],
                                    rgba=[0.9, 0.9, 0.9, 1], contype=1, conaffinity=1, condim=3, priority=0,
                                    friction=[0.01, 0.01, 0.01], solmix=1.0)  # terrain_collisions()
    floor.solref[:] = FLOOR_SOLREF
    floor.solimp[:] = FLOOR_SOLIMP
    spec.worldbody.add_light(pos=[0, 0, 3], dir=[0, 0, -1])
    opt = spec.option
    opt.timestep = SIM_TIMESTEP
    opt.integrator = mujoco.mjtIntegrator.mjINT_IMPLICITFAST
    opt.solver = mujoco.mjtSolver.mjSOL_NEWTON
    opt.cone = mujoco.mjtCone.mjCONE_PYRAMIDAL
    opt.iterations = SOLVER_ITERATIONS
    opt.ls_iterations = LS_ITERATIONS
    opt.ccd_iterations = CCD_ITERATIONS
    opt.impratio = 1.0
    model = spec.compile()
    data = mujoco.MjData(model)

    names = [model.joint(j).name for j in range(model.njnt)]
    jid = [next(j for j, n in enumerate(names) if n == name or n.endswith("/" + name)) for name in policy.joint_names]
    qadr, dadr = model.jnt_qposadr[jid], model.jnt_dofadr[jid]
    ctrl = np.array([int(np.flatnonzero((model.actuator_trntype == mujoco.mjtTrn.mjTRN_JOINT)
                                        & (model.actuator_trnid[:, 0] == j))[0]) for j in jid])

    # The gains the robot will be sent (ONNX metadata) must be the ones the policy trained with.
    kp, kd = model.actuator_gainprm[ctrl, 0], -model.actuator_biasprm[ctrl, 2]
    bad = [n for n, a, b, c, d in zip(policy.joint_names, kp, policy.stiffness, kd, policy.damping)
           if abs(a - b) > 1e-4 or abs(c - d) > 1e-4]
    if bad:
        raise SystemExit(f"PD gains in the ONNX metadata differ from the task's actuators for {bad}")

    # Torque-speed limits (BoosterEntity): full torque up to the knee speed, linear to 0 at no-load speed.
    peak, speed, width = (np.zeros(len(jid)) for _ in range(3))
    for act in robot_cfg.articulation.actuators:
        motor = act.motor
        for i, name in enumerate(policy.joint_names):
            if any(re.fullmatch(e, name) for e in act.target_names_expr):
                peak[i] = act.effort_limit
                v = motor.velocity_limit
                if v is None or not np.isfinite(v):
                    speed[i], width[i] = np.inf, 1.0
                else:
                    speed[i], width[i] = v, max(v - motor.effective_knee_point_velocity, 1e-6)
    if not peak.all():
        raise SystemExit("no effort limit for some joints")

    trunk = next(b for b in range(model.nbody) if model.body(b).name.split("/")[-1] == "Trunk")
    gyro_id = next(s for s in range(model.nsensor) if model.sensor(s).name.split("/")[-1] == "imu_ang_vel")
    a = model.sensor_adr[gyro_id]
    lv_id = next(s for s in range(model.nsensor) if model.sensor(s).name.split("/")[-1] == "imu_lin_vel")
    b = model.sensor_adr[lv_id]
    decimation = round(policy.control_dt / model.opt.timestep)
    return Sim(model, data, qadr, dadr, ctrl, trunk, slice(a, a + 3), slice(b, b + 3), peak, speed, width, decimation)


def physics_step(sim: Sim) -> None:
    v = sim.data.qvel[sim.dadr]
    limit = sim.peak * np.clip((sim.speed - np.abs(v)) / sim.width, 0.0, 1.0)
    sim.model.actuator_forcerange[sim.ctrl, 0] = -limit
    sim.model.actuator_forcerange[sim.ctrl, 1] = limit
    mujoco.mj_step(sim.model, sim.data)


def measure(sim: Sim) -> RobotState:
    d = sim.data
    return RobotState(d.qpos[sim.qadr].copy(), d.qvel[sim.dadr].copy(), d.xquat[sim.trunk].copy(), d.sensordata[sim.gyro].copy())


def reset(sim: Sim, cfg: Config, policy: TrackingPolicy, ref: Reference) -> None:
    d = sim.data
    mujoco.mj_resetData(sim.model, d)
    if cfg.start == "reference":
        trunk = 0  # body 0 of the motion file
        d.qpos[:3] = ref.body_pos[0, trunk]
        d.qpos[3:7] = ref.anchor_quat[0]
        d.qpos[sim.qadr] = ref.joint_pos[0]
        d.qvel[sim.dadr] = ref.joint_vel[0]
        d.ctrl[sim.ctrl] = ref.joint_pos[0]
    else:
        d.qpos[:3] = HOME_KEYFRAME.pos
        d.qpos[3:7] = (1, 0, 0, 0)
        d.qpos[sim.qadr] = policy.default_joint_pos
        d.ctrl[sim.ctrl] = policy.default_joint_pos
    mujoco.mj_forward(sim.model, d)
    if cfg.start == "stand":  # plain PD at the policy's gains (see Config.settle_s)
        for _ in range(round(cfg.settle_s / sim.model.opt.timestep)):
            physics_step(sim)


def body_index(name: str) -> int:
    """Index of a body in a motion file's body arrays (the K1's bodies in model order, world excluded)."""
    m = mujoco.MjModel.from_xml_path(str(K1_XML))
    return m.body(name).id - 1


def run_once(cfg: Config, policy: TrackingPolicy, sim: Sim, clip: Reference, seed: int, frames: list | None) -> dict:
    rng = np.random.default_rng(seed)
    reset(sim, cfg, policy, clip)
    if cfg.start == "stand":
        ref = clip.with_lead_in(sim.data.qpos[sim.qadr].copy(), cfg.blend_s, cfg.hold_start_s)
    else:
        ref = clip
    ref = ref.with_end_hold(cfg.hold_end_s).aligned_to(sim.data.xquat[sim.trunk])
    hand_ids = [body_index(h) for h in HANDS]
    sim_hands = [next(b for b in range(sim.model.nbody) if sim.model.body(b).name.split("/")[-1] == h) for h in HANDS]

    last_action = np.zeros(policy.num_joints)
    states: deque[RobotState] = deque(maxlen=cfg.obs_delay_steps + 1)
    next_push = rng.uniform(1.5, 4.0)
    hand_err, fell_at = [], None
    renderer = None
    for k in range(len(ref)):
        states.append(measure(sim))
        state = states[0]  # oldest = delayed
        priv = None
        if cfg.privileged:  # sim only: true values (no delay) for the terms a robot can't measure
            d = sim.data
            R = ob.quat_to_matrix(d.xquat[sim.trunk])
            priv = {"motion_anchor_pos_b": R.T @ (ref.body_pos[min(k, len(ref) - 1), 0] - d.xpos[sim.trunk]),
                    "base_lin_vel": d.sensordata[sim.linvel].copy()}
        obs = build_observation(policy.observation_names, policy.observation_dims, state, ref.frame(k),
                                last_action, policy.default_joint_pos, priv)
        action = policy.act(obs)
        last_action = action
        sim.data.ctrl[sim.ctrl] = policy.joint_targets(action)
        for _ in range(sim.decimation):
            physics_step(sim)
        t = (k + 1) * policy.control_dt
        if cfg.push and t >= next_push:
            sim.data.qvel[0:2] += rng.uniform(-0.14, 0.14, 2)
            next_push = t + rng.uniform(1.5, 4.0)

        d = sim.data
        up = ob.quat_to_matrix(d.xquat[sim.trunk])[2, 2]
        if d.xpos[sim.trunk][2] < 0.30 or up < 0.5:  # trunk below 30 cm or tilted > 60 deg: fallen
            fell_at = t
            break
        if ref.body_pos is not None and ref.clip_start <= k + 1 < ref.clip_end:
            # Hands relative to the trunk, in the trunk frame: robot vs reference (heading-free).
            R = ob.quat_to_matrix(d.xquat[sim.trunk])
            Rr = ob.quat_to_matrix(ref.anchor_quat[k + 1])
            for hs, hr in zip(sim_hands, hand_ids):
                rob = R.T @ (d.xpos[hs] - d.xpos[sim.trunk])
                tgt = Rr.T @ (ref.body_pos[k + 1, hr] - ref.body_pos[k + 1, 0])
                hand_err.append(np.linalg.norm(rob - tgt))
        if frames is not None:
            if renderer is None:
                renderer = mujoco.Renderer(sim.model, 480, 640)
                cam = mujoco.MjvCamera()
                cam.distance, cam.elevation, cam.azimuth = 2.0, -10.0, 150.0
            cam.lookat[:] = d.xpos[sim.trunk] - [0, 0, 0.2]
            renderer.update_scene(d, cam)
            frames.append(renderer.render())
    return {
        "seed": seed,
        "fell_at_s": fell_at,
        "phase": None if fell_at is None else ("lead-in" if fell_at < ref.clip_start * policy.control_dt
                                                else "end hold" if fell_at >= ref.clip_end * policy.control_dt
                                                else "clip"),
        "hand_err_cm": 100 * float(np.mean(hand_err)) if hand_err else None,
        "seconds": len(ref) * policy.control_dt,
    }


def resolve_policy(cfg: Config) -> Path:
    if cfg.policy:
        return cfg.policy
    if not cfg.wandb_run_path:
        raise SystemExit("Pass --policy or --wandb-run-path")
    import wandb

    out = Path("logs/sim2sim") / cfg.wandb_run_path.split("/")[-1]
    wandb.Api().run(cfg.wandb_run_path).file("policy.onnx").download(root=str(out), replace=True)
    return out / "policy.onnx"


def main() -> None:
    cfg = tyro.cli(Config)
    if cfg.start not in ("stand", "reference"):
        raise SystemExit("--start is stand or reference")
    if cfg.privileged and cfg.start != "reference":
        raise SystemExit("--privileged needs --start reference")
    policy = TrackingPolicy(resolve_policy(cfg))
    clip = Reference.from_npz(cfg.motion_file, cfg.clip)
    if abs(clip.fps * policy.control_dt - 1.0) > 1e-6:
        raise SystemExit(f"motion is {clip.fps:g} fps but the policy runs every {policy.control_dt} s")
    sim = build_sim(cfg.task, policy)
    print(f"[sim2sim] {policy.path} | clip {clip.name} ({clip.seconds:.1f} s) | start={cfg.start} "
          f"delay={cfg.obs_delay_steps} push={cfg.push}")
    results = []
    for seed in range(cfg.runs):
        frames = [] if (cfg.video and seed == 0) else None
        r = run_once(cfg, policy, sim, clip, seed, frames)
        results.append(r)
        status = "OK  " if r["fell_at_s"] is None else f"FELL at {r['fell_at_s']:.2f} s ({r['phase']})"
        hand = f"hands {r['hand_err_cm']:.1f} cm" if r["hand_err_cm"] is not None else ""
        print(f"  run {seed}: {status} {hand}")
        if frames:
            import mediapy

            cfg.video.parent.mkdir(parents=True, exist_ok=True)
            mediapy.write_video(str(cfg.video), frames, fps=1 / policy.control_dt)
            print(f"  video -> {cfg.video}")
    ok = sum(r["fell_at_s"] is None for r in results)
    errs = [r["hand_err_cm"] for r in results if r["hand_err_cm"] is not None and r["fell_at_s"] is None]
    print(f"[sim2sim] {ok}/{len(results)} without a fall" + (f", hands {np.mean(errs):.1f} cm" if errs else ""))


if __name__ == "__main__":
    main()
