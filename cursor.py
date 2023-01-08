"""Prints multiple lines to the screen as one big cursor."""

import constants
from domino import Domino
from branch import Branch

# Global
_cursor_rows: list[str] = [
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    ''
]

def _add_domino(domino: Domino) -> None:
    """Adds an ascii representation of the domino to `_cursor_rows`."""

    global _cursor_rows

    four_top = '● ●●●'
    four_across = '●● ●●'
    four_btm = '●●● ●'
    three_across = '● ● ●'
    two_across = '●   ●'
    one_top = '●    '
    one_mid = '  ●  '
    one_btm = '    ●'
    blank_across = '     '

    # Add vertical domino.
    if domino.end1_pips == domino.end2_pips:
        # Top, middle, bottom rows
        _cursor_rows[0] += '╭─────╮'
        _cursor_rows[4] += '├─────┤'
        _cursor_rows[8] += '╰─────╯'

        # Domino values
        if domino.end1_pips == 12:
            _cursor_rows[1] += f'│{constants.TEXT_COLOR_CYAN}{four_top}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[2] += f'│{constants.TEXT_COLOR_CYAN}{four_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[3] += f'│{constants.TEXT_COLOR_CYAN}{four_btm}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'│{constants.TEXT_COLOR_CYAN}{four_top}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[6] += f'│{constants.TEXT_COLOR_CYAN}{four_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[7] += f'│{constants.TEXT_COLOR_CYAN}{four_btm}{constants.TEXT_COLOR_RESET}│'
        elif domino.end1_pips == 11:
            _cursor_rows[1] += f'│{constants.TEXT_COLOR_BROWN}{four_top}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[2] += f'│{constants.TEXT_COLOR_BROWN}{three_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[3] += f'│{constants.TEXT_COLOR_BROWN}{four_btm}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'│{constants.TEXT_COLOR_BROWN}{four_top}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[6] += f'│{constants.TEXT_COLOR_BROWN}{three_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[7] += f'│{constants.TEXT_COLOR_BROWN}{four_btm}{constants.TEXT_COLOR_RESET}│'
        elif domino.end1_pips == 10:
            _cursor_rows[1] += f'│{constants.TEXT_COLOR_BLUE}{four_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[2] += f'│{constants.TEXT_COLOR_BLUE}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[3] += f'│{constants.TEXT_COLOR_BLUE}{four_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'│{constants.TEXT_COLOR_BLUE}{four_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[6] += f'│{constants.TEXT_COLOR_BLUE}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[7] += f'│{constants.TEXT_COLOR_BLUE}{four_across}{constants.TEXT_COLOR_RESET}│'
        elif domino.end1_pips == 9:
            _cursor_rows[1] += f'│{constants.TEXT_COLOR_TURQUOIS}{three_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[2] += f'│{constants.TEXT_COLOR_TURQUOIS}{three_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[3] += f'│{constants.TEXT_COLOR_TURQUOIS}{three_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'│{constants.TEXT_COLOR_TURQUOIS}{three_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[6] += f'│{constants.TEXT_COLOR_TURQUOIS}{three_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[7] += f'│{constants.TEXT_COLOR_TURQUOIS}{three_across}{constants.TEXT_COLOR_RESET}│'
        elif domino.end1_pips == 8:
            _cursor_rows[1] += f'│{constants.TEXT_COLOR_YELLOW}{three_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[2] += f'│{constants.TEXT_COLOR_YELLOW}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[3] += f'│{constants.TEXT_COLOR_YELLOW}{three_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'│{constants.TEXT_COLOR_YELLOW}{three_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[6] += f'│{constants.TEXT_COLOR_YELLOW}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[7] += f'│{constants.TEXT_COLOR_YELLOW}{three_across}{constants.TEXT_COLOR_RESET}│'
        elif domino.end1_pips == 7:
            _cursor_rows[1] += f'│{constants.TEXT_COLOR_GREY}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[2] += f'│{constants.TEXT_COLOR_GREY}{three_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[3] += f'│{constants.TEXT_COLOR_GREY}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'│{constants.TEXT_COLOR_GREY}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[6] += f'│{constants.TEXT_COLOR_GREY}{three_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[7] += f'│{constants.TEXT_COLOR_GREY}{two_across}{constants.TEXT_COLOR_RESET}│'
        elif domino.end1_pips == 6:
            _cursor_rows[1] += f'│{constants.TEXT_COLOR_ORANGE}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[2] += f'│{constants.TEXT_COLOR_ORANGE}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[3] += f'│{constants.TEXT_COLOR_ORANGE}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'│{constants.TEXT_COLOR_ORANGE}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[6] += f'│{constants.TEXT_COLOR_ORANGE}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[7] += f'│{constants.TEXT_COLOR_ORANGE}{two_across}{constants.TEXT_COLOR_RESET}│'
        elif domino.end1_pips == 5:
            _cursor_rows[1] += f'│{constants.TEXT_COLOR_MAGENTA}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[2] += f'│{constants.TEXT_COLOR_MAGENTA}{one_mid}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[3] += f'│{constants.TEXT_COLOR_MAGENTA}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'│{constants.TEXT_COLOR_MAGENTA}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[6] += f'│{constants.TEXT_COLOR_MAGENTA}{one_mid}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[7] += f'│{constants.TEXT_COLOR_MAGENTA}{two_across}{constants.TEXT_COLOR_RESET}│'
        elif domino.end1_pips == 4:
            _cursor_rows[1] += f'│{constants.TEXT_COLOR_LIGHTBLUE}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[2] += f'│{constants.TEXT_COLOR_LIGHTBLUE}{blank_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[3] += f'│{constants.TEXT_COLOR_LIGHTBLUE}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'│{constants.TEXT_COLOR_LIGHTBLUE}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[6] += f'│{constants.TEXT_COLOR_LIGHTBLUE}{blank_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[7] += f'│{constants.TEXT_COLOR_LIGHTBLUE}{two_across}{constants.TEXT_COLOR_RESET}│'
        elif domino.end1_pips == 3:
            _cursor_rows[1] += f'│{constants.TEXT_COLOR_PURPLE}{one_top}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[2] += f'│{constants.TEXT_COLOR_PURPLE}{one_mid}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[3] += f'│{constants.TEXT_COLOR_PURPLE}{one_btm}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'│{constants.TEXT_COLOR_PURPLE}{one_top}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[6] += f'│{constants.TEXT_COLOR_PURPLE}{one_mid}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[7] += f'│{constants.TEXT_COLOR_PURPLE}{one_btm}{constants.TEXT_COLOR_RESET}│'
        elif domino.end1_pips == 2:
            _cursor_rows[1] += f'│{constants.TEXT_COLOR_GREEN}{one_top}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[2] += f'│{constants.TEXT_COLOR_GREEN}{blank_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[3] += f'│{constants.TEXT_COLOR_GREEN}{one_btm}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'│{constants.TEXT_COLOR_GREEN}{one_top}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[6] += f'│{constants.TEXT_COLOR_GREEN}{blank_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[7] += f'│{constants.TEXT_COLOR_GREEN}{one_btm}{constants.TEXT_COLOR_RESET}│'
        elif domino.end1_pips == 1:
            _cursor_rows[1] += f'│{constants.TEXT_COLOR_RED}{blank_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[2] += f'│{constants.TEXT_COLOR_RED}{one_mid}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[3] += f'│{constants.TEXT_COLOR_RED}{blank_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'│{constants.TEXT_COLOR_RED}{blank_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[6] += f'│{constants.TEXT_COLOR_RED}{one_mid}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[7] += f'│{constants.TEXT_COLOR_RED}{blank_across}{constants.TEXT_COLOR_RESET}│'
        elif domino.end1_pips == 0:
            _cursor_rows[1] += f'│{blank_across}│'
            _cursor_rows[2] += f'│{blank_across}│'
            _cursor_rows[3] += f'│{blank_across}│'
            _cursor_rows[5] += f'│{blank_across}│'
            _cursor_rows[6] += f'│{blank_across}│'
            _cursor_rows[7] += f'│{blank_across}│'

    # Add horizontal domino.
    else:
        # Top and bottom rows
        _cursor_rows[0] += '             '
        _cursor_rows[1] += '             '
        _cursor_rows[2] += '╭─────┬─────╮'
        _cursor_rows[6] += '╰─────┴─────╯'
        _cursor_rows[7] += '             '
        _cursor_rows[8] += '             '

        # Domino values end1
        if domino.end1_pips == 12:
            _cursor_rows[3] += f'|{constants.TEXT_COLOR_CYAN}{four_top}{constants.TEXT_COLOR_RESET}|'
            _cursor_rows[4] += f'|{constants.TEXT_COLOR_CYAN}{four_across}{constants.TEXT_COLOR_RESET}|'
            _cursor_rows[5] += f'|{constants.TEXT_COLOR_CYAN}{four_btm}{constants.TEXT_COLOR_RESET}|'
        elif domino.end1_pips == 11:
            _cursor_rows[3] += f'│{constants.TEXT_COLOR_BROWN}{four_top}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[4] += f'│{constants.TEXT_COLOR_BROWN}{three_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'│{constants.TEXT_COLOR_BROWN}{four_btm}{constants.TEXT_COLOR_RESET}│'
        elif domino.end1_pips == 10:
            _cursor_rows[3] += f'│{constants.TEXT_COLOR_BLUE}{four_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[4] += f'│{constants.TEXT_COLOR_BLUE}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'│{constants.TEXT_COLOR_BLUE}{four_across}{constants.TEXT_COLOR_RESET}│'
        elif domino.end1_pips == 9:
            _cursor_rows[3] += f'│{constants.TEXT_COLOR_TURQUOIS}{three_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[4] += f'│{constants.TEXT_COLOR_TURQUOIS}{three_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'│{constants.TEXT_COLOR_TURQUOIS}{three_across}{constants.TEXT_COLOR_RESET}│'
        elif domino.end1_pips == 8:
            _cursor_rows[3] += f'│{constants.TEXT_COLOR_YELLOW}{three_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[4] += f'│{constants.TEXT_COLOR_YELLOW}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'│{constants.TEXT_COLOR_YELLOW}{three_across}{constants.TEXT_COLOR_RESET}│'
        elif domino.end1_pips == 7:
            _cursor_rows[3] += f'│{constants.TEXT_COLOR_GREY}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[4] += f'│{constants.TEXT_COLOR_GREY}{three_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'│{constants.TEXT_COLOR_GREY}{two_across}{constants.TEXT_COLOR_RESET}│'
        elif domino.end1_pips == 6:
            _cursor_rows[3] += f'│{constants.TEXT_COLOR_ORANGE}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[4] += f'│{constants.TEXT_COLOR_ORANGE}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'│{constants.TEXT_COLOR_ORANGE}{two_across}{constants.TEXT_COLOR_RESET}│'
        elif domino.end1_pips == 5:
            _cursor_rows[3] += f'│{constants.TEXT_COLOR_MAGENTA}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[4] += f'│{constants.TEXT_COLOR_MAGENTA}{one_mid}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'│{constants.TEXT_COLOR_MAGENTA}{two_across}{constants.TEXT_COLOR_RESET}│'
        elif domino.end1_pips == 4:
            _cursor_rows[3] += f'│{constants.TEXT_COLOR_LIGHTBLUE}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[4] += f'│{constants.TEXT_COLOR_LIGHTBLUE}{blank_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'│{constants.TEXT_COLOR_LIGHTBLUE}{two_across}{constants.TEXT_COLOR_RESET}│'
        elif domino.end1_pips == 3:
            _cursor_rows[3] += f'│{constants.TEXT_COLOR_PURPLE}{one_top}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[4] += f'│{constants.TEXT_COLOR_PURPLE}{one_mid}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'│{constants.TEXT_COLOR_PURPLE}{one_btm}{constants.TEXT_COLOR_RESET}│'
        elif domino.end1_pips == 2:
            _cursor_rows[3] += f'│{constants.TEXT_COLOR_GREEN}{one_top}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[4] += f'│{constants.TEXT_COLOR_GREEN}{blank_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'│{constants.TEXT_COLOR_GREEN}{one_btm}{constants.TEXT_COLOR_RESET}│'
        elif domino.end1_pips == 1:
            _cursor_rows[3] += f'│{constants.TEXT_COLOR_RED}{blank_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[4] += f'│{constants.TEXT_COLOR_RED}{one_mid}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'│{constants.TEXT_COLOR_RED}{blank_across}{constants.TEXT_COLOR_RESET}│'
        elif domino.end1_pips == 0:
            _cursor_rows[3] += f'│{blank_across}│'
            _cursor_rows[4] += f'│{blank_across}│'
            _cursor_rows[5] += f'│{blank_across}│'

        # Domino values end2
        if domino.end2_pips == 12:
            _cursor_rows[3] += f'{constants.TEXT_COLOR_CYAN}{four_top}{constants.TEXT_COLOR_RESET}|'
            _cursor_rows[4] += f'{constants.TEXT_COLOR_CYAN}{four_across}{constants.TEXT_COLOR_RESET}|'
            _cursor_rows[5] += f'{constants.TEXT_COLOR_CYAN}{four_btm}{constants.TEXT_COLOR_RESET}|'
        elif domino.end2_pips == 11:
            _cursor_rows[3] += f'{constants.TEXT_COLOR_BROWN}{four_top}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[4] += f'{constants.TEXT_COLOR_BROWN}{three_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'{constants.TEXT_COLOR_BROWN}{four_btm}{constants.TEXT_COLOR_RESET}│'
        elif domino.end2_pips == 10:
            _cursor_rows[3] += f'{constants.TEXT_COLOR_BLUE}{four_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[4] += f'{constants.TEXT_COLOR_BLUE}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'{constants.TEXT_COLOR_BLUE}{four_across}{constants.TEXT_COLOR_RESET}│'
        elif domino.end2_pips == 9:
            _cursor_rows[3] += f'{constants.TEXT_COLOR_TURQUOIS}{three_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[4] += f'{constants.TEXT_COLOR_TURQUOIS}{three_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'{constants.TEXT_COLOR_TURQUOIS}{three_across}{constants.TEXT_COLOR_RESET}│'
        elif domino.end2_pips == 8:
            _cursor_rows[3] += f'{constants.TEXT_COLOR_YELLOW}{three_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[4] += f'{constants.TEXT_COLOR_YELLOW}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'{constants.TEXT_COLOR_YELLOW}{three_across}{constants.TEXT_COLOR_RESET}│'
        elif domino.end2_pips == 7:
            _cursor_rows[3] += f'{constants.TEXT_COLOR_GREY}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[4] += f'{constants.TEXT_COLOR_GREY}{three_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'{constants.TEXT_COLOR_GREY}{two_across}{constants.TEXT_COLOR_RESET}│'
        elif domino.end2_pips == 6:
            _cursor_rows[3] += f'{constants.TEXT_COLOR_ORANGE}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[4] += f'{constants.TEXT_COLOR_ORANGE}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'{constants.TEXT_COLOR_ORANGE}{two_across}{constants.TEXT_COLOR_RESET}│'
        elif domino.end2_pips == 5:
            _cursor_rows[3] += f'{constants.TEXT_COLOR_MAGENTA}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[4] += f'{constants.TEXT_COLOR_MAGENTA}{one_mid}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'{constants.TEXT_COLOR_MAGENTA}{two_across}{constants.TEXT_COLOR_RESET}│'
        elif domino.end2_pips == 4:
            _cursor_rows[3] += f'{constants.TEXT_COLOR_LIGHTBLUE}{two_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[4] += f'{constants.TEXT_COLOR_LIGHTBLUE}{blank_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'{constants.TEXT_COLOR_LIGHTBLUE}{two_across}{constants.TEXT_COLOR_RESET}│'
        elif domino.end2_pips == 3:
            _cursor_rows[3] += f'{constants.TEXT_COLOR_PURPLE}{one_top}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[4] += f'{constants.TEXT_COLOR_PURPLE}{one_mid}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'{constants.TEXT_COLOR_PURPLE}{one_btm}{constants.TEXT_COLOR_RESET}│'
        elif domino.end2_pips == 2:
            _cursor_rows[3] += f'{constants.TEXT_COLOR_GREEN}{one_top}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[4] += f'{constants.TEXT_COLOR_GREEN}{blank_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'{constants.TEXT_COLOR_GREEN}{one_btm}{constants.TEXT_COLOR_RESET}│'
        elif domino.end2_pips == 1:
            _cursor_rows[3] += f'{constants.TEXT_COLOR_RED}{blank_across}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[4] += f'{constants.TEXT_COLOR_RED}{one_mid}{constants.TEXT_COLOR_RESET}│'
            _cursor_rows[5] += f'{constants.TEXT_COLOR_RED}{blank_across}{constants.TEXT_COLOR_RESET}│'
        elif domino.end2_pips == 0:
            _cursor_rows[3] += f'{blank_across}│'
            _cursor_rows[4] += f'{blank_across}│'
            _cursor_rows[5] += f'{blank_across}│'


def _add_train(id: str) -> None:
    """Adds an ascii representation of a train to `_cursor_rows` to signify that you can't
    play on that branch.
    """
    global _cursor_rows

    assert len(id) == 3, "ID needs to be exactly three characters long."

    _cursor_rows[0] += "                 "
    _cursor_rows[1] += "    -  - ----.   "
    _cursor_rows[2] += " - - -----,   )  "
    _cursor_rows[3] += "  ___  %s ╲_╱   " % id
    _cursor_rows[4] += "_[  o'──^───U──╮ "
    _cursor_rows[5] += "│_'------------┤ "
    _cursor_rows[6] += " (○)(○)──(○)(○)_╲"
    _cursor_rows[7] += "                 "
    _cursor_rows[8] += "                 "


def _add_id(id: str) -> None:
    """Adds an ascii representation of a train to `_cursor_rows` to signify that you can't
    play on that branch.
    """
    global _cursor_rows

    assert len(id) == 3, "ID need to be exactly three characters long."

    _cursor_rows[0] += "             "
    _cursor_rows[1] += "             "
    _cursor_rows[2] += "             "
    _cursor_rows[3] += "             "
    _cursor_rows[4] += "     %s     " % id
    _cursor_rows[5] += "             "
    _cursor_rows[6] += "             "
    _cursor_rows[7] += "             "
    _cursor_rows[8] += "             "


def _draw() -> None:
    """Draws what is stored in `_cursor_rows` then resets the cursor."""
    global _cursor_rows

    for row in _cursor_rows:
        print(row)

    # Reset cursor
    _cursor_rows = [
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        ''
    ]


def draw_domino(domino: Domino) -> None:
    """Draws a single domino on one line."""
    _add_domino(domino)
    _draw()


def draw_branch(branch: Branch) -> None:
    """Draws a single train or line of dominoes to the screen."""
    train = branch.train
    if len(train) > constants.MAX_CURSOR_LINE_LEN:
        for domino in train[len(train)-constants.MAX_CURSOR_LINE_LEN:len(train)]:
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

    if len(dominos) > constants.MAX_CURSOR_LINE_LEN:
        first_half: list[Domino] = [domino for domino in dominos[:int(len(dominos)/2)]]
        second_half: list[Domino] = [domino for domino in dominos[int(len(dominos)/2):]]

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