"""Houses the `Board` class."""

import constants
from branch import Branch
from domino import Domino
from player import Player


class Board:
    """The board that the game is played on."""
    def __init__(self, num_round: int, players: list[Player]) -> None:
        """Constructs a `Board` object for the round."""
        self.branches: list[Branch] = []
        self.round_num: int = num_round
        self.middle_tile: Domino = Domino(self.round_num, self.round_num)
        self.players: list[Player] = players
        # Create list of all branches stemming from the middle
        for player in self.players:
            self.branches.append(Branch(player))
        for _ in range(constants.AMMT_BRANCHES-len(self.players)):
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
            attributes += f"\n{indentation1}],"
        attributes += f"\n{indentation1}round_num={self.round_num},"
        attributes += f"\n{indentation1}middle_tile={self.middle_tile},"
        if isinstance(self.players, list):
            attributes += f"\n{indentation1}players=["
            for i, player in enumerate(self.players):
                attributes += player.__repr__(depth+2)
                if i != len(self.players)-1:
                    attributes += ","
            attributes += f"\n{indentation1}]"
        return f"\n{indentation0}Board({attributes}\n{indentation0})"
