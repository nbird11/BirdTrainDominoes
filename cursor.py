"""Prints multiple lines to the screen as one big cursor."""

import constants as c
from domino import Domino
from branch import Branch

# Global
_cursor_rows: list[str] = ["", "", "", "", "", "", "", "", ""]


def _add_domino(domino: Domino) -> None:
    """Adds an ascii representation of the domino to `_cursor_rows`."""

    global _cursor_rows

    four_top = "● ●●●"
    four_across = "●● ●●"
    four_btm = "●●● ●"
    three_across = "● ● ●"
    two_across = "●   ●"
    one_top = "●    "
    one_mid = "  ●  "
    one_btm = "    ●"
    blank_across = "     "

    # Add vertical domino.
    if domino.end1_pips == domino.end2_pips:
        # Top, middle, bottom rows
        _cursor_rows[0] += "╭─────╮"
        _cursor_rows[4] += "├─────┤"
        _cursor_rows[8] += "╰─────╯"

        # Domino values
        if domino.end1_pips == 12:
            _cursor_rows[1] += f"│{c.CYAN}{four_top}{c.COLOR_RESET}│"
            _cursor_rows[2] += f"│{c.CYAN}{four_across}{c.COLOR_RESET}│"
            _cursor_rows[3] += f"│{c.CYAN}{four_btm}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"│{c.CYAN}{four_top}{c.COLOR_RESET}│"
            _cursor_rows[6] += f"│{c.CYAN}{four_across}{c.COLOR_RESET}│"
            _cursor_rows[7] += f"│{c.CYAN}{four_btm}{c.COLOR_RESET}│"
        elif domino.end1_pips == 11:
            _cursor_rows[1] += f"│{c.BROWN}{four_top}{c.COLOR_RESET}│"
            _cursor_rows[2] += f"│{c.BROWN}{three_across}{c.COLOR_RESET}│"
            _cursor_rows[3] += f"│{c.BROWN}{four_btm}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"│{c.BROWN}{four_top}{c.COLOR_RESET}│"
            _cursor_rows[6] += f"│{c.BROWN}{three_across}{c.COLOR_RESET}│"
            _cursor_rows[7] += f"│{c.BROWN}{four_btm}{c.COLOR_RESET}│"
        elif domino.end1_pips == 10:
            _cursor_rows[1] += f"│{c.BLUE}{four_across}{c.COLOR_RESET}│"
            _cursor_rows[2] += f"│{c.BLUE}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[3] += f"│{c.BLUE}{four_across}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"│{c.BLUE}{four_across}{c.COLOR_RESET}│"
            _cursor_rows[6] += f"│{c.BLUE}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[7] += f"│{c.BLUE}{four_across}{c.COLOR_RESET}│"
        elif domino.end1_pips == 9:
            _cursor_rows[1] += f"│{c.TURQUOIS}{three_across}{c.COLOR_RESET}│"
            _cursor_rows[2] += f"│{c.TURQUOIS}{three_across}{c.COLOR_RESET}│"
            _cursor_rows[3] += f"│{c.TURQUOIS}{three_across}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"│{c.TURQUOIS}{three_across}{c.COLOR_RESET}│"
            _cursor_rows[6] += f"│{c.TURQUOIS}{three_across}{c.COLOR_RESET}│"
            _cursor_rows[7] += f"│{c.TURQUOIS}{three_across}{c.COLOR_RESET}│"
        elif domino.end1_pips == 8:
            _cursor_rows[1] += f"│{c.YELLOW}{three_across}{c.COLOR_RESET}│"
            _cursor_rows[2] += f"│{c.YELLOW}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[3] += f"│{c.YELLOW}{three_across}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"│{c.YELLOW}{three_across}{c.COLOR_RESET}│"
            _cursor_rows[6] += f"│{c.YELLOW}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[7] += f"│{c.YELLOW}{three_across}{c.COLOR_RESET}│"
        elif domino.end1_pips == 7:
            _cursor_rows[1] += f"│{c.GREY}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[2] += f"│{c.GREY}{three_across}{c.COLOR_RESET}│"
            _cursor_rows[3] += f"│{c.GREY}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"│{c.GREY}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[6] += f"│{c.GREY}{three_across}{c.COLOR_RESET}│"
            _cursor_rows[7] += f"│{c.GREY}{two_across}{c.COLOR_RESET}│"
        elif domino.end1_pips == 6:
            _cursor_rows[1] += f"│{c.ORANGE}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[2] += f"│{c.ORANGE}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[3] += f"│{c.ORANGE}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"│{c.ORANGE}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[6] += f"│{c.ORANGE}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[7] += f"│{c.ORANGE}{two_across}{c.COLOR_RESET}│"
        elif domino.end1_pips == 5:
            _cursor_rows[1] += f"│{c.MAGENTA}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[2] += f"│{c.MAGENTA}{one_mid}{c.COLOR_RESET}│"
            _cursor_rows[3] += f"│{c.MAGENTA}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"│{c.MAGENTA}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[6] += f"│{c.MAGENTA}{one_mid}{c.COLOR_RESET}│"
            _cursor_rows[7] += f"│{c.MAGENTA}{two_across}{c.COLOR_RESET}│"
        elif domino.end1_pips == 4:
            _cursor_rows[1] += f"│{c.LIGHTBLUE}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[2] += f"│{c.LIGHTBLUE}{blank_across}{c.COLOR_RESET}│"
            _cursor_rows[3] += f"│{c.LIGHTBLUE}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"│{c.LIGHTBLUE}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[6] += f"│{c.LIGHTBLUE}{blank_across}{c.COLOR_RESET}│"
            _cursor_rows[7] += f"│{c.LIGHTBLUE}{two_across}{c.COLOR_RESET}│"
        elif domino.end1_pips == 3:
            _cursor_rows[1] += f"│{c.PURPLE}{one_top}{c.COLOR_RESET}│"
            _cursor_rows[2] += f"│{c.PURPLE}{one_mid}{c.COLOR_RESET}│"
            _cursor_rows[3] += f"│{c.PURPLE}{one_btm}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"│{c.PURPLE}{one_top}{c.COLOR_RESET}│"
            _cursor_rows[6] += f"│{c.PURPLE}{one_mid}{c.COLOR_RESET}│"
            _cursor_rows[7] += f"│{c.PURPLE}{one_btm}{c.COLOR_RESET}│"
        elif domino.end1_pips == 2:
            _cursor_rows[1] += f"│{c.GREEN}{one_top}{c.COLOR_RESET}│"
            _cursor_rows[2] += f"│{c.GREEN}{blank_across}{c.COLOR_RESET}│"
            _cursor_rows[3] += f"│{c.GREEN}{one_btm}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"│{c.GREEN}{one_top}{c.COLOR_RESET}│"
            _cursor_rows[6] += f"│{c.GREEN}{blank_across}{c.COLOR_RESET}│"
            _cursor_rows[7] += f"│{c.GREEN}{one_btm}{c.COLOR_RESET}│"
        elif domino.end1_pips == 1:
            _cursor_rows[1] += f"│{c.RED}{blank_across}{c.COLOR_RESET}│"
            _cursor_rows[2] += f"│{c.RED}{one_mid}{c.COLOR_RESET}│"
            _cursor_rows[3] += f"│{c.RED}{blank_across}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"│{c.RED}{blank_across}{c.COLOR_RESET}│"
            _cursor_rows[6] += f"│{c.RED}{one_mid}{c.COLOR_RESET}│"
            _cursor_rows[7] += f"│{c.RED}{blank_across}{c.COLOR_RESET}│"
        elif domino.end1_pips == 0:
            _cursor_rows[1] += f"│{blank_across}│"
            _cursor_rows[2] += f"│{blank_across}│"
            _cursor_rows[3] += f"│{blank_across}│"
            _cursor_rows[5] += f"│{blank_across}│"
            _cursor_rows[6] += f"│{blank_across}│"
            _cursor_rows[7] += f"│{blank_across}│"

    # Add horizontal domino.
    else:
        # Top and bottom rows
        _cursor_rows[0] += "             "
        _cursor_rows[1] += "             "
        _cursor_rows[2] += "╭─────┬─────╮"
        _cursor_rows[6] += "╰─────┴─────╯"
        _cursor_rows[7] += "             "
        _cursor_rows[8] += "             "

        # Domino values end1
        if domino.end1_pips == 12:
            _cursor_rows[3] += f"|{c.CYAN}{four_top}{c.COLOR_RESET}|"
            _cursor_rows[4] += f"|{c.CYAN}{four_across}{c.COLOR_RESET}|"
            _cursor_rows[5] += f"|{c.CYAN}{four_btm}{c.COLOR_RESET}|"
        elif domino.end1_pips == 11:
            _cursor_rows[3] += f"│{c.BROWN}{four_top}{c.COLOR_RESET}│"
            _cursor_rows[4] += f"│{c.BROWN}{three_across}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"│{c.BROWN}{four_btm}{c.COLOR_RESET}│"
        elif domino.end1_pips == 10:
            _cursor_rows[3] += f"│{c.BLUE}{four_across}{c.COLOR_RESET}│"
            _cursor_rows[4] += f"│{c.BLUE}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"│{c.BLUE}{four_across}{c.COLOR_RESET}│"
        elif domino.end1_pips == 9:
            _cursor_rows[3] += f"│{c.TURQUOIS}{three_across}{c.COLOR_RESET}│"
            _cursor_rows[4] += f"│{c.TURQUOIS}{three_across}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"│{c.TURQUOIS}{three_across}{c.COLOR_RESET}│"
        elif domino.end1_pips == 8:
            _cursor_rows[3] += f"│{c.YELLOW}{three_across}{c.COLOR_RESET}│"
            _cursor_rows[4] += f"│{c.YELLOW}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"│{c.YELLOW}{three_across}{c.COLOR_RESET}│"
        elif domino.end1_pips == 7:
            _cursor_rows[3] += f"│{c.GREY}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[4] += f"│{c.GREY}{three_across}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"│{c.GREY}{two_across}{c.COLOR_RESET}│"
        elif domino.end1_pips == 6:
            _cursor_rows[3] += f"│{c.ORANGE}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[4] += f"│{c.ORANGE}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"│{c.ORANGE}{two_across}{c.COLOR_RESET}│"
        elif domino.end1_pips == 5:
            _cursor_rows[3] += f"│{c.MAGENTA}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[4] += f"│{c.MAGENTA}{one_mid}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"│{c.MAGENTA}{two_across}{c.COLOR_RESET}│"
        elif domino.end1_pips == 4:
            _cursor_rows[3] += f"│{c.LIGHTBLUE}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[4] += f"│{c.LIGHTBLUE}{blank_across}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"│{c.LIGHTBLUE}{two_across}{c.COLOR_RESET}│"
        elif domino.end1_pips == 3:
            _cursor_rows[3] += f"│{c.PURPLE}{one_top}{c.COLOR_RESET}│"
            _cursor_rows[4] += f"│{c.PURPLE}{one_mid}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"│{c.PURPLE}{one_btm}{c.COLOR_RESET}│"
        elif domino.end1_pips == 2:
            _cursor_rows[3] += f"│{c.GREEN}{one_top}{c.COLOR_RESET}│"
            _cursor_rows[4] += f"│{c.GREEN}{blank_across}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"│{c.GREEN}{one_btm}{c.COLOR_RESET}│"
        elif domino.end1_pips == 1:
            _cursor_rows[3] += f"│{c.RED}{blank_across}{c.COLOR_RESET}│"
            _cursor_rows[4] += f"│{c.RED}{one_mid}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"│{c.RED}{blank_across}{c.COLOR_RESET}│"
        elif domino.end1_pips == 0:
            _cursor_rows[3] += f"│{blank_across}│"
            _cursor_rows[4] += f"│{blank_across}│"
            _cursor_rows[5] += f"│{blank_across}│"

        # Domino values end2
        if domino.end2_pips == 12:
            _cursor_rows[3] += f"{c.CYAN}{four_top}{c.COLOR_RESET}|"
            _cursor_rows[4] += f"{c.CYAN}{four_across}{c.COLOR_RESET}|"
            _cursor_rows[5] += f"{c.CYAN}{four_btm}{c.COLOR_RESET}|"
        elif domino.end2_pips == 11:
            _cursor_rows[3] += f"{c.BROWN}{four_top}{c.COLOR_RESET}│"
            _cursor_rows[4] += f"{c.BROWN}{three_across}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"{c.BROWN}{four_btm}{c.COLOR_RESET}│"
        elif domino.end2_pips == 10:
            _cursor_rows[3] += f"{c.BLUE}{four_across}{c.COLOR_RESET}│"
            _cursor_rows[4] += f"{c.BLUE}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"{c.BLUE}{four_across}{c.COLOR_RESET}│"
        elif domino.end2_pips == 9:
            _cursor_rows[3] += f"{c.TURQUOIS}{three_across}{c.COLOR_RESET}│"
            _cursor_rows[4] += f"{c.TURQUOIS}{three_across}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"{c.TURQUOIS}{three_across}{c.COLOR_RESET}│"
        elif domino.end2_pips == 8:
            _cursor_rows[3] += f"{c.YELLOW}{three_across}{c.COLOR_RESET}│"
            _cursor_rows[4] += f"{c.YELLOW}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"{c.YELLOW}{three_across}{c.COLOR_RESET}│"
        elif domino.end2_pips == 7:
            _cursor_rows[3] += f"{c.GREY}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[4] += f"{c.GREY}{three_across}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"{c.GREY}{two_across}{c.COLOR_RESET}│"
        elif domino.end2_pips == 6:
            _cursor_rows[3] += f"{c.ORANGE}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[4] += f"{c.ORANGE}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"{c.ORANGE}{two_across}{c.COLOR_RESET}│"
        elif domino.end2_pips == 5:
            _cursor_rows[3] += f"{c.MAGENTA}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[4] += f"{c.MAGENTA}{one_mid}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"{c.MAGENTA}{two_across}{c.COLOR_RESET}│"
        elif domino.end2_pips == 4:
            _cursor_rows[3] += f"{c.LIGHTBLUE}{two_across}{c.COLOR_RESET}│"
            _cursor_rows[4] += f"{c.LIGHTBLUE}{blank_across}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"{c.LIGHTBLUE}{two_across}{c.COLOR_RESET}│"
        elif domino.end2_pips == 3:
            _cursor_rows[3] += f"{c.PURPLE}{one_top}{c.COLOR_RESET}│"
            _cursor_rows[4] += f"{c.PURPLE}{one_mid}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"{c.PURPLE}{one_btm}{c.COLOR_RESET}│"
        elif domino.end2_pips == 2:
            _cursor_rows[3] += f"{c.GREEN}{one_top}{c.COLOR_RESET}│"
            _cursor_rows[4] += f"{c.GREEN}{blank_across}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"{c.GREEN}{one_btm}{c.COLOR_RESET}│"
        elif domino.end2_pips == 1:
            _cursor_rows[3] += f"{c.RED}{blank_across}{c.COLOR_RESET}│"
            _cursor_rows[4] += f"{c.RED}{one_mid}{c.COLOR_RESET}│"
            _cursor_rows[5] += f"{c.RED}{blank_across}{c.COLOR_RESET}│"
        elif domino.end2_pips == 0:
            _cursor_rows[3] += f"{blank_across}│"
            _cursor_rows[4] += f"{blank_across}│"
            _cursor_rows[5] += f"{blank_across}│"


