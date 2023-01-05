"""Bird house-rules version of Mexican Train Dominoes.

AI players will calculate the best move based on all possible move options.
"""

import random

AMMT_PLAYERS = 4
DEAL_AMMT = 15
DOUBLE_TWELVES_VALUE = 12
AMMT_BRANCHES = 8

class Domino:
    """A tile that has a certain amount of dots (pips) on both ends."""
    def __init__(self, value_end1: int, value_end2: int) -> None:
        """Constructs a `Domino`."""
        self.end1_pips: int = value_end1
        self.end2_pips: int = value_end2

    def __repr__(self) -> str:
        """Representation of `Domino` object."""
        end1: str
        end2: str
        if self.end1_pips < 10:
            end1 = f" {self.end1_pips}"
        else:
            end1 = f"{self.end1_pips}"
        if self.end2_pips < 10:
            end2 = f"{self.end2_pips} "
        else:
            end2 = f"{self.end2_pips}"
        
        # rep: str = f"[{end1}|{end2}]"
        rep: str = f"[{self.end1_pips}|{self.end2_pips}]"
        return rep

    def add_ascii_to_cursor(self, rows: list[str] = ['', '', '', '', '', '', '', '', '']):
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
            rows[0] += '╭─────╮'
            rows[4] += '├─────┤'
            rows[8] += '╰─────╯'

            # Domino values
            if self.end1_pips == 12:
                rows[1] += f'│{four_top}│'
                rows[2] += f'│{four_across}│'
                rows[3] += f'│{four_btm}│'
                rows[5] += f'│{four_top}│'
                rows[6] += f'│{four_across}│'
                rows[7] += f'│{four_btm}│'
            elif self.end1_pips == 11:
                rows[1] += f'│{four_top}│'
                rows[2] += f'│{three_across}│'
                rows[3] += f'│{four_btm}│'
                rows[5] += f'│{four_top}│'
                rows[6] += f'│{three_across}│'
                rows[7] += f'│{four_btm}│'
            elif self.end1_pips == 10:
                rows[1] += f'│{four_across}│'
                rows[2] += f'│{two_across}│'
                rows[3] += f'│{four_across}│'
                rows[5] += f'│{four_across}│'
                rows[6] += f'│{two_across}│'
                rows[7] += f'│{four_across}│'
            elif self.end1_pips == 9:
                rows[1] += f'│{three_across}│'
                rows[2] += f'│{three_across}│'
                rows[3] += f'│{three_across}│'
                rows[5] += f'│{three_across}│'
                rows[6] += f'│{three_across}│'
                rows[7] += f'│{three_across}│'
            elif self.end1_pips == 8:
                rows[1] += f'│{three_across}│'
                rows[2] += f'│{two_across}│'
                rows[3] += f'│{three_across}│'
                rows[5] += f'│{three_across}│'
                rows[6] += f'│{two_across}│'
                rows[7] += f'│{three_across}│'
            elif self.end1_pips == 7:
                rows[1] += f'│{two_across}│'
                rows[2] += f'│{three_across}│'
                rows[3] += f'│{two_across}│'
                rows[5] += f'│{two_across}│'
                rows[6] += f'│{three_across}│'
                rows[7] += f'│{two_across}│'
            elif self.end1_pips == 6:
                rows[1] += f'│{two_across}│'
                rows[2] += f'│{two_across}│'
                rows[3] += f'│{two_across}│'
                rows[5] += f'│{two_across}│'
                rows[6] += f'│{two_across}│'
                rows[7] += f'│{two_across}│'
            elif self.end1_pips == 5:
                rows[1] += f'│{two_across}│'
                rows[2] += f'│{one_mid}│'
                rows[3] += f'│{two_across}│'
                rows[5] += f'│{two_across}│'
                rows[6] += f'│{one_mid}│'
                rows[7] += f'│{two_across}│'
            elif self.end1_pips == 4:
                rows[1] += f'│{two_across}│'
                rows[2] += f'│{blank_across}│'
                rows[3] += f'│{two_across}│'
                rows[5] += f'│{two_across}│'
                rows[6] += f'│{blank_across}│'
                rows[7] += f'│{two_across}│'
            elif self.end1_pips == 3:
                rows[1] += f'│{one_top}│'
                rows[2] += f'│{one_mid}│'
                rows[3] += f'│{one_btm}│'
                rows[5] += f'│{one_top}│'
                rows[6] += f'│{one_mid}│'
                rows[7] += f'│{one_btm}│'
            elif self.end1_pips == 2:
                rows[1] += f'│{one_top}│'
                rows[2] += f'│{blank_across}│'
                rows[3] += f'│{one_btm}│'
                rows[5] += f'│{one_top}│'
                rows[6] += f'│{blank_across}│'
                rows[7] += f'│{one_btm}│'
            elif self.end1_pips == 1:
                rows[1] += f'│{blank_across}│'
                rows[2] += f'│{one_mid}│'
                rows[3] += f'│{blank_across}│'
                rows[5] += f'│{blank_across}│'
                rows[6] += f'│{one_mid}│'
                rows[7] += f'│{blank_across}│'
            elif self.end1_pips == 0:
                rows[1] += f'│{blank_across}│'
                rows[2] += f'│{blank_across}│'
                rows[3] += f'│{blank_across}│'
                rows[5] += f'│{blank_across}│'
                rows[6] += f'│{blank_across}│'
                rows[7] += f'│{blank_across}│'
        # Draw horizontal.
        else:
            # Top and bottom rows
            rows[0] += '             '
            rows[1] += '             '
            rows[2] += '╭─────┬─────╮'
            rows[6] += '╰─────┴─────╯'
            rows[7] += '             '
            rows[8] += '             '

            # Domino values end1
            if self.end1_pips == 12:
                rows[3] += f'|{four_top}|'
                rows[4] += f'|{four_across}|'
                rows[5] += f'|{four_btm}|'
            elif self.end1_pips == 11:
                rows[3] += f'│{four_top}│'
                rows[4] += f'│{three_across}│'
                rows[5] += f'│{four_btm}│'
            elif self.end1_pips == 10:
                rows[3] += f'│{four_across}│'
                rows[4] += f'│{two_across}│'
                rows[5] += f'│{four_across}│'
            elif self.end1_pips == 9:
                rows[3] += f'│{three_across}│'
                rows[4] += f'│{three_across}│'
                rows[5] += f'│{three_across}│'
            elif self.end1_pips == 8:
                rows[3] += f'│{three_across}│'
                rows[4] += f'│{two_across}│'
                rows[5] += f'│{three_across}│'
            elif self.end1_pips == 7:
                rows[3] += f'│{two_across}│'
                rows[4] += f'│{three_across}│'
                rows[5] += f'│{two_across}│'
            elif self.end1_pips == 6:
                rows[3] += f'│{two_across}│'
                rows[4] += f'│{two_across}│'
                rows[5] += f'│{two_across}│'
            elif self.end1_pips == 5:
                rows[3] += f'│{two_across}│'
                rows[4] += f'│{one_mid}│'
                rows[5] += f'│{two_across}│'
            elif self.end1_pips == 4:
                rows[3] += f'│{two_across}│'
                rows[4] += f'│{blank_across}│'
                rows[5] += f'│{two_across}│'
            elif self.end1_pips == 3:
                rows[3] += f'│{one_top}│'
                rows[4] += f'│{one_mid}│'
                rows[5] += f'│{one_btm}│'
            elif self.end1_pips == 2:
                rows[3] += f'│{one_top}│'
                rows[4] += f'│{blank_across}│'
                rows[5] += f'│{one_btm}│'
            elif self.end1_pips == 1:
                rows[3] += f'│{blank_across}│'
                rows[4] += f'│{one_mid}│'
                rows[5] += f'│{blank_across}│'
            elif self.end1_pips == 0:
                rows[3] += f'│{blank_across}│'
                rows[4] += f'│{blank_across}│'
                rows[5] += f'│{blank_across}│'

            # Domino values end2
            if self.end2_pips == 12:
                rows[3] += f'{four_top}|'
                rows[4] += f'{four_across}|'
                rows[5] += f'{four_btm}|'
            elif self.end2_pips == 11:
                rows[3] += f'{four_top}│'
                rows[4] += f'{three_across}│'
                rows[5] += f'{four_btm}│'
            elif self.end2_pips == 10:
                rows[3] += f'{four_across}│'
                rows[4] += f'{two_across}│'
                rows[5] += f'{four_across}│'
            elif self.end2_pips == 9:
                rows[3] += f'{three_across}│'
                rows[4] += f'{three_across}│'
                rows[5] += f'{three_across}│'
            elif self.end2_pips == 8:
                rows[3] += f'{three_across}│'
                rows[4] += f'{two_across}│'
                rows[5] += f'{three_across}│'
            elif self.end2_pips == 7:
                rows[3] += f'{two_across}│'
                rows[4] += f'{three_across}│'
                rows[5] += f'{two_across}│'
            elif self.end2_pips == 6:
                rows[3] += f'{two_across}│'
                rows[4] += f'{two_across}│'
                rows[5] += f'{two_across}│'
            elif self.end2_pips == 5:
                rows[3] += f'{two_across}│'
                rows[4] += f'{one_mid}│'
                rows[5] += f'{two_across}│'
            elif self.end2_pips == 4:
                rows[3] += f'{two_across}│'
                rows[4] += f'{blank_across}│'
                rows[5] += f'{two_across}│'
            elif self.end2_pips == 3:
                rows[3] += f'{one_top}│'
                rows[4] += f'{one_mid}│'
                rows[5] += f'{one_btm}│'
            elif self.end2_pips == 2:
                rows[3] += f'{one_top}│'
                rows[4] += f'{blank_across}│'
                rows[5] += f'{one_btm}│'
            elif self.end2_pips == 1:
                rows[3] += f'{blank_across}│'
                rows[4] += f'{one_mid}│'
                rows[5] += f'{blank_across}│'
            elif self.end2_pips == 0:
                rows[3] += f'{blank_across}│'
                rows[4] += f'{blank_across}│'
                rows[5] += f'{blank_across}│'
        
        return rows


