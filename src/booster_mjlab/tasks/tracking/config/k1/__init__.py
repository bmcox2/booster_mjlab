from mjlab.tasks.registry import register_mjlab_task

from booster_mjlab.tasks.tracking.runner import K1MotionTrackingRunner

from .env_cfgs import booster_k1_flat_tracking_env_cfg
from .rl_cfg import booster_k1_tracking_ppo_runner_cfg

register_mjlab_task(
    task_id="Mjlab-Tracking-Flat-Booster-K1",
    env_cfg=booster_k1_flat_tracking_env_cfg(),
    play_env_cfg=booster_k1_flat_tracking_env_cfg(play=True),
    rl_cfg=booster_k1_tracking_ppo_runner_cfg(),
    runner_cls=K1MotionTrackingRunner,
)

# Deployable variant: the policy sees only what the real K1 measures (joint encoders, IMU orientation
# and turn rate) plus the reference. notes/demo_plan.md.
register_mjlab_task(
    task_id="Mjlab-Tracking-Flat-Booster-K1-No-State-Estimation",
    env_cfg=booster_k1_flat_tracking_env_cfg(has_state_estimation=False),
    play_env_cfg=booster_k1_flat_tracking_env_cfg(play=True, has_state_estimation=False),
    rl_cfg=booster_k1_tracking_ppo_runner_cfg(),
    runner_cls=K1MotionTrackingRunner,
)

# Deployable + the last 10 policy observations (0.2 s at 50 Hz). Experiment vs the variant above
# (notes/roadmap.md, exit criterion 8).
register_mjlab_task(
    task_id="Mjlab-Tracking-Flat-Booster-K1-No-State-Estimation-History10",
    env_cfg=booster_k1_flat_tracking_env_cfg(has_state_estimation=False, actor_history_length=10),
    play_env_cfg=booster_k1_flat_tracking_env_cfg(play=True, has_state_estimation=False, actor_history_length=10),
    rl_cfg=booster_k1_tracking_ppo_runner_cfg(),
    runner_cls=K1MotionTrackingRunner,
)