def _add_train(id: str) -> None:
    """Adds an ascii representation of a train to `_cursor_rows` to signify that you can't
    play on that branch.
    """
    global _cursor_rows

    assert len(id) == 3, "ID needs to be exactly three characters long."
    s = id
    _cursor_rows[0] +=  "                 "
    _cursor_rows[1] +=  "    -  - ----.   "
    _cursor_rows[2] +=  " - - -----,   )  "
    _cursor_rows[3] += f"  ___ {s} ╲_╱   "
    _cursor_rows[4] +=  "_[  o'──^───U──╮ "
    _cursor_rows[5] +=  "│_'------------┤ "
    _cursor_rows[6] +=  " (○)(○)──(○)(○)_╲"
    _cursor_rows[7] +=  "                 "
    _cursor_rows[8] +=  "                 "


def _add_id(id: str) -> None:
    """Adds an ascii representation of a train to `_cursor_rows` to signify that you can't
    play on that branch.
    """
    global _cursor_rows

    assert len(id) == 3, "ID need to be exactly three characters long."

    s = id
    _cursor_rows[0] += f"             "
    _cursor_rows[1] += f"             "
    _cursor_rows[2] += f"             "
    _cursor_rows[3] += f"             "
    _cursor_rows[4] += f"     {s}     "
    _cursor_rows[5] += f"             "
    _cursor_rows[6] += f"             "
    _cursor_rows[7] += f"             "
    _cursor_rows[8] += f"             "


