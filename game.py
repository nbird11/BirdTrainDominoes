"""Houses the `Game` class."""

from constants import Constants
from player import Player
from boneyard import Boneyard
from board import Board

class Game:
    """Handles all game actions."""
    def __init__(self) -> None:
        """Constructs a `Game` object"""
        self.ammt_players: int = Constants.AMMT_PLAYERS
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
        for _ in range(Constants.DEAL_AMMT):
            for player in self.players:
                player.draw(self.boneyard)

    def _update_turn(self) -> None:
        """Updates the turn cycle to the next player's index in `players` list"""
        self.turn_i += 1
        if self.turn_i >= len(self.players):
            self.turn_i = 0