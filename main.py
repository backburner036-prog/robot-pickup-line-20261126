"""Entry for make.fun bounty "The Robot Pickup Line Championship".

One line, 137 characters, a robot's pickup line built on the judge
brief's recipe — robot first, machine-grown joke, surprise, economy,
charm:

  1. Robot pickup line, first person: "I" is the robot, speaking to
     someone it wants to charm, not a human line with a beep pasted on.
  2. Machine-grown joke: a warranty is a machine thing — a promise
     written into the hardware's service contract. The joke grows out
     of being a product with a warranty, a build date and a designed
     lifespan, not out of generic tech jargon.
  3. Surprise twist: the warranty "covers everything except this" —
     the exception is not a defect or an exclusion clause, it is the
     robot already choosing how to spend its whole fifty-year life.
     The punchline lands on the last words, "standing next to you".
  4. Economy: 137 characters, one sentence, no padding — every word
     earns its place, and deleting any clause breaks the joke.
  5. Charm: warm and confident, not creepy — a robot that knows
     exactly how long it will last and spends that certainty on one
     person, standing beside them.

Delete the warranty frame and the line is just a human compliment;
delete the last clause and there is no joke. 137 characters, under
the 200 cap.
"""

from pathlib import Path

# Premis garansi: janji servis mesin jadi bingkai lelucon — pengecualiannya bukan cacat, tapi pilihan robot.
# Batas 200 karakter: entri 137 karakter, satu kalimat, tanpa padding — di bawah cap bounty.
TEXT = "My warranty covers everything except this: I was built to last fifty years, and I already want to spend all of them standing next to you."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=200):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    assert text.strip(), "entry must not be whitespace only"
    return size


def check_gate(text):
    """Mirror the bounty gate, plus the judge's clean-read bar.

    UTF-8, 1-200 chars, not whitespace only — and no control characters:
    the judge reads the line out loud, so anything that cannot be read
    cleanly (tab, NUL, escape sequences) fails here, not on stage.
    """
    text.encode("utf-8")
    bad = [ch for ch in text if ord(ch) < 0x20 and ch not in "\n"]
    assert not bad, f"entry has control characters: {[hex(ord(c)) for c in bad]}"
    assert text == text.strip(), "entry must not start/end with whitespace"
    return check_len(text)


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_gate(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
