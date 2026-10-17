"""Evaluate a trained motion-tracking policy: N rollouts of the full clip, pass/fail + tracking errors.

Milestone 1 asks: does the K1 play the whole gesture without falling, every time? Training charts
can't answer that (episodes there start mid-clip, get pushed, and are averaged over thousands of
robots), so this runs a clean, repeatable test:

- N robots (default 50) per clip run in parallel, one rollout each, from frame 0 to the last frame.
  A combined motion file (combine-motions) is evaluated clip by clip, one result row per clip;
  every clip runs at the same time, N robots each, and each robot stops counting at the end of
  its own clip.
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
    uv run eval-tracking --wandb-run-path ... --clips wave_000508 wave_001104   # some clips only

Results print as a table (one row per clip) and are saved to logs/eval/<run>_<motion>[_push].json.
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

from booster_mjlab.tasks.tracking.multi_motion_command import MultiMotionCommand, read_clip_table

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
    """Rollouts per clip."""
    clips: tuple[str, ...] = ()
    """Evaluate only these clips of a combined motion file (default: all)."""
    max_envs: int = 4096
    """Most robots simulated at once; clips are evaluated in batches if num_rollouts x clips is more."""
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
    return max(0.0, (centre - spread) / (1 + z * z / n))  # 0 successes rounds to -1e-17


def resolve_motion(cfg: Config) -> tuple[str, str]:
    """Return (local motion.npz path, label)."""
    if cfg.motion_file:
        path = Path(cfg.motion_file)
        return cfg.motion_file, path.parent.name if path.name == "motion.npz" else path.stem
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


def summarize(rollouts: list[dict], clip_seconds: float) -> dict:
    """Pass/fail and mean tracking errors over one clip's rollouts."""
    n = len(rollouts)
    k = sum(r["success"] for r in rollouts)
    ok_runs = [r for r in rollouts if r["success"]] or rollouts

    def stat(key, fn=np.mean):
        return float(fn([r[key] for r in ok_runs]))

    return {
        "successes": k,
        "rollouts": n,
        "success_rate": k / n,
        "success_rate_95_lower": wilson_lower(k, n),
        "passed": k == n,
        "clip_seconds": clip_seconds,
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


def failure_line(rollouts: list[dict]) -> str:
    reasons: dict[str, int] = {}
    for r in rollouts:
        if not r["success"]:
            reasons[r["fail_reason"]] = reasons.get(r["fail_reason"], 0) + 1
    times = [r["fail_time_s"] for r in rollouts if not r["success"]]
    return f"failures by reason: {reasons}; at t = {min(times):.2f}-{max(times):.2f} s"


def run_batch(env, policy, cmd: MultiMotionCommand, batch: list[int], ctx: dict) -> dict[int, list[dict]]:
    """Roll out cfg.num_rollouts robots on each clip in `batch` at once; return rollouts per clip."""
    n, dev, dt = ctx["n"], cmd.device, ctx["dt"]
    terms, fail_terms, groups = ctx["terms"], ctx["fail_terms"], ctx["groups"]
    hand_ids, foot_ids = ctx["hand_ids"], ctx["foot_ids"]
    num_envs = cmd.num_envs

    # Robots [i*n, (i+1)*n) play batch[i]. Spare robots (last batch only) replay batch[0], uncounted.
    slot = torch.arange(num_envs, device=dev) // n
    valid = slot < len(batch)
    assign = torch.tensor(batch, device=dev)[torch.where(valid, slot, 0)]
    # Reset under inference_mode too: the previous batch's steps made env buffers (e.g. the actuator
    # delay buffer) inference tensors, which can't be updated in place outside it.
    with torch.inference_mode():
        cmd.clip_ids[:] = assign
        obs, _ = env.reset()  # play mode = "start" sampling: every robot at frame 0 of its own clip

    # Steps until each robot reaches its clip's last frame. One more step and it would move on to
    # the next clip (a teleport), so each robot stops counting there.
    remaining = cmd.clip_lengths[assign] - 1 - cmd.clip_frames
    num_steps = int(remaining[valid].max())
    stance_z = ctx["stance_z"][assign]  # (num_envs, 2)
    settle_steps = ctx["settle_steps"]

    alive = valid.clone()
    fail_step = torch.full((num_envs,), -1, dtype=torch.long, device=dev)
    fail_reason = [""] * num_envs
    sums = {k: torch.zeros(num_envs, device=dev) for k in ("body_cm", "hand_cm", "arms", "head", "legs", "height_cm")}
    max_hand_cm = torch.zeros(num_envs, device=dev)
    max_tilt = torch.zeros(num_envs, 2, device=dev)
    steps_alive = torch.zeros(num_envs, device=dev)
    drift_cm = torch.zeros(num_envs, device=dev)

    with torch.inference_mode():
        for step in range(num_steps):
            obs, _, dones, _ = env.step(policy(obs))
            in_clip = step < remaining
            done = dones.bool() & alive & in_clip
            if done.any():
                # The env auto-resets finished robots; record why, then stop counting them.
                for i in torch.nonzero(done).flatten().tolist():
                    fail_step[i] = step + 1
                    fail_reason[i] = ",".join(t for t in fail_terms if bool(terms.get_term(t)[i])) or "unknown"
                alive &= ~done
            counting = alive & in_clip
            if not counting.any():
                break
            # Drift at each robot's own last frame.
            last = counting & (step == remaining - 1)
            if last.any():
                d = torch.linalg.norm(cmd.robot_anchor_pos_w[:, :2] - cmd.anchor_pos_w[:, :2], dim=-1) * 100
                drift_cm = torch.where(last, d, drift_cm)
            if step < settle_steps:
                continue
            a = counting.float()
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

    # Per-rollout results (errors are averages over the steps that rollout was alive).
    denom = steps_alive.clamp(min=1)
    out: dict[int, list[dict]] = {c: [] for c in batch}
    for i in torch.nonzero(valid).flatten().tolist():
        ok = bool(alive[i])
        c = int(assign[i])
        out[c].append({
            "clip": cmd.clip_names[c],
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
    ctx["clip_steps"].update({c: int(remaining[assign == c][0]) for c in batch})
    return out


def print_single(s: dict, rollouts: list[dict]) -> None:
    """The detailed report for one clip."""
    k, n = s["successes"], s["rollouts"]
    verdict = "PASS" if s["passed"] else "FAIL"
    print(f"Full clip, no falls:   {k}/{n}  -> {verdict}")
    print(f"  95% confident the true success rate is at least {s['success_rate_95_lower']:.1%}")
    if k < n:
        print(f"  {failure_line(rollouts)}")
    which = "successful rollouts" if k else "all rollouts, none succeeded"
    print(f"\nTracking quality ({which}; lower is better):")
    print(f"  hand position error    mean {s['hand_err_cm_mean']:5.1f} cm   worst moment {s['hand_err_cm_worst']:5.1f} cm")
    print(f"  all-body position err  mean {s['body_err_cm_mean']:5.1f} cm")
    print(f"  joint angle error      arms {s['arm_joint_err_deg_mean']:4.1f} deg   head {s['head_joint_err_deg_mean']:4.1f} deg   legs {s['leg_joint_err_deg_mean']:4.1f} deg")
    print(f"  trunk height vs ref    {s['height_err_cm_mean']:+5.1f} cm   (negative = robot lower)")
    print(f"  drift across floor     {s['final_drift_cm_mean']:5.1f} cm at clip end")
    print(f"  max foot tilt on floor L {s['max_foot_tilt_deg'][0]:4.1f} deg   R {s['max_foot_tilt_deg'][1]:4.1f} deg")


def print_table(summaries: dict[str, dict], rollouts: dict[str, list[dict]]) -> None:
    """One row per clip. Errors are over successful rollouts (all rollouts if none succeeded)."""
    w = max(len("clip"), *(len(c) for c in summaries))
    print(f"{'clip':<{w}}  {'secs':>5}  {'no falls':<11}  {'hand cm':>11}  {'body':>4}  "
          f"{'arms/head/legs':>14}  {'height':>6}  {'drift':>5}  {'foot tilt L/R':>13}")
    print(f"{'':<{w}}  {'':>5}  {'':<11}  {'mean/worst':>11}  {'cm':>4}  {'deg':>14}  {'cm':>6}  {'cm':>5}  {'deg':>13}")
    for c, s in summaries.items():
        ok = f"{s['successes']}/{s['rollouts']} {'PASS' if s['passed'] else 'FAIL'}"
        print(f"{c:<{w}}  {s['clip_seconds']:>5.2f}  {ok:<11}  "
              f"{s['hand_err_cm_mean']:>4.1f} / {s['hand_err_cm_worst']:>4.1f}  {s['body_err_cm_mean']:>4.1f}  "
              f"{s['arm_joint_err_deg_mean']:>4.1f}/{s['head_joint_err_deg_mean']:>4.1f}/{s['leg_joint_err_deg_mean']:>4.1f}  "
              f"{s['height_err_cm_mean']:>+6.1f}  {s['final_drift_cm_mean']:>5.1f}  "
              f"{s['max_foot_tilt_deg'][0]:>5.1f} / {s['max_foot_tilt_deg'][1]:>4.1f}")
    passed = sum(s["passed"] for s in summaries.values())
    k = sum(s["successes"] for s in summaries.values())
    n = sum(s["rollouts"] for s in summaries.values())
    print(f"\nAll clips: {passed}/{len(summaries)} pass ({k}/{n} rollouts played their whole clip with no falls)")
    for c, s in summaries.items():
        if not s["passed"]:
            print(f"  {c}: {failure_line(rollouts[c])}")


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

    motion_cmd.motion_file, motion_label = resolve_motion(cfg)
    names, lengths = read_clip_table(motion_cmd.motion_file)
    unknown = [c for c in cfg.clips if c not in names]
    if unknown:
        raise SystemExit(f"Unknown clip(s) {unknown}; this motion has: {names}")
    eval_clips = [names.index(c) for c in cfg.clips] if cfg.clips else list(range(len(names)))

    n = cfg.num_rollouts
    per_batch = max(1, min(len(eval_clips), cfg.max_envs // n))
    batches = [eval_clips[i : i + per_batch] for i in range(0, len(eval_clips), per_batch)]
    env_cfg.scene.num_envs = n * per_batch
    env_cfg.seed = cfg.seed
    # Episode length from the clip length: long enough for the longest clip evaluated (+1 s), so a
    # time-out can never end a rollout early. (Play mode already sets it near-infinite; this keeps
    # eval correct on long clips even if that changes.)
    dt = env_cfg.sim.mujoco.timestep * env_cfg.decimation
    env_cfg.episode_length_s = float(lengths[eval_clips].max()) * dt + 1.0

    ckpt_path, ckpt_label = resolve_checkpoint(cfg, agent_cfg.experiment_name)
    print(f"[eval] checkpoint {ckpt_path}\n[eval] motion     {motion_label} ({len(names)} clip{'s' * (len(names) > 1)})")

    env = RslRlVecEnvWrapper(
        ManagerBasedRlEnv(cfg=env_cfg, device=cfg.device), clip_actions=agent_cfg.clip_actions
    )
    runner = (load_runner_cls(cfg.task) or MjlabOnPolicyRunner)(env, asdict(agent_cfg), device=cfg.device)
    runner.load(str(ckpt_path), load_cfg={"actor": True}, strict=True, map_location=cfg.device)
    policy = runner.get_inference_policy(device=cfg.device)

    base = env.unwrapped
    cmd = base.command_manager.get_term("motion")
    assert isinstance(cmd, MultiMotionCommand)
    terms = base.termination_manager
    joint_names = list(cmd.robot.joint_names)
    foot_ids = [cmd.cfg.body_names.index(f) for f in FEET]
    # A foot is "on the floor" within STANCE_HEIGHT of its lowest reference height in that clip.
    stance_z = torch.stack([
        cmd.motion.body_pos_w[s : s + length, foot_ids, 2].min(dim=0).values
        for s, length in zip(cmd.clip_starts.tolist(), cmd.clip_lengths.tolist())
    ]) + STANCE_HEIGHT  # (clips, 2)
    ctx = {
        "n": n,
        "dt": base.step_dt,
        "terms": terms,
        "fail_terms": [t for t in terms.active_terms if not terms.get_term_cfg(t).time_out],
        "groups": {
            "arms": [i for i, j in enumerate(joint_names) if "Shoulder" in j or "Elbow" in j],
            "head": [i for i, j in enumerate(joint_names) if "Head" in j],
            "legs": [i for i, j in enumerate(joint_names) if "Hip" in j or "Knee" in j or "Ankle" in j],
        },
        "hand_ids": [cmd.cfg.body_names.index(h) for h in HANDS],
        "foot_ids": foot_ids,
        "stance_z": stance_z,
        "settle_steps": round(cfg.settle_s / base.step_dt),
        "clip_steps": {},
    }

    t0 = time.time()
    by_clip: dict[int, list[dict]] = {}
    for batch in batches:
        by_clip.update(run_batch(env, policy, cmd, batch, ctx))
    elapsed = time.time() - t0

    rollouts = {names[c]: by_clip[c] for c in eval_clips}
    summaries = {
        names[c]: summarize(by_clip[c], round(ctx["clip_steps"][c] * base.step_dt, 2)) for c in eval_clips
    }

    # Report.
    print(f"\n=== {ckpt_label} on {motion_label}{' (with pushes)' if cfg.push else ''} ===")
    if len(eval_clips) == 1:
        (clip, s), = summaries.items()
        clip_note = f" ({clip})" if len(names) > 1 else ""
        print(f"{n} rollouts x {s['clip_seconds']} s clip{clip_note}, simulated in {elapsed:.1f} s"
              f" (errors skip the first {cfg.settle_s} s)\n")
        print_single(s, rollouts[clip])
    else:
        total_s = sum(s["clip_seconds"] for s in summaries.values())
        print(f"{n} rollouts per clip x {len(eval_clips)} clips ({total_s:.1f} s of motion), simulated in"
              f" {elapsed:.1f} s on {cfg.device} (errors skip the first {cfg.settle_s} s)\n")
        print_table(summaries, rollouts)

    cfg.out_dir.mkdir(parents=True, exist_ok=True)
    motion_slug = motion_label.replace("/", "_").replace(":", "_")
    out = cfg.out_dir / f"{ckpt_label}_{motion_slug}{'_push' if cfg.push else ''}.json"
    report = {
        "config": {k2: str(v) for k2, v in asdict(cfg).items()},
        "checkpoint": str(ckpt_path),
        "motion": motion_label,
        "clips": summaries,
        "rollouts": [r for c in rollouts.values() for r in c],
    }
    if len(summaries) == 1:
        report["summary"] = next(iter(summaries.values()))
    out.write_text(json.dumps(report, indent=2))
    print(f"\nsaved -> {out}")
    env.close()


if __name__ == "__main__":
    main()
