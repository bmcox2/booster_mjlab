"""Hand features of K1 motion clips, and the cut into gesture units.

Hands are measured in the trunk's own frame (position relative to the trunk, rotated into the
trunk's orientation), so turning or swaying the whole body doesn't count as gesturing.

A **unit** is a short piece of motion, ideally one gesture: preparation -> stroke -> hold ->
retraction (McNeill's gesture phases). Units are cut where the hands are slowest, which is usually
between gestures, and kept between ``min_s`` and ``max_s`` long.
"""

from __future__ import annotations

import numpy as np
from scipy.ndimage import uniform_filter1d
from scipy.signal import find_peaks

HANDS = ("left_hand_end_ball", "right_hand_end_ball")
TRUNK = "Trunk"
MOTION_FEATURES = ("speed_l", "speed_r", "speed", "lx", "ly", "lz", "rx", "ry", "rz")


def quat_to_matrix(q: np.ndarray) -> np.ndarray:
    """(..., 4) w, x, y, z -> (..., 3, 3)."""
    q = q / np.linalg.norm(q, axis=-1, keepdims=True)
    w, x, y, z = np.moveaxis(q, -1, 0)
    return np.stack([
        np.stack([1 - 2 * (y * y + z * z), 2 * (x * y - w * z), 2 * (x * z + w * y)], -1),
        np.stack([2 * (x * y + w * z), 1 - 2 * (x * x + z * z), 2 * (y * z - w * x)], -1),
        np.stack([2 * (x * z - w * y), 2 * (y * z + w * x), 1 - 2 * (x * x + y * y)], -1),
    ], -2)


def hand_features(body_pos: np.ndarray, body_quat: np.ndarray, body_names: list[str], fps: float) -> np.ndarray:
    """(T, len(MOTION_FEATURES)): left / right / total hand speed (m/s) and both hand positions
    (m) in the trunk frame (x forward, y left, z up)."""
    t = body_names.index(TRUNK)
    R = quat_to_matrix(body_quat[:, t])  # world <- trunk
    cols_pos, speeds = [], []
    for h in HANDS:
        rel = body_pos[:, body_names.index(h)] - body_pos[:, t]
        local = np.einsum("tji,tj->ti", R, rel)  # R^T @ rel
        v = np.linalg.norm(np.diff(local, axis=0), axis=1) * fps
        speeds.append(np.concatenate([v[:1], v]))
        cols_pos.append(local)
    total = speeds[0] + speeds[1]
    return np.column_stack([speeds[0], speeds[1], total, cols_pos[0], cols_pos[1]])


FEET = ("left_foot_link", "right_foot_link")


def twist(body_pos: np.ndarray, body_quat: np.ndarray, body_names: list[str]) -> np.ndarray:
    """(T,) trunk heading minus stance heading (rad): how far the trunk is turned relative to the
    feet. The stance faces perpendicular to the line from the right foot to the left. Units whose
    twist differs force the trunk to turn at the seam once the feet are locked (generate.foot_lock)."""
    R = quat_to_matrix(body_quat[:, body_names.index(TRUNK)])
    trunk_yaw = np.arctan2(R[:, 1, 0], R[:, 0, 0])
    across = body_pos[:, body_names.index(FEET[0]), :2] - body_pos[:, body_names.index(FEET[1]), :2]
    stance_yaw = np.arctan2(across[:, 1], across[:, 0]) - np.pi / 2
    return (trunk_yaw - stance_yaw + np.pi) % (2 * np.pi) - np.pi


def cut_units(speed: np.ndarray, fps: float, min_s: float = 0.5, max_s: float = 3.0,
              smooth_s: float = 0.2, min_dip: float = 0.1, relative_dip: bool = True) -> list[int]:
    """Unit boundaries (frame indices, first 0, last len(speed)) where the hands pause.

    A pause is a local minimum of the smoothed hand speed whose dip (scipy's *prominence*: how far
    it is below the lower of the two peaks around it) is at least ``min_dip`` m/s and, with
    ``relative_dip``, at least the speed at the minimum itself, i.e. the hands at least halve their
    speed. That skips wiggles while still (cut at 0.1 m/s noise) and dips in the middle of a
    movement (a seam there would blend two fast motions). Too-short pieces merge into a neighbour
    (dropping the boundary with more motion); too-long pieces split at their quietest frame
    (nearest the middle among near-quietest)."""
    n = len(speed)
    lo, hi = max(1, round(min_s * fps)), max(2, round(max_s * fps))
    if n <= lo:
        return [0, n]
    s = uniform_filter1d(np.asarray(speed, float), size=max(1, round(smooth_s * fps)), mode="nearest")
    minima, props = find_peaks(-s, distance=max(1, round(0.25 * fps)), prominence=min_dip)
    if relative_dip:
        minima = minima[props["prominences"] >= s[minima]]
    bounds = [0, *[int(m) for m in minima], n]

    # Merge pieces shorter than min_s.
    while len(bounds) > 2:
        lengths = np.diff(bounds)
        i = int(np.argmin(lengths))
        if lengths[i] >= lo:
            break
        inner = [j for j in (i, i + 1) if 0 < j < len(bounds) - 1]
        drop = max(inner, key=lambda j: s[bounds[j]])  # keep the quieter boundary
        bounds.pop(drop)

    # Split pieces longer than max_s.
    out = [0]
    stack = [(bounds[k], bounds[k + 1]) for k in range(len(bounds) - 1)][::-1]
    while stack:
        a, b = stack.pop()
        if b - a <= hi:
            out.append(b)
            continue
        cand = np.arange(a + lo, b - lo + 1)
        seg = s[cand]
        near_min = cand[seg <= seg.min() + 0.1 * (seg.max() - seg.min() + 1e-12)]
        c = int(near_min[np.argmin(np.abs(near_min - (a + b) / 2))])
        stack.extend([(c, b), (a, c)])
    return out
