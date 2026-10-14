---
description: Add a dated entry to notes/log.md for this work session and update CLAUDE.md status
---

Help me log this work session.

1. Read `notes/log.md` to match its existing format, and read the Status section of `CLAUDE.md`.
2. Ask me (briefly, in one message) for anything you can't infer: what I ran (task, num-envs, iterations/time), WandB run ID(s), what the graphs showed, how it looked in `play`, problems hit and how I fixed them, and what's next. Use anything I've already said in this conversation or in $ARGUMENTS instead of asking again.
3. Append a new entry headed `## YYYY-MM-DD: <short title>` using today's date, with subsections only where there's content (Setup / Runs / Results / Problems & fixes / Takeaways). Include exact commands and run IDs. Keep it factual and concise. Don't invent results.
4. Update the `## Next` section at the bottom of `notes/log.md`.
5. If my project stage changed, update the `## Status` section of `CLAUDE.md` to match (one or two lines).
6. Show me the diff, then suggest the git commands to commit and push to `gesture-tracking`. Don't push without my OK.
