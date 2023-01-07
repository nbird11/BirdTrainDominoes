"""Houses the `Branch` class."""

from player import Player
from domino import Domino

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

    def __eq__(self, _other: object) -> bool:
        return self.__dict__ == _other.__dict__

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