---
description: Add a dated entry to notes/log.md for this work session and update CLAUDE.md
---

Help me log this work session.

1. Read the **last ~150 lines** of `notes/log.md` (the newest entries and the `## Next` section) to match the format. Don't read the whole file; October is in `notes/archive/log_2026-10.md`.
2. Ask me (briefly, in one message) for anything you can't infer: what I ran (task, num-envs, iterations/time), WandB run ID(s), what the graphs showed, how it looked in `play` / sim2sim / on the robot, problems hit and how I fixed them, and what's next. Use anything I've already said in this conversation or in $ARGUMENTS instead of asking again.
3. Insert a new entry headed `## YYYY-MM-DD: <short title>` (today's date) **above `## Next`**, with subsections only where there's content (Setup / Runs / Results / Problems & fixes / Takeaways). Include exact commands and run IDs. Keep it factual and concise. Don't invent results.
4. Update `## Next`: remove items that are done (they now live in the entry), add new ones. Keep it a to-do list, not a diary.
5. Update `CLAUDE.md` only where the current state changed: "Current focus", "What to use now" (new best run, dataset, voice...), and one line under "Milestones" for a real milestone. Replace outdated facts instead of appending history.
6. Show me the diff, then suggest the git commands to commit and push to `gesture-tracking`. Don't push without my OK.
