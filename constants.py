"""Constants to be used across the entire program."""

from time import sleep

# Configurable items:
AMMT_PLAYERS: int = 4
DEAL_AMMT: int = 15
DOUBLE_TWELVES_VALUE: int = 12
AMMT_BRANCHES: int = 8
SLEEP_TIME = 1

MAX_CURSOR_LINE_LEN = 10

# Text colors:
TEXT_COLOR_GREY = '\u001b[30;1m'
TEXT_COLOR_RED = '\u001b[31;1m'
TEXT_COLOR_GREEN = '\u001b[32;1m'
TEXT_COLOR_YELLOW = '\u001b[33;1m'
TEXT_COLOR_BLUE = '\u001b[34;1m'
TEXT_COLOR_MAGENTA = '\u001b[35;1m'
TEXT_COLOR_CYAN = '\u001b[36;1m'
TEXT_COLOR_WHITE = '\u001b[37;1m'

TEXT_COLOR_ORANGE = '\u001b[38;5;208m'
TEXT_COLOR_PURPLE = '\u001b[38;5;129m'
TEXT_COLOR_BROWN = '\u001b[38;5;95m'
TEXT_COLOR_LIGHTBLUE = '\u001b[38;5;51m'
TEXT_COLOR_TURQUOIS = '\u001b[38;5;86m'

TEXT_COLOR_RESET = '\u001b[0m'

def sleeprint(msg: str, time: int = SLEEP_TIME) -> None:
    print(msg)
    sleep(time)