class Boneyard:
    """The draw pile."""
    def __init__(self, num_round: int) -> None:
        """Constructs a new `Boneyard` with all the dominoes in the game."""
        self.draw_pile: list[Domino] = []
        for i in range(DOUBLE_TWELVES_VALUE+1):
            for j in range(i, DOUBLE_TWELVES_VALUE+1):
                if not ((i == j) and (i == num_round)):
                    domino = Domino(i, j)
                    self.draw_pile.append(domino)
        random.shuffle(self.draw_pile)
        self.tile_count: int = len(self.draw_pile)
        self.round_num: int = num_round

    def __repr__(self, depth: int = 1) -> str:
        """Representation of the `Boneyard` object, including all dominoes
        still left in the draw pile.
        """
        self._update()

     #### Remnant of three-columned draw_pile repr ####
        # rep: str = "\n\t\tdraw_pile=["
        # for i, domino in enumerate(self.draw_pile):
        #     # Last Domino but not first column
        #     if i == len(self.draw_pile)-1 and i % 3 != 0:
        #         rep += f"{domino}"
        #     # Last Domino and first column
        #     elif i == len(self.draw_pile)-1:
        #         rep += f"\n\t\t\t{domino}"
        #     # First column
        #     elif i % 3 == 0:
        #         col_1: Domino = domino
        #         rep += f"\n\t\t\t{col_1},\t"
        #     # Second column
        #     elif i % 3 == 1:
        #         col_2: Domino = domino
        #         rep += f"{col_2},\t"
        #     # Third column
        #     elif i % 3 == 2:
        #         col_3: Domino = domino
        #         rep += f"{col_3}"
        # rep += f"],"

        indentation0: str = '    ' * (depth-1)
        indentation1: str = '    ' * depth
        indentation2: str = '    ' * (depth+1)
        attributes: str = ""
        if isinstance(self.draw_pile, list):
            attributes += f"\n{indentation1}draw_pile=["
            for i, domino in enumerate(self.draw_pile):
                attributes += f"\n{indentation2}{domino}"
                if i != len(self.draw_pile)-1:
                    attributes += ","
            attributes += f"\n{indentation1}]"
        attributes += f"\n{indentation1}tile_count={self.tile_count}, "
        attributes += f"\n{indentation1}round_num={self.round_num}"
        return f"\n{indentation0}Boneyard({attributes}\n{indentation0})"

    def _update(self) -> None:
        """Updates the `tile_count` attribute.

        Usually will be called after deal or draw methods change the length
        of the `draw_pile`.
        """
        self.tile_count = len(self.draw_pile)


