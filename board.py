"""Houses the `Board` class."""

import cursor
import constants
from constants import sleeprint
from time import sleep
from branch import Branch
from domino import Domino
from player import Player


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
        sleeprint(f"\n\n\n\n\n\n\n\n\nRound {self.round_num}: Initial trains!\n\n\n\n\n\n\n\n\n")
        for branch in self.branches:
            branch.train.append(self.middle_tile)
        for i_player, player in enumerate(self.players):
            # Real player picks their dominoes from options list.
            if not player.ai:
                print(f"Player {i_player+1}: {player.initials}")
                print(f"Middle tile: {self.middle_tile}")
                cursor.draw_domino(self.middle_tile)

                # Set initial compare value (which is the round number).
                compare_value: int = self.round_num

                # Get list of all dominos with ends matching round num and move them to options buffer.
                options: list[Domino] = [domino for domino in player.hand if domino.end1_pips == compare_value or domino.end2_pips == compare_value]
                for domino in options:
                    # player.hand.remove(domino)
                    if domino.end2_pips == compare_value:
                        domino.flip()

                print(f"{player.initials}'s hand: {player.hand}")
                cursor.draw_list(player.hand)

                # Continue playing tiles until options becomes zero.
                while options:
                    do_action: bool = True

                    # Only one option, play tile automatically.
                    if len(options) == 1:
                        choice_domino = options[0]
                        sleeprint(f"\nPlayed domino {choice_domino} automatically.\n\n\n\n\n")
                        do_action = False
                    else:...
                        # # Print list of playable dominoes.
                        # print(f"Options: {options}")
                        # cursor.draw_list(options)
                    
                    # Parse command.
                    while do_action:
                        cmd_options = "\n'_-_'\t\t\t- pick a domino [replace underscores with pip values]"
                        cmd_options += "\n'f _-_' | 'f [int]'\t- flip a domino | flip all dominoes matching int"
                        cmd_options += "\n's _-_ _-_'\t\t- swap two dominos in your hand\n"
                        choice_str = input(f"Input command:{cmd_options}\n> ")
                        arg1 = choice_str.split(' ')[0]
                        try:
                            # Pick next domino
                            if '-' in arg1:
                                val1_str, val2_str = arg1.split('-')
                                val1 = int(val1_str)
                                val2 = int(val2_str)
                                choice_domino = Domino(val1, val2)
                                if choice_domino in options:
                                    sleeprint(f"\nPlayed domino {choice_domino}.\n\n\n\n\n")
                                    choice_domino = options[options.index(choice_domino)]
                                    break
                                else:
                                    sleeprint(f"\nERROR: CHOICE NOT LISTED IN OPTIONS.\n\n\n\n\n")
                            # Flip domino
                            elif 'f' in arg1:
                                arg2 = choice_str.split(' ')[1]
                                if '-' in arg2:
                                    val1_str, val2_str = arg2.split('-')
                                    val1 = int(val1_str)
                                    val2 = int(val2_str)
                                    flip_domino = Domino(val1, val2)
                                    if flip_domino in player.hand:
                                        player.hand[player.hand.index(flip_domino)].flip()
                                        print(f"\n\n\n\n\nFlipped domino {flip_domino} in hand.\n")
                                    else:
                                        sleeprint(f"\nERROR: DOMINO NOT LISTED IN HAND.\n\n\n\n\n")
                                else:
                                    value = int(arg2)
                                    flipped: bool = False
                                    for domino in player.hand:
                                        if domino.matches(value):
                                            flipped = True
                                            domino.flip()
                                    if flipped:
                                        print(f"\n\n\n\n\nFlipped all dominos matching {value} in hand.\n")
                                    else:
                                        sleeprint(f"\nERROR: NO DOMINOES IN HAND MATCHING VALUE.\n\n\n\n\n")
                            # Swap two dominoes
                            elif 's' in arg1:
                                arg2 = choice_str.split(' ')[1]
                                arg3 = choice_str.split(' ')[2]
                                dom1_val1_str, dom1_val2_str = arg2.split('-')
                                dom1_val1 = int(dom1_val1_str)
                                dom1_val2 = int(dom1_val2_str)
                                swap_dom1 = Domino(dom1_val1, dom1_val2)
                                dom2_val1_str, dom2_val2_str = arg3.split('-')
                                dom2_val1 = int(dom2_val1_str)
                                dom2_val2 = int(dom2_val2_str)
                                swap_dom2 = Domino(dom2_val1, dom2_val2)
                                if swap_dom1 in player.hand and swap_dom2 in player.hand:
                                    i_dom1 = player.hand.index(swap_dom1)
                                    i_dom2 = player.hand.index(swap_dom2)
                                    player.hand[i_dom1], player.hand[i_dom2] = player.hand[i_dom2], player.hand[i_dom1]
                                    print(f"\n\n\n\n\nSwapped dominoes {swap_dom1} and {swap_dom2} in hand.\n")
                                else:
                                    swap_doms: list[Domino] = [swap_dom1, swap_dom2]
                                    display_doms = [domino for domino in swap_doms if domino not in player.hand]
                                    sleeprint(f"\nERROR: DOMINO(ES) {display_doms} NOT LISTED IN HAND.\n\n\n\n\n")
                            else:
                                raise ValueError
                        except:
                            sleeprint(f"\nERROR: INVALID COMMAND SYNTAX.\n\n\n\n\n")

                        if len(self.branches[i_player].train) == 1:
                            print(f"Middle tile: {self.middle_tile}")
                            cursor.draw_domino(self.middle_tile)
                        else:
                            print(f"Train: {self.branches[i_player].train}")
                            cursor.draw_branch(self.branches[i_player])
                        print(f"Hand: {player.hand}")
                        cursor.draw_list(player.hand)
                        # print(f"Options: {options}")
                        # cursor.draw_list(options)

                    # Add domino to branch and remove from options buffer.
                    self.branches[i_player].add_to_train(choice_domino)
                    player.hand.remove(choice_domino)
                    options.remove(choice_domino)

                    # # Return all dominoes in options buffer to hand.
                    # for domino in options:
                    #     player.hand.append(domino)

                    # Get new compare value
                    if choice_domino.end1_pips == compare_value:
                        new_compare_value: int = choice_domino.end2_pips
                    else:
                        new_compare_value: int = choice_domino.end1_pips

                    # Replace old compare_value
                    compare_value = new_compare_value

                    # Get new list of options for next domino in train and move from hand to options buffer.
                    options = [domino for domino in player.hand if domino.matches(compare_value)]
                    for domino in options:
                        # player.hand.remove(domino)
                        if domino.end2_pips == compare_value:
                            domino.flip()

                    # Draw train and hand to screen
                    print(f"\n\n\n\n\nTrain: {self.branches[i_player].train}")
                    cursor.draw_branch(self.branches[i_player])
                    print(f"Hand: {player.hand}")
                    cursor.draw_list(player.hand)
                else:
                    sleeprint("\nNo options\n\n\n\n\n\n\n\n\n")
            # AI calculates best initial train
            else:
                ...
        
        cursor.draw_branches(self.branches[:constants.AMMT_PLAYERS])
        sleep(constants.SLEEP_TIME)