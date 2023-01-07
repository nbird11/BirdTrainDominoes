"""Constants to be used across the entire program."""

from time import sleep

AMMT_PLAYERS: int = 4
DEAL_AMMT: int = 15
DOUBLE_TWELVES_VALUE: int = 12
AMMT_BRANCHES: int = 8
MAX_ASCII_DOMINO_LEN = 10
SLEEP_TIME = 0

def sleeprint(msg: str, time: int = SLEEP_TIME) -> None:
    print(msg)
    sleep(time)