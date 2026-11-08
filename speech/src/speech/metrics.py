"""Word error rate (WER): how different a transcript is from the correct text.

WER = (words substituted + words deleted + words inserted) / words in the correct text.
0% = perfect; 10% = about one word in ten wrong. Before comparing, both texts are lowercased,
punctuation is removed, and filler sounds (um, uh) are dropped, since Whisper keeps or drops
those somewhat randomly and they don't change the meaning.
"""

import re

FILLERS = {"um", "uh", "umm", "uhh", "erm", "hmm", "mm"}
# Whisper writes small numbers either way ("two" / "2"); count both as the same word.
NUMBER_WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
                "eighteen", "nineteen", "twenty"]
DIGITS = {str(i): word for i, word in enumerate(NUMBER_WORDS)}


def words(text: str) -> list[str]:
    text = text.lower().replace("-", " ")
    return [DIGITS.get(w, w) for w in re.sub(r"[^a-z0-9' ]", " ", text).split() if w not in FILLERS]


def word_error_rate(reference: str, hypothesis: str) -> float:
    r, h = words(reference), words(hypothesis)
    # Edit distance over words (dynamic programming, one row at a time).
    row = list(range(len(h) + 1))
    for i in range(1, len(r) + 1):
        diagonal, row[0] = row[0], i
        for j in range(1, len(h) + 1):
            diagonal, row[j] = row[j], min(row[j] + 1,          # word deleted
                                           row[j - 1] + 1,      # word inserted
                                           diagonal + (r[i - 1] != h[j - 1]))  # substituted?
    return row[len(h)] / max(len(r), 1)
