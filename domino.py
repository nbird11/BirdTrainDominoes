"""Houses the `Domino` class."""
class Domino:
    """A tile that has a certain amount of dots (pips) on both ends."""
    def __init__(self, value_end1: int, value_end2: int) -> None:
        """Constructs a `Domino`."""
        self.end1_pips: int = value_end1
        self.end2_pips: int = value_end2

    def __repr__(self) -> str:
        """Representation of `Domino` object."""
        return f"[{self.end1_pips}|{self.end2_pips}]"

    def add_ascii_to_cursor(self, cursor: list[str] = ['', '', '', '', '', '', '', '', '']):
        four_top = 'O OOO'
        four_across = 'OO OO'
        four_btm = 'OOO O'
        three_across = 'O O O'
        two_across = 'O   O'
        one_top = 'O    '
        one_mid = '  O  '
        one_btm = '    O'
        blank_across = '     '

        # Draw vertical.
        if self.end1_pips == self.end2_pips:
            # Top, middle, bottom rows
            cursor[0] += '╭─────╮'
            cursor[4] += '├─────┤'
            cursor[8] += '╰─────╯'

            # Domino values
            if self.end1_pips == 12:
                cursor[1] += f'│{four_top}│'
                cursor[2] += f'│{four_across}│'
                cursor[3] += f'│{four_btm}│'
                cursor[5] += f'│{four_top}│'
                cursor[6] += f'│{four_across}│'
                cursor[7] += f'│{four_btm}│'
            elif self.end1_pips == 11:
                cursor[1] += f'│{four_top}│'
                cursor[2] += f'│{three_across}│'
                cursor[3] += f'│{four_btm}│'
                cursor[5] += f'│{four_top}│'
                cursor[6] += f'│{three_across}│'
                cursor[7] += f'│{four_btm}│'
            elif self.end1_pips == 10:
                cursor[1] += f'│{four_across}│'
                cursor[2] += f'│{two_across}│'
                cursor[3] += f'│{four_across}│'
                cursor[5] += f'│{four_across}│'
                cursor[6] += f'│{two_across}│'
                cursor[7] += f'│{four_across}│'
            elif self.end1_pips == 9:
                cursor[1] += f'│{three_across}│'
                cursor[2] += f'│{three_across}│'
                cursor[3] += f'│{three_across}│'
                cursor[5] += f'│{three_across}│'
                cursor[6] += f'│{three_across}│'
                cursor[7] += f'│{three_across}│'
            elif self.end1_pips == 8:
                cursor[1] += f'│{three_across}│'
                cursor[2] += f'│{two_across}│'
                cursor[3] += f'│{three_across}│'
                cursor[5] += f'│{three_across}│'
                cursor[6] += f'│{two_across}│'
                cursor[7] += f'│{three_across}│'
            elif self.end1_pips == 7:
                cursor[1] += f'│{two_across}│'
                cursor[2] += f'│{three_across}│'
                cursor[3] += f'│{two_across}│'
                cursor[5] += f'│{two_across}│'
                cursor[6] += f'│{three_across}│'
                cursor[7] += f'│{two_across}│'
            elif self.end1_pips == 6:
                cursor[1] += f'│{two_across}│'
                cursor[2] += f'│{two_across}│'
                cursor[3] += f'│{two_across}│'
                cursor[5] += f'│{two_across}│'
                cursor[6] += f'│{two_across}│'
                cursor[7] += f'│{two_across}│'
            elif self.end1_pips == 5:
                cursor[1] += f'│{two_across}│'
                cursor[2] += f'│{one_mid}│'
                cursor[3] += f'│{two_across}│'
                cursor[5] += f'│{two_across}│'
                cursor[6] += f'│{one_mid}│'
                cursor[7] += f'│{two_across}│'
            elif self.end1_pips == 4:
                cursor[1] += f'│{two_across}│'
                cursor[2] += f'│{blank_across}│'
                cursor[3] += f'│{two_across}│'
                cursor[5] += f'│{two_across}│'
                cursor[6] += f'│{blank_across}│'
                cursor[7] += f'│{two_across}│'
            elif self.end1_pips == 3:
                cursor[1] += f'│{one_top}│'
                cursor[2] += f'│{one_mid}│'
                cursor[3] += f'│{one_btm}│'
                cursor[5] += f'│{one_top}│'
                cursor[6] += f'│{one_mid}│'
                cursor[7] += f'│{one_btm}│'
            elif self.end1_pips == 2:
                cursor[1] += f'│{one_top}│'
                cursor[2] += f'│{blank_across}│'
                cursor[3] += f'│{one_btm}│'
                cursor[5] += f'│{one_top}│'
                cursor[6] += f'│{blank_across}│'
                cursor[7] += f'│{one_btm}│'
            elif self.end1_pips == 1:
                cursor[1] += f'│{blank_across}│'
                cursor[2] += f'│{one_mid}│'
                cursor[3] += f'│{blank_across}│'
                cursor[5] += f'│{blank_across}│'
                cursor[6] += f'│{one_mid}│'
                cursor[7] += f'│{blank_across}│'
            elif self.end1_pips == 0:
                cursor[1] += f'│{blank_across}│'
                cursor[2] += f'│{blank_across}│'
                cursor[3] += f'│{blank_across}│'
                cursor[5] += f'│{blank_across}│'
                cursor[6] += f'│{blank_across}│'
                cursor[7] += f'│{blank_across}│'

        # Draw horizontal.
        else:
            # Top and bottom rows
            cursor[0] += '             '
            cursor[1] += '             '
            cursor[2] += '╭─────┬─────╮'
            cursor[6] += '╰─────┴─────╯'
            cursor[7] += '             '
            cursor[8] += '             '

            # Domino values end1
            if self.end1_pips == 12:
                cursor[3] += f'|{four_top}|'
                cursor[4] += f'|{four_across}|'
                cursor[5] += f'|{four_btm}|'
            elif self.end1_pips == 11:
                cursor[3] += f'│{four_top}│'
                cursor[4] += f'│{three_across}│'
                cursor[5] += f'│{four_btm}│'
            elif self.end1_pips == 10:
                cursor[3] += f'│{four_across}│'
                cursor[4] += f'│{two_across}│'
                cursor[5] += f'│{four_across}│'
            elif self.end1_pips == 9:
                cursor[3] += f'│{three_across}│'
                cursor[4] += f'│{three_across}│'
                cursor[5] += f'│{three_across}│'
            elif self.end1_pips == 8:
                cursor[3] += f'│{three_across}│'
                cursor[4] += f'│{two_across}│'
                cursor[5] += f'│{three_across}│'
            elif self.end1_pips == 7:
                cursor[3] += f'│{two_across}│'
                cursor[4] += f'│{three_across}│'
                cursor[5] += f'│{two_across}│'
            elif self.end1_pips == 6:
                cursor[3] += f'│{two_across}│'
                cursor[4] += f'│{two_across}│'
                cursor[5] += f'│{two_across}│'
            elif self.end1_pips == 5:
                cursor[3] += f'│{two_across}│'
                cursor[4] += f'│{one_mid}│'
                cursor[5] += f'│{two_across}│'
            elif self.end1_pips == 4:
                cursor[3] += f'│{two_across}│'
                cursor[4] += f'│{blank_across}│'
                cursor[5] += f'│{two_across}│'
            elif self.end1_pips == 3:
                cursor[3] += f'│{one_top}│'
                cursor[4] += f'│{one_mid}│'
                cursor[5] += f'│{one_btm}│'
            elif self.end1_pips == 2:
                cursor[3] += f'│{one_top}│'
                cursor[4] += f'│{blank_across}│'
                cursor[5] += f'│{one_btm}│'
            elif self.end1_pips == 1:
                cursor[3] += f'│{blank_across}│'
                cursor[4] += f'│{one_mid}│'
                cursor[5] += f'│{blank_across}│'
            elif self.end1_pips == 0:
                cursor[3] += f'│{blank_across}│'
                cursor[4] += f'│{blank_across}│'
                cursor[5] += f'│{blank_across}│'

            # Domino values end2
            if self.end2_pips == 12:
                cursor[3] += f'{four_top}|'
                cursor[4] += f'{four_across}|'
                cursor[5] += f'{four_btm}|'
            elif self.end2_pips == 11:
                cursor[3] += f'{four_top}│'
                cursor[4] += f'{three_across}│'
                cursor[5] += f'{four_btm}│'
            elif self.end2_pips == 10:
                cursor[3] += f'{four_across}│'
                cursor[4] += f'{two_across}│'
                cursor[5] += f'{four_across}│'
            elif self.end2_pips == 9:
                cursor[3] += f'{three_across}│'
                cursor[4] += f'{three_across}│'
                cursor[5] += f'{three_across}│'
            elif self.end2_pips == 8:
                cursor[3] += f'{three_across}│'
                cursor[4] += f'{two_across}│'
                cursor[5] += f'{three_across}│'
            elif self.end2_pips == 7:
                cursor[3] += f'{two_across}│'
                cursor[4] += f'{three_across}│'
                cursor[5] += f'{two_across}│'
            elif self.end2_pips == 6:
                cursor[3] += f'{two_across}│'
                cursor[4] += f'{two_across}│'
                cursor[5] += f'{two_across}│'
            elif self.end2_pips == 5:
                cursor[3] += f'{two_across}│'
                cursor[4] += f'{one_mid}│'
                cursor[5] += f'{two_across}│'
            elif self.end2_pips == 4:
                cursor[3] += f'{two_across}│'
                cursor[4] += f'{blank_across}│'
                cursor[5] += f'{two_across}│'
            elif self.end2_pips == 3:
                cursor[3] += f'{one_top}│'
                cursor[4] += f'{one_mid}│'
                cursor[5] += f'{one_btm}│'
            elif self.end2_pips == 2:
                cursor[3] += f'{one_top}│'
                cursor[4] += f'{blank_across}│'
                cursor[5] += f'{one_btm}│'
            elif self.end2_pips == 1:
                cursor[3] += f'{blank_across}│'
                cursor[4] += f'{one_mid}│'
                cursor[5] += f'{blank_across}│'
            elif self.end2_pips == 0:
                cursor[3] += f'{blank_across}│'
                cursor[4] += f'{blank_across}│'
                cursor[5] += f'{blank_across}│'

        return cursor