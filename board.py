"""Houses the `Board` class."""

import constants
from player import Player
from branch import Branch
from domino import Domino

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

    def initial_trains(self) -> None:
        """Lets every player add an initial train to their personal branch.
        
        AI players automatically calculate an initial train using the most pips;
        Regular players can choose the dominoes in their initial train.
        """
        print(f"\nROUND {self.round_num}: INITIAL TRAINS\n")
        for branch in self.branches:
            branch.train.append(self.middle_tile)
        for i_player, player in enumerate(self.players):
            # Real player picks their dominoes from options list.
            if not player.ai:
                print(f"Middle tile: {self.middle_tile}")
                # Set initial compare value (which is the round number).
                compare_value: int = self.round_num
                # Get list of all dominos with ends matching round num and move them to options buffer.
                options: list[Domino] = [domino for domino in player.hand if domino.end1_pips == compare_value or domino.end2_pips == compare_value]
                for domino in options:
                    player.hand.remove(domino)
                    if domino.end2_pips == compare_value:
                        domino.end1_pips, domino.end2_pips = domino.end2_pips, domino.end1_pips
                print(f"Your hand: {player.hand}")
                # Continue while options for playing still remain.
                while options:
                    # Print list with indicies for picking choice.
                    print(f"Option number and domino for first domino in train: {[(i_options, domino) for i_options, domino in enumerate(options)]}")
                    # Get choice (index).
                    choice: int = int(input(f"Pick which domino to start: {[i_options for i_options in range(len(options))]}\n> "))

                    choice_domino: Domino = options[choice]

                    # Add domino to branch and remove from options buffer.
                    self.branches[i_player].add_to_train(choice_domino)
                    options.remove(choice_domino)

                    # Return all dominoes in options buffer to hand.
                    for domino in options:
                        player.hand.add(domino)

                    # Get new compare value
                    if choice_domino.end1_pips == compare_value:
                        new_compare_value: int = choice_domino.end2_pips
                    else:
                        new_compare_value: int = choice_domino.end1_pips

                    # Replace old compare_value
                    compare_value = new_compare_value

                    # Get new list of options for next domino in train and move from hand to options buffer.
                    options = [domino for domino in player.hand if domino.end1_pips == compare_value or domino.end2_pips == compare_value]
                    for domino in options:
                        player.hand.remove(domino)
                        if domino.end2_pips == compare_value:
                            domino.end1_pips, domino.end2_pips = domino.end2_pips, domino.end1_pips

                    # Print train and hand to screen
                    print(f"Train: {self.branches[i_player].train}")
                    print(f"Hand: {player.hand}")
                else:
                    print("No options\n\n")
            # AI calculates best initial train
            else:
                ...