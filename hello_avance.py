
import string
from collections import Counter
from pathlib import Path

stats = Counter()
table = str.maketrans(string.punctuation, len(string.punctuation) * " ")
text = Path("song.txt").read_text(encoding="utf8")
line = str.translate(text.casefold().strip(), table)
stats.update(line.split())

for word, score in stats.most_common(5):
    print(word, ":", score)