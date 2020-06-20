import time
import logging
from .core.parse import try_parse

# Logging config
# ----------------------------------------------------------------------
DEBUGGING = True
UNIQUE_FILE = False

_filename = "debug.log"
if UNIQUE_FILE:
    _filename = f"{str(int(time.time() * 10000))}_" + _filename

if DEBUGGING:
    logging.basicConfig(
        filename=_filename, level=logging.DEBUG,
    )
else:
    logging.basicConfig(
        filename=_filename, level=logging.WARNING,
    )

# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    a = try_parse(r"(a/b)\c")
    b = try_parse(r"(a\b/c)/(a\b)")
    c = try_parse(r"(a/b)*b*c")
    d = try_parse(r"(a/b)*b*(c)")
