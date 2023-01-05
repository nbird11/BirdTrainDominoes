"""Houses the `Boneyard` class."""

import random
import constants
from domino import Domino

class Boneyard:
    """The draw pile."""
    def __init__(self, num_round: int) -> None:
        """Constructs a new `Boneyard` with all the dominoes in the game."""
        self.draw_pile: list[Domino] = []
        for i in range(constants.DOUBLE_TWELVES_VALUE+1):
            for j in range(i, constants.DOUBLE_TWELVES_VALUE+1):
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