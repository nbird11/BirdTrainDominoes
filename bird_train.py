"""Bird house-rules version of Mexican Train Dominoes.

AI players will calculate the best move based on all possible move options.
"""

import random

AMMT_PLAYERS = 4
DEAL_AMMT = 15
DOUBLE_TWELVES_VALUE = 12

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

    def __repr__(self) -> str:
        """Representation of the `Boneyard` object, including all dominoes
        still left in the draw pile.
        """
        self._update()
        rep: str = "Boneyard("
        rep += "\n\tdraw_pile=\n\t["
        for i, domino in enumerate(self.draw_pile):
            # Last Domino but not first column
            if i == len(self.draw_pile)-1 and i % 3 != 0:
                rep += f"{domino}"
            # Last Domino and first column
            elif i == len(self.draw_pile)-1:
                rep += f"\n\t\t{domino}"
            # First column
            elif i % 3 == 0:
                col_1: Domino = domino
                rep += f"\n\t\t{col_1},\t"
            # Second column
            elif i % 3 == 1:
                col_2: Domino = domino
                rep += f"{col_2},\t"
            # Third column
            elif i % 3 == 2:
                col_3: Domino = domino
                rep += f"{col_3}"
        rep += f"\n\t],"
        rep += f"\n\tcount_tiles={self.tile_count},"
        rep += f"\n\tround_num={self.round_num}\n)"
        return rep


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
        self.hand: set = set()

    def __repr__(self) -> str:
        """Representation of an instance of `Player`."""
        rep: str = "Player("
        rep += f"ai={self.ai}, "
        rep += f"hand={self.hand})"
        return rep
    
    def _draw(self, boneyard: Boneyard) -> None:
        """Takes the last domino in the passed boneyard and puts it in the
        player's hand.
        """
        self.hand.add(boneyard.draw_pile.pop())


class Game:
    """Handles all game actions."""
    def __init__(self) -> None:
        """Constructs a `Game` object"""
        self.ammt_players: int = AMMT_PLAYERS
        self.players: list[Player] = []
        self.round_num: int = 12
        self.boneyard: Boneyard = None


    def round_init(self, num_round: int) -> None:
        """Starts the game."""
        # Create each player, taking amount of AI players into account
        ammt_players_real = int(input(f"How many real players? (1-{AMMT_PLAYERS})\n> "))
        for _ in range(self.ammt_players):
            if ammt_players_real:
                self.players.append(Player())
                ammt_players_real -= 1
            else:
                self.players.append(Player(ai=True))

        self.round_num = num_round
        self.boneyard = Boneyard(self.round_num)
        self._deal()


    def _deal(self) -> None:
        """Deals the tiles from the boneyard. Is called at the beginning of
        each round.
        """
        for _ in range(DEAL_AMMT):
            for player in self.players:
                player._draw(self.boneyard)
        


def main():
    """Runs the game."""

    game = Game()
    game.round_init(12)
    
    # update_turn()
    # show_possible_moves()
    # if no_possible_moves
    #     draw_tile()
    #        update_DrawPile()
    #     if can_play
    #         play_tile()
    # else
    #     choose_move() ~

if __name__ == '__main__':
    main()