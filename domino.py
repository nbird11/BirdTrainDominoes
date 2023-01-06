"""Houses the `Domino` class."""
class Domino:
    """A tile that has a certain amount of dots (pips) on both ends."""
    def __init__(self, value_end1: int, value_end2: int) -> None:
        """Constructs a `Domino`."""
        self.end1_pips: int = value_end1
        self.end2_pips: int = value_end2

    def __repr__(self) -> str:
        """Representation of `Domino` object."""
        return f"{self.end1_pips}|{self.end2_pips}"
    
    def __eq__(self, _other: object) -> bool:
        if isinstance(_other, self.__class__):
            return self.__dict__ == _other.__dict__ or (self.end1_pips == _other.end2_pips and self.end2_pips == _other.end1_pips)
        return False

    def flip(self) -> None:
        """Flips the end values of self domino."""
        self.end1_pips, self.end2_pips = self.end2_pips, self.end1_pips

    def matches(self, value: int) -> bool:
        """Returns bool, whether self domino could be played on a train with end `value`."""
        return self.end1_pips == value or self.end2_pips == value