class Player:
    """A player of the game."""
    def __init__(self, ai: bool = False) -> None:
        """Constructs a `Player`."""
        self.ai: bool = ai
        self.hand: set[Domino] = set()

    def __repr__(self, depth: int = 1) -> str:
        """Representation of an instance of `Player`."""
        indentation0: str = '    ' * (depth-1)
        indentation1: str = '    ' * depth
        attributes: str = ""
        attributes += f"\n{indentation1}ai={self.ai}, "
        attributes += f"\n{indentation1}hand={self.hand}"
        return f"\n{indentation0}Player({attributes}\n{indentation0})"
    
    def draw(self, boneyard: Boneyard) -> None:
        """Takes the last domino in the passed boneyard and puts it in the
        player's hand.
        """
        self.hand.add(boneyard.draw_pile.pop())


class Branch:
    """A branch of the play area."""
    def __init__(self, player: Player | None = None) -> None:
        """Constructs a `Branch` object."""
        self.player: Player | None = player
        # Assign whether the branch can be played on by anyone.
        self.train_on: bool = None
        if self.player:
            self.train_on = True
        else:
            self.train_on = False
        self.train: list[Domino] = []

    def __repr__(self, depth: int = 1) -> str:
        """Representation of a `Branch` on the `Board`"""
        indentation0: str = '    ' * (depth-1)
        indentation1: str = '    ' * depth
        indentation2: str = '    ' * (depth+1)
        attributes: str = ""
        if isinstance(self.player, Player):
            attributes += f"\n{indentation1}player={self.player.__repr__(depth+2)},"
        else:
            attributes += f"\n{indentation1}player=None,"
        attributes += f"\n{indentation1}train_on={self.train_on},"
        if isinstance(self.train, list):
            attributes += f"\n{indentation1}train=["
            for i, domino in enumerate(self.train):
                attributes += f"\n{indentation2}{domino}"
                if i != len(self.train)-1:
                    attributes += ","
            attributes += f"\n{indentation1}]"
        return f"\n{indentation0}Branch({attributes}\n{indentation0})"

    def toggle_train_on(self) -> None:
        """Toggles whether the branch is set to be able to be played on by
        anyone or not. If there is no player attached to the branch, `train_on`
        should always remain False.
        """
        if self.player:
            self.train_on = not self.train_on

    def add_to_train(self, domino: Domino) -> None:
        """Adds the passed `Domino` to the end of the branch's `train`."""
        self.train.append(domino)