def _draw() -> None:
    """Draws what is stored in `_cursor_rows` then resets the cursor."""
    global _cursor_rows

    for row in _cursor_rows:
        print(row)

    # Reset cursor
    _cursor_rows = ["", "", "", "", "", "", "", "", ""]


def draw_domino(domino: Domino) -> None:
    """Draws a single domino on one line."""
    _add_domino(domino)
    _draw()


def draw_branch(branch: Branch) -> None:
    """Draws a single train or line of dominoes to the screen."""
    train = branch.train
    if len(train) > c.MAX_CURSOR_LINE_LEN:
        for domino in train[len(train) - c.MAX_CURSOR_LINE_LEN : len(train)]:
            _add_domino(domino)
    else:
        for domino in train:
            _add_domino(domino)

    if branch.player:
        if branch.train_on:
            _add_train(branch.player.id)
        else:
            _add_id(branch.player.id)

    _draw()


def draw_branches(branches: list[Branch]) -> None:
    """Draws multiple trains or lines of dominoes to the screen."""
    for branch in branches:
        draw_branch(branch)


def draw_list(dominos: list[Domino]) -> None:
    """Draws a list of dominoes."""

    if len(dominos) > c.MAX_CURSOR_LINE_LEN:
        first_half: list[Domino] = [
            domino for domino in dominos[: int(len(dominos) / 2)]
        ]
        second_half: list[Domino] = [
            domino for domino in dominos[int(len(dominos) / 2) :]
        ]

        for domino in first_half:
            _add_domino(domino)
        _draw()

        for domino in second_half:
            _add_domino(domino)
        _draw()
    else:
        for domino in dominos:
            _add_domino(domino)
        _draw()
