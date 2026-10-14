---
description: Read my WandB training charts and say whether to keep training, stop, or change something
---

Analyze a training run for me. I'm new to RL, so explain plainly.

Input: $ARGUMENTS (screenshots, pasted numbers, a run ID, and/or the task name). If I haven't said which task (velocity vs tracking), how many envs, and roughly how long it's run, ask in one short message.

1. Read `notes/wandb-guide.md` and use it as the checklist.
2. Go tier by tier: is it learning (reward, episode length) → how it fails (terminations) → task quality (task errors, reward terms, style) → health (mean_std/entropy, losses). Quote the actual values/trends you see.
3. Point out anything that looks alarming but is normal (curriculum steps, penalties growing with longer episodes, noise).
4. Give a verdict: **keep training**, **done**, **stuck**, or **broken**, with the reason in one or two sentences.
5. Say exactly what to check in `play` to confirm, and the command (`uv run play <TASK> --wandb-run-path bmcox2-university-of-illinois-urbana-champaign/mjlab/<run-id>`).
6. If stuck or broken, give the next thing to try (new seed first, then config changes) and which config file it lives in.
7. End with 3–5 bullet lines I can paste into `notes/log.md`.