class Board:
    """TODO The board that the game is played on."""
    def __init__(self, num_round: int, players: list[Player]) -> None:
        """Constructs a `Board` object for the round."""
        self.branches: list[Branch] = []
        self.round_num: int = num_round
        self.middle_tile: Domino = Domino(self.round_num, self.round_num)
        self.players: list[Player] = players
        # Create list of all branches stemming from the middle
        for player in self.players:
            self.branches.append(Branch(player))
        for _ in range(AMMT_BRANCHES-len(self.players)):
            self.branches.append(Branch())

    def __repr__(self, depth: int = 1) -> str:
        indentation0: str = '    ' * (depth-1)
        indentation1: str = '    ' * depth
        attributes: str = ""
        if isinstance(self.branches, list):
            attributes += f"\n{indentation1}branches=["
            for i, branch in enumerate(self.branches):
                attributes += branch.__repr__(depth+2)
                if i != len(self.branches)-1:
                    attributes += ","
            attributes += f"\n{indentation1}]"
        attributes += f"\n{indentation1}round_num={self.round_num}, "
        attributes += f"\n{indentation1}middle_tile={self.middle_tile}, "
        if isinstance(self.players, list):
            attributes += f"\n{indentation1}players=["
            for i, player in enumerate(self.players):
                attributes += player.__repr__(depth+2)
                if i != len(self.players)-1:
                    attributes += ","
            attributes += f"\n{indentation1}]"
        return f"\n{indentation0}Board({attributes}\n{indentation0})"

    def initial_trains(self) -> None:
        """Lets every player add an initial train to their personal branch.
        
        AI players automatically calculate an initial train using the most pips;
        Regular players can choose the dominoes in their initial train.
        """
        print(f"\nROUND {self.round_num}: INITIAL TRAINS\n")
        for branch in self.branches:
            branch.train.append(self.middle_tile)
        for i_player, player in enumerate(self.players):
            # Real player picks their dominoes from options list.
            if not player.ai:
                print(f"Middle tile: {self.middle_tile}")
                # Set initial compare value (which is the round number).
                compare_value: int = self.round_num
                # Get list of all dominos with ends matching round num and move them to options buffer.
                options: list[Domino] = [domino for domino in player.hand if domino.end1_pips == compare_value or domino.end2_pips == compare_value]
                for domino in options:
                    player.hand.remove(domino)
                    if domino.end2_pips == compare_value:
                        domino.end1_pips, domino.end2_pips = domino.end2_pips, domino.end1_pips
                print(f"Your hand: {player.hand}")
                # Continue while options for playing still remain.
                while options:
                    # Print list with indicies for picking choice.
                    print(f"Option number and domino for first domino in train: {[(i_options, domino) for i_options, domino in enumerate(options)]}")
                    # Get choice (index).
                    choice: int = int(input(f"Pick which domino to start: {[i_options for i_options in range(len(options))]}\n> "))

                    choice_domino: Domino = options[choice]

                    # Add domino to branch and remove from options buffer.
                    self.branches[i_player].add_to_train(choice_domino)
                    options.remove(choice_domino)

                    # Return all dominoes in options buffer to hand.
                    for domino in options:
                        player.hand.add(domino)

                    # Get new compare value
                    if choice_domino.end1_pips == compare_value:
                        new_compare_value: int = choice_domino.end2_pips
                    else:
                        new_compare_value: int = choice_domino.end1_pips

                    # Replace old compare_value
                    compare_value = new_compare_value

                    # Get new list of options for next domino in train and move from hand to options buffer.
                    options = [domino for domino in player.hand if domino.end1_pips == compare_value or domino.end2_pips == compare_value]
                    for domino in options:
                        player.hand.remove(domino)
                        if domino.end2_pips == compare_value:
                            domino.end1_pips, domino.end2_pips = domino.end2_pips, domino.end1_pips

                    # Print train and hand to screen
                    print(f"Train: {self.branches[i_player].train}")
                    print(f"Hand: {player.hand}")
                else:
                    print("No options\n\n")
            # AI calculates best initial train
            else:
                ...


