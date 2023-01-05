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

    four_top = '○ ○○○'
    four_across = '○○ ○○'
    four_btm = '○○○ ○'
    three_across = '○ ○ ○'
    two_across = '○   ○'
    one_top = '○    '
    one_mid = '  ○  '
    one_btm = '    ○'
    blank_across = '     '

    # Add vertical domino.
    if domino.end1_pips == domino.end2_pips:
        # Top, middle, bottom rows
        _cursor_rows[0] += '╭─────╮'
        _cursor_rows[4] += '├─────┤'
        _cursor_rows[8] += '╰─────╯'

        # Domino values
        if domino.end1_pips == 12:
            _cursor_rows[1] += f'│{four_top}│'
            _cursor_rows[2] += f'│{four_across}│'
            _cursor_rows[3] += f'│{four_btm}│'
            _cursor_rows[5] += f'│{four_top}│'
            _cursor_rows[6] += f'│{four_across}│'
            _cursor_rows[7] += f'│{four_btm}│'
        elif domino.end1_pips == 11:
            _cursor_rows[1] += f'│{four_top}│'
            _cursor_rows[2] += f'│{three_across}│'
            _cursor_rows[3] += f'│{four_btm}│'
            _cursor_rows[5] += f'│{four_top}│'
            _cursor_rows[6] += f'│{three_across}│'
            _cursor_rows[7] += f'│{four_btm}│'
        elif domino.end1_pips == 10:
            _cursor_rows[1] += f'│{four_across}│'
            _cursor_rows[2] += f'│{two_across}│'
            _cursor_rows[3] += f'│{four_across}│'
            _cursor_rows[5] += f'│{four_across}│'
            _cursor_rows[6] += f'│{two_across}│'
            _cursor_rows[7] += f'│{four_across}│'
        elif domino.end1_pips == 9:
            _cursor_rows[1] += f'│{three_across}│'
            _cursor_rows[2] += f'│{three_across}│'
            _cursor_rows[3] += f'│{three_across}│'
            _cursor_rows[5] += f'│{three_across}│'
            _cursor_rows[6] += f'│{three_across}│'
            _cursor_rows[7] += f'│{three_across}│'
        elif domino.end1_pips == 8:
            _cursor_rows[1] += f'│{three_across}│'
            _cursor_rows[2] += f'│{two_across}│'
            _cursor_rows[3] += f'│{three_across}│'
            _cursor_rows[5] += f'│{three_across}│'
            _cursor_rows[6] += f'│{two_across}│'
            _cursor_rows[7] += f'│{three_across}│'
        elif domino.end1_pips == 7:
            _cursor_rows[1] += f'│{two_across}│'
            _cursor_rows[2] += f'│{three_across}│'
            _cursor_rows[3] += f'│{two_across}│'
            _cursor_rows[5] += f'│{two_across}│'
            _cursor_rows[6] += f'│{three_across}│'
            _cursor_rows[7] += f'│{two_across}│'
        elif domino.end1_pips == 6:
            _cursor_rows[1] += f'│{two_across}│'
            _cursor_rows[2] += f'│{two_across}│'
            _cursor_rows[3] += f'│{two_across}│'
            _cursor_rows[5] += f'│{two_across}│'
            _cursor_rows[6] += f'│{two_across}│'
            _cursor_rows[7] += f'│{two_across}│'
        elif domino.end1_pips == 5:
            _cursor_rows[1] += f'│{two_across}│'
            _cursor_rows[2] += f'│{one_mid}│'
            _cursor_rows[3] += f'│{two_across}│'
            _cursor_rows[5] += f'│{two_across}│'
            _cursor_rows[6] += f'│{one_mid}│'
            _cursor_rows[7] += f'│{two_across}│'
        elif domino.end1_pips == 4:
            _cursor_rows[1] += f'│{two_across}│'
            _cursor_rows[2] += f'│{blank_across}│'
            _cursor_rows[3] += f'│{two_across}│'
            _cursor_rows[5] += f'│{two_across}│'
            _cursor_rows[6] += f'│{blank_across}│'
            _cursor_rows[7] += f'│{two_across}│'
        elif domino.end1_pips == 3:
            _cursor_rows[1] += f'│{one_top}│'
            _cursor_rows[2] += f'│{one_mid}│'
            _cursor_rows[3] += f'│{one_btm}│'
            _cursor_rows[5] += f'│{one_top}│'
            _cursor_rows[6] += f'│{one_mid}│'
            _cursor_rows[7] += f'│{one_btm}│'
        elif domino.end1_pips == 2:
            _cursor_rows[1] += f'│{one_top}│'
            _cursor_rows[2] += f'│{blank_across}│'
            _cursor_rows[3] += f'│{one_btm}│'
            _cursor_rows[5] += f'│{one_top}│'
            _cursor_rows[6] += f'│{blank_across}│'
            _cursor_rows[7] += f'│{one_btm}│'
        elif domino.end1_pips == 1:
            _cursor_rows[1] += f'│{blank_across}│'
            _cursor_rows[2] += f'│{one_mid}│'
            _cursor_rows[3] += f'│{blank_across}│'
            _cursor_rows[5] += f'│{blank_across}│'
            _cursor_rows[6] += f'│{one_mid}│'
            _cursor_rows[7] += f'│{blank_across}│'
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
            _cursor_rows[3] += f'|{four_top}|'
            _cursor_rows[4] += f'|{four_across}|'
            _cursor_rows[5] += f'|{four_btm}|'
        elif domino.end1_pips == 11:
            _cursor_rows[3] += f'│{four_top}│'
            _cursor_rows[4] += f'│{three_across}│'
            _cursor_rows[5] += f'│{four_btm}│'
        elif domino.end1_pips == 10:
            _cursor_rows[3] += f'│{four_across}│'
            _cursor_rows[4] += f'│{two_across}│'
            _cursor_rows[5] += f'│{four_across}│'
        elif domino.end1_pips == 9:
            _cursor_rows[3] += f'│{three_across}│'
            _cursor_rows[4] += f'│{three_across}│'
            _cursor_rows[5] += f'│{three_across}│'
        elif domino.end1_pips == 8:
            _cursor_rows[3] += f'│{three_across}│'
            _cursor_rows[4] += f'│{two_across}│'
            _cursor_rows[5] += f'│{three_across}│'
        elif domino.end1_pips == 7:
            _cursor_rows[3] += f'│{two_across}│'
            _cursor_rows[4] += f'│{three_across}│'
            _cursor_rows[5] += f'│{two_across}│'
        elif domino.end1_pips == 6:
            _cursor_rows[3] += f'│{two_across}│'
            _cursor_rows[4] += f'│{two_across}│'
            _cursor_rows[5] += f'│{two_across}│'
        elif domino.end1_pips == 5:
            _cursor_rows[3] += f'│{two_across}│'
            _cursor_rows[4] += f'│{one_mid}│'
            _cursor_rows[5] += f'│{two_across}│'
        elif domino.end1_pips == 4:
            _cursor_rows[3] += f'│{two_across}│'
            _cursor_rows[4] += f'│{blank_across}│'
            _cursor_rows[5] += f'│{two_across}│'
        elif domino.end1_pips == 3:
            _cursor_rows[3] += f'│{one_top}│'
            _cursor_rows[4] += f'│{one_mid}│'
            _cursor_rows[5] += f'│{one_btm}│'
        elif domino.end1_pips == 2:
            _cursor_rows[3] += f'│{one_top}│'
            _cursor_rows[4] += f'│{blank_across}│'
            _cursor_rows[5] += f'│{one_btm}│'
        elif domino.end1_pips == 1:
            _cursor_rows[3] += f'│{blank_across}│'
            _cursor_rows[4] += f'│{one_mid}│'
            _cursor_rows[5] += f'│{blank_across}│'
        elif domino.end1_pips == 0:
            _cursor_rows[3] += f'│{blank_across}│'
            _cursor_rows[4] += f'│{blank_across}│'
            _cursor_rows[5] += f'│{blank_across}│'

        # Domino values end2
        if domino.end2_pips == 12:
            _cursor_rows[3] += f'{four_top}|'
            _cursor_rows[4] += f'{four_across}|'
            _cursor_rows[5] += f'{four_btm}|'
        elif domino.end2_pips == 11:
            _cursor_rows[3] += f'{four_top}│'
            _cursor_rows[4] += f'{three_across}│'
            _cursor_rows[5] += f'{four_btm}│'
        elif domino.end2_pips == 10:
            _cursor_rows[3] += f'{four_across}│'
            _cursor_rows[4] += f'{two_across}│'
            _cursor_rows[5] += f'{four_across}│'
        elif domino.end2_pips == 9:
            _cursor_rows[3] += f'{three_across}│'
            _cursor_rows[4] += f'{three_across}│'
            _cursor_rows[5] += f'{three_across}│'
        elif domino.end2_pips == 8:
            _cursor_rows[3] += f'{three_across}│'
            _cursor_rows[4] += f'{two_across}│'
            _cursor_rows[5] += f'{three_across}│'
        elif domino.end2_pips == 7:
            _cursor_rows[3] += f'{two_across}│'
            _cursor_rows[4] += f'{three_across}│'
            _cursor_rows[5] += f'{two_across}│'
        elif domino.end2_pips == 6:
            _cursor_rows[3] += f'{two_across}│'
            _cursor_rows[4] += f'{two_across}│'
            _cursor_rows[5] += f'{two_across}│'
        elif domino.end2_pips == 5:
            _cursor_rows[3] += f'{two_across}│'
            _cursor_rows[4] += f'{one_mid}│'
            _cursor_rows[5] += f'{two_across}│'
        elif domino.end2_pips == 4:
            _cursor_rows[3] += f'{two_across}│'
            _cursor_rows[4] += f'{blank_across}│'
            _cursor_rows[5] += f'{two_across}│'
        elif domino.end2_pips == 3:
            _cursor_rows[3] += f'{one_top}│'
            _cursor_rows[4] += f'{one_mid}│'
            _cursor_rows[5] += f'{one_btm}│'
        elif domino.end2_pips == 2:
            _cursor_rows[3] += f'{one_top}│'
            _cursor_rows[4] += f'{blank_across}│'
            _cursor_rows[5] += f'{one_btm}│'
        elif domino.end2_pips == 1:
            _cursor_rows[3] += f'{blank_across}│'
            _cursor_rows[4] += f'{one_mid}│'
            _cursor_rows[5] += f'{blank_across}│'
        elif domino.end2_pips == 0:
            _cursor_rows[3] += f'{blank_across}│'
            _cursor_rows[4] += f'{blank_across}│'
            _cursor_rows[5] += f'{blank_across}│'


