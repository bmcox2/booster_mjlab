# Standard live test: conversation script

Say the same lines every time, so runs can be compared (speech latency, turn-taking, gestures).
About 3 minutes. Run it with `tools/live_test.sh`, then watch the video it prints.

Speak normally, then stop and wait for the reply before the next line. *Italics* are instructions.

| # | Say | What it tests |
|---|---|---|
| 1 | "Hi, can you hear me okay?" | Greeting; a short, friendly reply |
| 2 | "What's your name?" | Very short reply: gestures should stay small |
| 3 | "Can you explain how a robot keeps its balance?" | A longer explanation: beat gestures over several sentences |
| 4 | "So I was thinking... *(pause 1 s)* ...about getting a dog." | Pause mid-sentence: should **not** cut you off |
| 5 | "Tell me a joke." | Setup and punch line: emphasis on the punch line |
| 6 | "Guess what, I got an A on my robotics exam!" | Excitement in, excitement out (later: a reaction) |
| 7 | "What should I wear to a job interview?" | A list of things (later: context gestures) |
| 8 | "Where would you put a couch in a small room?" | Spatial words (later: pointing) |
| 9 | "Yes." | One-word turn: end-of-turn on very short input |
| 10 | "Okay, thanks. Talk to you later." | Goodbye; ends in listening idle |

**After the run, note:**
- Cut-offs (it answered while you were still talking): which line?
- Long waits before a reply: which line?
- Gestures in the video: natural, too big, too still, wrong moment?
- Anything odd in the voice or the reply text.

Write them in `notes/log.md` under the date, with the session folder name.