class Game:
    """Handles all game actions."""
    def __init__(self) -> None:
        """Constructs a `Game` object"""
        self.ammt_players: int = AMMT_PLAYERS
        self.players: list[Player] = []
        # Create each player, taking amount of AI players into account
        print(f"\nGAME: START\n")
        ammt_players_real = int(input(f"How many real players? (1-{self.ammt_players})\n> "))
        for _ in range(self.ammt_players):
            if ammt_players_real:
                self.players.append(Player())
                ammt_players_real -= 1
            else:
                self.players.append(Player(ai=True))
        self.turn_i: int = -1       # Starts at -1 because `_update_turn` increments it
        self.round_num: int = 12
        self.boneyard: Boneyard = None
        self.board: Board = None

    def __repr__(self, depth: int = 1) -> None:
        """Representation of all current game info."""
        indentation0: str = '    ' * (depth-1)
        indentation1: str = '    ' * depth
        attributes: str = ""
        attributes += f"\n{indentation1}ammt_players={self.ammt_players},"
        if isinstance(self.players, list):
            attributes += f"\n{indentation1}players=["
            for i, player in enumerate(self.players):
                attributes += player.__repr__(depth+2)
                if i != len(self.players)-1:
                    attributes += ","
            attributes += f"\n{indentation1}]"
        attributes += f"\n{indentation1}turn_i={self.turn_i},"
        attributes += f"\n{indentation1}round_num={self.round_num},"
        if isinstance(self.boneyard, Boneyard):
            attributes += f"\n{indentation1}boneyard={self.boneyard.__repr__(depth+2)},"
        if isinstance(self.board, Board):
            attributes += f"\n{indentation1}board={self.board.__repr__(depth+2)}"
        return f"\n{indentation0}Game({attributes}\n{indentation0})"

    def gameloop(self) -> None:
        """Handle the main gameloop."""
        while self.round_num >= 0:
            self._roundloop()
            return              # For testing the round loop for one round
            self.round_num -= 1

    def _roundloop(self) -> None:
        """Handle the loop for each individual round."""
        self._round_init()
        self._update_turn()
        
        self.board.initial_trains()         # TODO AI
        # show_possible_moves()             # TODO
        # if no_possible_moves              # TODO
        #    draw_tile()                    # TODO
        #    update_DrawPile()              # TODO
        #    if can_play                    # TODO
        #       play_tile()                 # TODO
        # else                              # TODO
        #    choose_move() ~                # TODO

    def _round_init(self) -> None:
        """Starts the round."""
        self.boneyard = Boneyard(self.round_num)
        self._deal()
        self.board = Board(self.round_num, self.players)

    def _deal(self) -> None:
        """Deals the tiles from the boneyard. Is called at the beginning of
        each round.
        """
        for _ in range(DEAL_AMMT):
            for player in self.players:
                player.draw(self.boneyard)

    def _update_turn(self) -> None:
        """Updates the turn cycle to the next player's index in `players` list"""
        self.turn_i += 1
        if self.turn_i >= len(self.players):
            self.turn_i = 0


def main():
    """Runs the game."""
    game = Game()
    game.gameloop()
    # print(game)
    

if __name__ == '__main__':
    main()