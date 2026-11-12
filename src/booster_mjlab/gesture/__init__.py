"""Gesture generator (notes/gesture_plan.md): turn speech audio into a K1 reference by retrieving
pieces of real BEAT2 motion whose own audio matches.

- ``audio``: speech features at the motion frame rate (loudness, onsets, pitch, speech/pause).
- ``motion``: hand features of K1 clips and the cut into gesture units.
- ``sync``: the per-take jaw check that BEAT2 audio and motion line up.
- ``library``: builds the library (features + units of every usable clip) once, cached.
- ``analysis``: does audio predict hand motion, and by how much? (step 2's key question)
- ``generate``: a whole reply -> K1 reference (offline); ``serve``: the same as a local service.
- ``stream`` / ``live``: motion made while the conversation runs, tracked live in MuJoCo (step 7).

CLI: ``uv run gesture <command>`` (``booster_mjlab.gesture.cli``). Only numpy / scipy / mujoco, so
the runtime part can later run on the robot.
"""

import os as _os

# `gesture live`'s MuJoCo window goes through X11 (XWayland): GLFW's Wayland mode crashed at start on
# Ubuntu 24.04 (GLib: settings key 'antialiasing' missing). Here because it must be set before
# anything imports glfw, which `import mujoco` does.
_os.environ.setdefault("PYGLFW_LIBRARY_VARIANT", "x11")
