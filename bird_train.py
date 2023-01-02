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

    def __repr__(self) -> str:
        """Representation of the `Boneyard` object, including all dominoes
        still left in the draw pile.
        """
        self._update()
        # rep: str = "Boneyard("
        # rep += "\n\t\tdraw_pile=["
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
        # rep += f"\n\t\tcount_tiles={self.tile_count},"
        # rep += f"\n\t\tround_num={self.round_num}\n\t)"

        rep: str = "Boneyard("
        rep += f"draw_pile={self.draw_pile}, "
        rep += f"tile_count={self.tile_count}, "
        rep += f"round_num={self.round_num})"
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
        self.hand: set[Domino] = set()

    def __repr__(self) -> str:
        """Representation of an instance of `Player`."""
        rep: str = "Player("
        rep += f"ai={self.ai}, "
        rep += f"hand={self.hand})"
        return rep
    
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

    def __repr__(self) -> str:
        """Representation of a `Branch` on the `Board`"""
        rep: str = "Branch("
        rep += f"player={self.player}, "
        rep += f"train_on={self.train_on}, "
        rep += f"train={self.train})"
        return rep

    def toggle_train_on(self) -> None:
        """Toggles whether the branch is set to be able to be played on by
        anyone or not. If there is no player attached to the branch, `train_on`
        should always remain False.
        """
        if self.player:
            self.train_on = not self.train_on


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
        
        for i, branch in enumerate(self.branches):
            print(f"branch_{i}={branch}")

    def __repr__(self) -> str:
        rep: str = "Board("
        rep += f"branches={self.branches}, "
        rep += f"round_num={self.round_num}, "
        rep += f"middle_tile={self.middle_tile}, "
        rep += f"players={self.players})"
        return rep


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

    def __repr__(self) -> None:
        """Representation of all current game info."""
        rep: str = "Game("
        rep += f"ammt_players={self.ammt_players}, "
        rep += f"players={self.players}, "
        rep += f"turn_i={self.turn_i}, "
        rep += f"round_num={self.round_num}, "
        rep += f"boneyard={self.boneyard}, "
        rep += f"board={self.board})"
        return rep

    def gameloop(self) -> None:
        """Handle the main gameloop."""
        while self.round_num >= 0:
            self._roundloop()
            print(self)
            return              # For testing the round loop for one round
            self.round_num -= 1

    def _roundloop(self) -> None:
        """Handle the loop for each individual round."""
        self._round_init()
        self._update_turn()
        
        # show_possible_moves()             # TODO
        # if no_possible_moves              # TODO
            # draw_tile()                   # TODO
            #    update_DrawPile()          # TODO
            # if can_play                   # TODO
                # play_tile()               # TODO
        # else                              # TODO
            # choose_move() ~               # TODO

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
    

if __name__ == '__main__':
    main()