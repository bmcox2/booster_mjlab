"""Thin wrapper around mjlab's play script.

Swaps the viser viewer for :class:`RecordingViserPlayViewer`, which
adds a record / stop-recording button that captures the browser view to an mp4
under ``--record-dir``. Frames are timed by the sim clock, so the video plays
back in real time even when the machine can't step the policy at full speed.

For headless recording (``--video True``) it also sets up the video itself,
without editing mjlab: a closer camera (mjlab's tracking camera is 2.8 m away,
so the 0.95 m K1 fills a third of the frame), 1080p, a higher-quality encode
than mediapy's default, and optionally no debug overlays (``--hide-overlays``:
the green reference ghost and the magenta foot-height rays). These only touch
the offscreen video renderer, not the interactive viewer.
"""

import dataclasses
import functools
import sys
import types

import mediapy
import mjlab.envs.manager_based_rl_env as mjlab_env
import mjlab.scripts.play as mjlab_play
import mjlab.utils.wrappers.video_recorder as mjlab_video_recorder
from mjlab.viewer.offscreen_renderer import OffscreenRenderer

from booster_mjlab.viewer import DEFAULT_VIDEO_DIR, RecordingViserPlayViewer

# Headless video defaults (each overridable by its flag). Distance 1.8 m with a 45 deg vertical field of
# view frames ~1.5 m around the trunk: the whole K1 at ~2/3 of the frame height. qp: x264 quantizer,
# lower = better (18 is near visually lossless).
VIDEO_CAMERA = {"distance": 1.8, "elevation": -8.0, "azimuth": None, "fovy": 45.0}
VIDEO_QP = 18
VIDEO_SIZE = ("1920", "1080")


def _pop_flag(argv: list[str], flag: str) -> str | None:
    """Remove ``--flag VALUE`` or ``--flag=VALUE`` from argv; return VALUE."""
    for i, tok in enumerate(argv):
        if tok == flag:
            if i + 1 >= len(argv):
                raise SystemExit(f"{flag} requires a value")
            value = argv[i + 1]
            del argv[i : i + 2]
            return value
        if tok.startswith(flag + "="):
            value = tok.split("=", 1)[1]
            del argv[i]
            return value
    return None


def _pop_switch(argv: list[str], flag: str) -> bool:
    """Remove a bare ``--flag`` from argv; return whether it was there."""
    if flag in argv:
        argv.remove(flag)
        return True
    return False


def _has_flag(argv: list[str], flag: str) -> bool:
    return any(tok == flag or tok.startswith(flag + "=") for tok in argv)


def _setup_video(argv: list[str]) -> None:
    """Camera, size, encoding quality and overlays for ``--video True`` recordings."""
    camera = {}
    for key, default in VIDEO_CAMERA.items():
        value = _pop_flag(argv, f"--video-{key}")
        camera[key] = float(value) if value is not None else default
    camera = {k: v for k, v in camera.items() if v is not None}
    qp = int(_pop_flag(argv, "--video-qp") or VIDEO_QP)
    hide_overlays = _pop_switch(argv, "--hide-overlays")
    if not _has_flag(argv, "--video-width") and not _has_flag(argv, "--video-height"):
        argv += ["--video-width", VIDEO_SIZE[0], "--video-height", VIDEO_SIZE[1]]

    class VideoRenderer(OffscreenRenderer):
        def __init__(self, model, cfg, *args, **kwargs):
            super().__init__(model, dataclasses.replace(cfg, **camera), *args, **kwargs)

        def update(self, data, debug_vis_callback=None, camera=None):
            super().update(data, None if hide_overlays else debug_vis_callback, camera)

    # mjlab's env imported the class by name, so swap it there. The env only builds an offscreen renderer
    # for render_mode="rgb_array" (headless video), so the interactive viewer is unaffected.
    mjlab_env.OffscreenRenderer = VideoRenderer  # type: ignore[misc]
    mjlab_video_recorder.media = types.SimpleNamespace(  # type: ignore[assignment]
        write_video=functools.partial(mediapy.write_video, qp=qp)
    )


def main() -> None:
    argv = sys.argv[1:]
    if "-h" in argv or "--help" in argv:
        # mjlab's help won't list our flags (we pop them before mjlab parses), so surface them here.
        print(
            "booster_mjlab play adds:\n"
            "  --record-dir STR  (viser viewer: where recorded mp4s are written, "
            f"default {DEFAULT_VIDEO_DIR})\n"
            "  for --video True (headless mp4, default size "
            f"{VIDEO_SIZE[0]}x{VIDEO_SIZE[1]}):\n"
            f"  --video-distance M    camera distance from the trunk (default {VIDEO_CAMERA['distance']})\n"
            f"  --video-elevation DEG camera pitch, negative looks down (default {VIDEO_CAMERA['elevation']})\n"
            "  --video-azimuth DEG   camera angle around the robot (default: the task's, 120)\n"
            f"  --video-fovy DEG      vertical field of view (default {VIDEO_CAMERA['fovy']})\n"
            f"  --video-qp INT        encode quality, lower = better (default {VIDEO_QP})\n"
            "  --hide-overlays       no reference ghost / foot-height rays in the video\n",
            file=sys.stderr,
        )
    record_dir = _pop_flag(argv, "--record-dir")
    _setup_video(argv)
    sys.argv = [sys.argv[0], *argv]

    # Viser viewer with a record button.
    mjlab_play.ViserPlayViewer = functools.partial(  # type: ignore[assignment]
        RecordingViserPlayViewer,
        video_dir=record_dir or DEFAULT_VIDEO_DIR,
    )

    mjlab_play.main()


if __name__ == "__main__":
    main()
