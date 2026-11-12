"""The exported tracking policy (``policy.onnx``) and the metadata stored inside it."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import onnxruntime as ort


def _floats(text: str) -> np.ndarray:
    return np.array([float(v) for v in text.split(",")], dtype=np.float64)


class TrackingPolicy:
    """``act(obs) -> action``; ``joint_targets(action)`` turns an action into PD targets.

    Attributes come from the ONNX metadata (see ``K1MotionTrackingRunner.export_deploy_policy``):
    joint_names (the policy's joint order), default_joint_pos, stiffness / damping (PD gains),
    action_scale, observation_names / observation_dims, control_dt.
    """

    def __init__(self, onnx_path: str | Path):
        self.path = Path(onnx_path)
        self.session = ort.InferenceSession(str(self.path), providers=["CPUExecutionProvider"])
        md = self.session.get_modelmeta().custom_metadata_map
        missing = {"joint_names", "observation_names", "observation_dims", "control_dt"} - md.keys()
        if missing:
            raise ValueError(
                f"{self.path} has no {sorted(missing)} metadata: export it with `uv run export-tracking-policy` "
                "(mjlab's motion-bundled ONNX is a different file)"
            )
        self.metadata = md
        self.joint_names: list[str] = md["joint_names"].split(",")
        self.default_joint_pos = _floats(md["default_joint_pos"])
        self.stiffness = _floats(md["joint_stiffness"])
        self.damping = _floats(md["joint_damping"])
        self.action_scale = _floats(md["action_scale"])
        self.observation_names: list[str] = md["observation_names"].split(",")
        self.observation_dims: list[int] = [int(round(v)) for v in _floats(md["observation_dims"])]
        self.control_dt = float(md["control_dt"])
        # Frames of history per term (0 = current frame only; older exports have no key).
        self.history_length = int(round(float(md.get("observation_history_length", 0))))
        frames = max(1, self.history_length)
        if any(d % frames for d in self.observation_dims):
            raise ValueError(f"observation_dims {self.observation_dims} don't divide into {frames} history frames")
        # One frame's term sizes: what build_observation makes each step (ObservationHistory stacks them).
        self.frame_dims: list[int] = [d // frames for d in self.observation_dims]
        self.input_name = self.session.get_inputs()[0].name
        self.obs_dim = int(self.session.get_inputs()[0].shape[-1])
        if sum(self.observation_dims) != self.obs_dim:
            raise ValueError(f"observation_dims sum to {sum(self.observation_dims)}, the network takes {self.obs_dim}")

    @property
    def num_joints(self) -> int:
        return len(self.joint_names)

    def act(self, obs: np.ndarray) -> np.ndarray:
        out = self.session.run(None, {self.input_name: obs.astype(np.float32).reshape(1, -1)})[0]
        return out[0].astype(np.float64)

    def joint_targets(self, action: np.ndarray) -> np.ndarray:
        return self.default_joint_pos + self.action_scale * action
