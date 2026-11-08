"""Export clips of a combined motion .npz as one file each, for the robot's deploy task.

booster_deploy's tasks play one clip per file. Each file has the usual arrays (fps, joint_pos, joint_vel,
body_pos_w, body_quat_w, body_lin_vel_w, body_ang_vel_w), plus joint_names and body_names, so the deploy
task can check the order it reads them in instead of assuming it.

With --audio, each clip also gets <clip>.wav: the speaker's BEAT2 audio for exactly the clip's time span (from the
batch build's segments.json), 16-bit PCM so plain `aplay` can play it. The take's .wav must be downloaded first:
    uv run hf download H-Liu1997/BEAT2 --repo-type dataset --local-dir ~/robotics/data/BEAT2 \\
        beat_english_v2.0.0/wave16k/<take>.wav

Usage (from ~/projects/booster-mjlab):
    uv run python tools/export_deploy_clip.py ~/robotics/data/beat2_full_torso/combined/beat2-full-torso-heldout-val.npz \\
        --clips nidal_0_13_13_t18-36 --out-dir ../booster_deploy/tasks/gesture_tracking/motions [--audio]
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mujoco
import numpy as np
from scipy.io import wavfile

K1_XML = Path(__file__).resolve().parents[1] / "src/booster_mjlab/robots/booster_k1/xmls/k1.xml"
SEGMENTS = Path.home() / "robotics/data/beat2_full_torso/segments.json"
WAVE_DIR = Path.home() / "robotics/data/BEAT2/beat_english_v2.0.0/wave16k"
ARRAYS = ("joint_pos", "joint_vel", "body_pos_w", "body_quat_w", "body_lin_vel_w", "body_ang_vel_w")


def k1_names() -> tuple[list[str], list[str]]:
    """Joint and body names in motion-file order: model order, without the floating base and the world."""
    model = mujoco.MjModel.from_xml_path(str(K1_XML))
    joints = [model.joint(j).name for j in range(1, model.njnt)]
    bodies = [model.body(b).name for b in range(1, model.nbody)]
    return joints, bodies


def write_audio(clip: str, seconds: float, segments: dict[str, dict], wave_dir: Path, out: Path) -> None:
    """The clip's span of its take's audio, as 16-bit PCM."""
    seg = segments.get(clip)
    if seg is None:
        raise SystemExit(f"{clip} isn't in the segments file, so its audio time span is unknown")
    src = wave_dir / f"{seg['take']}.wav"
    if not src.exists():
        raise SystemExit(f"{src} not downloaded (see this file's docstring)")
    rate, audio = wavfile.read(src)
    a, b = round(seg["start"] * rate), min(round(seg["end"] * rate), len(audio))
    audio = audio[a:b]
    if audio.dtype.kind == "f":  # BEAT2 mixes float32 and int16 files
        audio = (np.clip(audio, -1.0, 1.0) * 32767).astype(np.int16)
    if abs(len(audio) / rate - seconds) > 0.1:
        raise SystemExit(f"{clip}: audio is {len(audio) / rate:.2f} s but the motion is {seconds:.2f} s")
    wavfile.write(out, rate, audio)
    print(f"{out} ({len(audio) / rate:.1f} s, from {seg['take']} {seg['start']:.2f}-{seg['end']:.2f} s)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("motion_file", type=Path)
    parser.add_argument("--clips", nargs="+", required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--audio", action="store_true", help="also write each clip's audio as <clip>.wav")
    parser.add_argument("--segments", type=Path, default=SEGMENTS)
    parser.add_argument("--wave-dir", type=Path, default=WAVE_DIR)
    args = parser.parse_args()

    segments = {}
    if args.audio:
        takes = json.loads(args.segments.read_text())["takes"]
        segments = {c["name"]: c for take in takes for c in take["clips"]}

    joints, bodies = k1_names()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    with np.load(args.motion_file, allow_pickle=False) as data:
        names = [str(n) for n in data["clip_names"]]
        starts = np.concatenate([[0], np.cumsum(data["clip_lengths"])])
        missing = [c for c in args.clips if c not in names]
        if missing:
            raise SystemExit(f"not in {args.motion_file.name}: {missing}")
        arrays = {key: data[key] for key in ARRAYS}
        if arrays["joint_pos"].shape[1] != len(joints) or arrays["body_pos_w"].shape[1] != len(bodies):
            raise SystemExit(f"{args.motion_file.name} doesn't have the K1's {len(joints)} joints and {len(bodies)} bodies")
        for clip in args.clips:
            i = names.index(clip)
            s, e = int(starts[i]), int(starts[i + 1])
            out = args.out_dir / f"{clip}.npz"
            seconds = (e - s) / float(np.asarray(data["fps"]).reshape(-1)[0])
            np.savez(out, fps=data["fps"], joint_names=np.array(joints), body_names=np.array(bodies),
                     **{key: value[s:e] for key, value in arrays.items()})
            print(f"{out} ({seconds:.1f} s)")
            if args.audio:
                write_audio(clip, seconds, segments, args.wave_dir, out.with_suffix(".wav"))


if __name__ == "__main__":
    main()
