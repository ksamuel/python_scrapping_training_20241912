import logging
import logging.config
import string
import sys
from collections import Counter
from pathlib import Path

old_hook = sys.excepthook


def quand_mon_prog_crash(exc_type, exc_value, exc_tb):
    old_hook(exc_type, exc_value, exc_tb)
    log.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_tb))


sys.excepthook = quand_mon_prog_crash

logging.config.dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        },
        "handlers": {
            "file": {
                "class": "logging.FileHandler",
                "filename": "app.log",
                "formatter": "default",
                "level": "DEBUG",
            },
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
                "level": "INFO",
            },
        },
        "root": {"handlers": ["file", "console"], "level": "DEBUG"},
    }
)


log = logging.getLogger(__name__)

log.info("coucou")
log.debug("heyy")
log.warning("hey")


1 / 0


stats = Counter()
table = str.maketrans(string.punctuation, len(string.punctuation) * " ")
text = Path("song.txt").read_text(encoding="utf8")
line = str.translate(text.casefold().strip(), table)
stats.update(line.split())

for word, score in stats.most_common(5):
    print(word, ":", score)
