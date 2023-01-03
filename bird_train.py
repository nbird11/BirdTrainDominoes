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
            end1 = f"0{self.end1_pips}"
        else:
            end1 = f"{self.end1_pips}"
        if self.end2_pips < 10:
            end2 = f"0{self.end2_pips}"
        else:
            end2 = f"{self.end2_pips}"
        
        rep: str = f"{end1}|{end2}"
        return rep


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
        attributes += f"\n{indentation1}hand={self.hand})"
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


class Game:
    """Handles all game actions."""
    def __init__(self) -> None:
        """Constructs a `Game` object"""
        self.ammt_players: int = AMMT_PLAYERS
        self.players: list[Player] = []
        # Create each player, taking amount of AI players into account
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
        
        # initial_train()                   # TODO
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
    print(game)
    

if __name__ == '__main__':
    main()