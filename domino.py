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