def _add_train() -> None:
    """Adds an ascii representation of a train to `_cursor_rows` to signify that you can't
    play on that branch.
    """

    _cursor_rows[0] += '                 '
    _cursor_rows[1] += '─┬─────┬─        '
    _cursor_rows[2] += ' │ ╭─╮ │    __   '
    _cursor_rows[3] += ' │ │ │ ├┬───╲╱┐  '
    _cursor_rows[4] += ' │ ╰─╯ │       ╲ '
    _cursor_rows[5] += ' │ __  │  _  _  )'
    _cursor_rows[6] += ' └╱  ╲─┴─╱ ╲╱ ╲╱ '
    _cursor_rows[7] += '  ╲__╱   ╲_╱╲_╱  '
    _cursor_rows[8] += '                 '


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


def draw_branch(branch: Branch) -> None:
    """Draws a single train or line of dominoes to the screen."""

    global _cursor_rows

    train = branch.train
    if len(train) > constants.MAX_ASCII_DOMINO_LEN:
        for domino in train[len(train)-constants.MAX_ASCII_DOMINO_LEN:len(train)]:
            _add_domino(domino)
    else:
        for domino in train:
            _add_domino(domino)
    
    if branch.train_on:
        _add_train()

    _draw()


def draw_branches(branches: list[Branch]) -> None:
    """Draws multiple trains or lines of dominoes to the screen."""
    for branch in branches:
        draw_branch(branch)


# def draw_hand(self, hand: set(Domino)) -> None:
#     """Draws a player's hand of dominoes."""
#     ...