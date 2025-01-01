"""Constants to be used across the entire program."""

from time import sleep

# Configurable items:
AMMT_PLAYERS: int = 4
DEAL_AMMT: int = 15
DOUBLE_TWELVES_VALUE: int = 12
AMMT_BRANCHES: int = 8
SLEEP_TIME = 1

MAX_CURSOR_LINE_LEN = 6

# Text colors:
GREY = "\u001b[30;1m"
RED = "\u001b[31;1m"
GREEN = "\u001b[32;1m"
YELLOW = "\u001b[33;1m"
BLUE = "\u001b[34;1m"
MAGENTA = "\u001b[35;1m"
CYAN = "\u001b[36;1m"
WHITE = "\u001b[37;1m"

ORANGE = "\u001b[38;5;208m"
PURPLE = "\u001b[38;5;129m"
BROWN = "\u001b[38;5;95m"
LIGHTBLUE = "\u001b[38;5;51m"
TURQUOIS = "\u001b[38;5;86m"

COLOR_RESET = "\u001b[0m"


def sleeprint(msg: str, time: int = SLEEP_TIME) -> None:
    """Prints a message then time.sleeps"""
    print(msg)
    sleep(time)
