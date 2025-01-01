"""Houses the `Player` class."""

from domino import Domino
from boneyard import Boneyard


class Player:
    """A player of the game."""

    def __init__(self, ai: bool = False, id: str = "ai_", score: int = 0) -> None:
        """Constructs a `Player`."""
        self.ai: bool = ai
        self.hand: list[Domino] = []
        self.id: str = id
        self.score: int = score

    def draw(self, boneyard: Boneyard) -> None:
        """Takes the last domino in the passed boneyard and puts it in the
        player's hand.
        """
        assert (
            len(boneyard.draw_pile) > 0
        ), """Boneyard probably shouldn't be empty.
When boneyard is empty, need to add functionality to end round and
count the pips of dominos still in each player's hand."""
        self.hand.append(boneyard.draw_pile.pop())

    def __repr__(self, depth: int = 1) -> str:
        """Representation of an instance of `Player`."""
        indentation0: str = "    " * (depth - 1)
        indentation1: str = "    " * depth
        attributes: str = ""
        attributes += f"\n{indentation1}ai={self.ai},"
        attributes += f"\n{indentation1}hand={self.hand},"
        attributes += f"\n{indentation1}initials={self.id},"
        attributes += f"\n{indentation1}score={self.score}"
        return f"\n{indentation0}Player({attributes}\n{indentation0})"
