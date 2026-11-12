"""Gesture generator (notes/gesture_plan.md): turn speech audio into a K1 reference by retrieving
pieces of real BEAT2 motion whose own audio matches.

- ``audio``: speech features at the motion frame rate (loudness, onsets, pitch, speech/pause).
- ``motion``: hand features of K1 clips and the cut into gesture units.
- ``sync``: the per-take jaw check that BEAT2 audio and motion line up.
- ``library``: builds the library (features + units of every usable clip) once, cached.
- ``analysis``: does audio predict hand motion, and by how much? (step 2's key question)

CLI: ``uv run gesture <command>`` (``booster_mjlab.gesture.cli``). Only numpy / scipy / mujoco, so
the runtime part can later run on the robot.
"""
