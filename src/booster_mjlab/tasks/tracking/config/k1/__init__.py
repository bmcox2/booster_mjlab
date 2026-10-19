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
