# Preparing Motions for Tracking

booster_mjlab uses WandB to manage motion datasets for the `Mjlab-Tracking-*` tasks.
Clips can come from [GMR](https://github.com/YanjieZe/GMR/) (`.pkl`, the format produced when retargeting
[GVHMR](https://github.com/zju3dv/GVHMR) video reconstructions) or from
[BeyondMimic](https://github.com/HybridRobotics/whole_body_tracking) (`.csv`).

Set your WandB entity first:

```bash
export WANDB_ENTITY=your-organization-name
```

## GMR motions

### Ground the clips first

GMR's K1 model differs slightly from the one used for training (the legs sit 1.5 cm lower here), so
retargeted K1 clips come out with the feet ~6–7 cm below the floor. Fix every clip in a folder with:

```bash
uv run python tools/ground_clip.py ~/robotics/data/k1_motions            # writes <name>_grounded.pkl
uv run python tools/ground_clip.py ~/robotics/data/k1_motions --upload   # ...and uploads each one
```

The script runs forward kinematics on `k1.xml` and measures each clip's own offset, so the lowest collision
point touches the floor. Re-running it only processes new or changed clips (`--force` redoes all). With
`--upload`, the artifact is named after the original clip (`<name>-tracking`), so re-uploading a fixed clip
adds a new version instead of a new artifact. Upload the `_grounded.pkl` files, never the raw ones.

### Upload

`upload-motion` converts a `.pkl` clip to the tracking format and uploads it to WandB in one step:

```bash
uv run upload-motion --input-file /path/to/motion.pkl --entity your-org
```

The motion is uploaded as an artifact named `<file-stem>-tracking` to the `motion_upload` project
(override with `--project` and `--artifact-name`). The command prints the artifact's full name, e.g.
`your-org/motion_upload/motion-tracking:v0`, which you pass as `--registry-name` when training.

## BeyondMimic motions

First create a registry collection in your WandB workspace named `motions`, then run:

```bash
MUJOCO_GL=egl uv run python -m booster_mjlab.scripts.csv_to_npz \
    --input-file /path/to/motion.csv \
    --output-name motion_name \
    --input-fps 30 \
    --output-fps 50 \
    --render
```

This uploads the motion to the `motions` registry as `your-org/motions/motion_name`, which you pass as
`--registry-name` when training.

## Next steps

See the [Motion Imitation](../README.md#2-motion-imitation) section of the README for training and evaluation
commands, and use `uv run visualize-motions` to inspect clips before training on them.
