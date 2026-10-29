"""Run a trained tracking policy outside mjlab: in plain MuJoCo (sim2sim) or on the robot.

Only numpy and onnxruntime, so the same code can run on the K1's onboard computer:

- ``policy.TrackingPolicy``: loads ``policy.onnx`` (written next to every checkpoint, or by
  ``uv run export-tracking-policy``) and its metadata: joint order, default pose, PD gains,
  action scale, observation layout, control period.
- ``observation.build_observation``: the policy's observation vector from what a robot measures
  (joint encoders, IMU orientation and gyro) plus the current reference frame, matching mjlab's
  terms exactly.
- ``reference.Reference``: a reference clip played at the control rate, with a lead-in from the
  robot's standing pose, a hold at the end, and its heading aligned to the robot's.

A backend (``scripts/sim2sim.py`` now; a Booster SDK one later) supplies ``RobotState`` each control
step and applies the joint targets with the policy's PD gains. notes/demo_plan.md.
"""

from booster_mjlab.deploy.observation import RobotState, build_observation
from booster_mjlab.deploy.policy import TrackingPolicy
from booster_mjlab.deploy.reference import RefFrame, Reference

__all__ = ("RefFrame", "Reference", "RobotState", "TrackingPolicy", "build_observation")
