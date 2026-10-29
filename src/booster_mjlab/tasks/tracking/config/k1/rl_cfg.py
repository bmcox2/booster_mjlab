"""RL configuration for Booster K1 tracking task."""

from mjlab.rl import RslRlModelCfg
from booster_mjlab.rl.config import (
    RslRlOnPolicyRunnerCfg,
    RslRlPpoAlgorithmCfg,
)


def booster_k1_tracking_ppo_runner_cfg() -> RslRlOnPolicyRunnerCfg:
    """Create RL runner configuration for Booster K1 tracking task."""
    return RslRlOnPolicyRunnerCfg(
        actor=RslRlModelCfg(
            hidden_dims=(512, 256, 128),
            activation="elu",
            obs_normalization=True,
            distribution_cfg={
                "class_name": "rsl_rl.modules.distribution:GaussianDistribution",
                "init_std": 1.0,
            },
        ),
        critic=RslRlModelCfg(
            hidden_dims=(512, 256, 128),
            activation="elu",
            obs_normalization=True,
        ),
        algorithm=RslRlPpoAlgorithmCfg(
            optimizer="muon",
            value_loss_coef=1.0,
            use_clipped_value_loss=True,
            clip_param=0.2,
            # 0.005 let the policy std drift up late in runs (s5cdzms7, 0j0flpxj); 0.001 fixed it in
            # the 10-19 full-BEAT2 runs (wbitlbqw, 1de2pner), where it was passed on the command line.
            entropy_coef=0.001,
            num_learning_epochs=5,
            num_mini_batches=4,
            learning_rate=1.0e-3,
            schedule="adaptive",
            gamma=0.99,
            lam=0.95,
            desired_kl=0.01,
            max_grad_norm=1.0,
        ),
        experiment_name="k1_tracking",
        save_interval=500,
        num_steps_per_env=24,
        max_iterations=30_000,
    )
