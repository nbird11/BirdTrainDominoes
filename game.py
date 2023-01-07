"""Houses the `Game` class."""

import cursor
import constants
from constants import sleeprint
from time import sleep
from domino import Domino
from boneyard import Boneyard
from player import Player
from branch import Branch
from board import Board

class Game:
    """Handles all game actions."""
    def __init__(self) -> None:
        """Constructs a `Game` object"""
        self.ammt_players: int = constants.AMMT_PLAYERS
        self.players: list[Player] = []
        # Create each player, taking amount of AI players into account
        sleeprint(f"\n\n\n\n\n\n\n\n\nGame: Start\n\n\n\n\n\n\n\n\n")
        while True:
            ammt_players_real_str = input(f"How many real players? (1-{self.ammt_players})\n> ")
            try:
                ammt_players_real = int(ammt_players_real_str)
                if 0 <= ammt_players_real <= self.ammt_players:
                    break
                else:
                    sleeprint(f"\nERROR: AMMOUNT OF PLAYERS MUST BE BETWEEN 1 AND {self.ammt_players}.\n")
            except:
                sleeprint(f"\nERROR: AMMOUNT OF PLAYERS MUST BE AN INT (WHOLE NUMBER).\n")
        for i in range(self.ammt_players):
            if ammt_players_real:
                while True:
                    initials = input(f"Input initials for Player {i+1}: (3 characters)\n> ")
                    if len(initials) == 3:
                        break
                    sleeprint("\nERROR: INITIALS MUST BE LENGTH OF 3 CHARACTERS.\n")
                self.players.append(Player(ai=False, id=initials))
                ammt_players_real -= 1
            else:
                ai_num: int = i+1 - int(ammt_players_real_str)
                self.players.append(Player(ai=True, id=f'ai{ai_num}'))
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
        self._initial_trains(self.board)        # TODO AI HARD MODE

        round_over = False

        # One loop constitutes an individual turn.
        while not round_over:
            self._update_turn()
            self._turn()
            if not round_over:
                round_over = not round_over

    def _round_init(self) -> None:
        """Starts the round."""
        # Create new Boneyard with round number tile missing.
        self.boneyard = Boneyard(self.round_num)
        # Deals from the Boneyard
        self._deal(self.boneyard)
        # Creates new Board with round number middle tile and players list.
        self.board = Board(self.round_num, self.players)

    def _deal(self, boneyard: Boneyard) -> None:
        """Deals the tiles from the boneyard. Is called at the beginning of
        each round.
        """
        for _ in range(constants.DEAL_AMMT):
            for player in self.players:
                player.draw(boneyard)

    def _update_turn(self) -> None:
        """Updates the turn cycle to the next player's index in `players` list"""
        self.turn_i += 1
        if self.turn_i >= len(self.players):
            self.turn_i = 0

    def _initial_trains(self, board: Board) -> None:
        """Lets every player add an initial train to their personal branch.
        
        AI players automatically calculate an initial train using the most pips;
        Regular players can choose the dominoes in their initial train.
        """
        sleeprint(f"\n\n\n\n\n\n\n\n\nRound {board.round_num}: Initial trains!\n\n\n\n\n\n\n\n\n")
        for branch in board.branches:
            branch.train.append(board.middle_tile)
        # <Loop through each player to build their train.>
        for i_player, player in enumerate(board.players):
            # <Real player picks their dominoes for train.>
            if not player.ai:
                print(f"Player {i_player+1}: {player.id}")
                print(f"Middle tile: {board.middle_tile}")
                cursor.draw_domino(board.middle_tile)

                # Set initial compare value (which is the round number).
                compare_value: int = board.round_num
                # Get list of all dominos with ends matching compare value.
                options: list[Domino] = [domino for domino in player.hand if domino.matches(compare_value)]

                # Make hand easier to read.
                for domino in player.hand:
                    if domino.end2_pips == compare_value:
                        domino.flip()

                print(f"{player.id}'s hand: {player.hand}")
                cursor.draw_list(player.hand)
                
                # <Continue playing tiles until options becomes zero.>
                while options:
                    do_action: bool = True

                    # Only one option, play tile automatically.
                    if len(options) == 1:
                        choice_domino = options[0]
                        sleeprint(f"\n\n\n\n\nPlayed domino {choice_domino} automatically.\n")
                        do_action = False
                    # # Print list of playable dominoes.
                    # else:
                    #     print(f"Options: {options}")
                    #     cursor.draw_list(options)
                    
                    # Parse command / get choice domino.
                    while do_action:
                        cmd_options = "\n'_-_'\t\t- pick a domino [replace underscores with pip values]"
                        cmd_options += "\n'f _-_'\t\t- flip a domino"
                        cmd_options += "\n's _-_ _-_'\t- swap two dominos in your hand\n"
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
                                    sleeprint(f"\n\n\n\n\nPlayed domino {choice_domino}.\n")
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
                            # Auto pick domino.
                            elif 'auto' in arg1:
                                # EASY PICK.
                                choice_domino = options[0]
                                sleeprint(f"\n\n\n\n\nAutomatically played domino {choice_domino}.\n", .5)
                                break
                            else:
                                raise ValueError
                        except:
                            sleeprint(f"\nERROR: INVALID COMMAND SYNTAX.\n\n\n\n\n")

                        if len(board.branches[i_player].train) == 1:
                            print(f"Middle tile: {board.middle_tile}")
                            cursor.draw_domino(board.middle_tile)
                        else:
                            print(f"Train: {board.branches[i_player].train}")
                            cursor.draw_branch(board.branches[i_player])
                        print(f"Hand: {player.hand}")
                        cursor.draw_list(player.hand)
                        # print(f"Options: {options}")
                        # cursor.draw_list(options)

                    # Add domino to branch and remove from hand.
                    board.branches[i_player].add_to_train(choice_domino)
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
                    # Reset options
                    options: list[Domino] = [domino for domino in player.hand if domino.matches(compare_value)]

                    # Make hand easier to read.
                    for domino in player.hand:
                        if domino.end2_pips == compare_value:
                            domino.flip()

                    # Draw train and hand to screen
                    print(f"\n\n\n\n\nTrain: {board.branches[i_player].train}")
                    cursor.draw_branch(board.branches[i_player])
                    print(f"Hand: {player.hand}")
                    cursor.draw_list(player.hand)
                # </Continue playing tiles until options becomes zero./>
                else:
                    if board.branches[i_player].train[len(board.branches[i_player].train)-1] == board.middle_tile:
                        sleeprint(f"\nNo options\n\n\n\n\n\n\n\n\n")
                        board.branches[i_player].toggle_train_on()
                    else:
                        sleeprint(f"\nNo more options\n\n\n\n\n")
            # </Real player picks their dominoes from options list./>

            # <AI calculates train.>
            else:
                print(f"Player {i_player+1}: {player.id}")
                # Set initial compare value (which is the round number).
                compare_value: int = board.round_num
                # Get list of all dominos with ends matching compare value.
                options: list[Domino] = [domino for domino in player.hand if domino.matches(compare_value)]

                for domino in player.hand:
                    if domino.end2_pips == compare_value:
                        domino.flip()

                # <Continue playing tiles until options becomes zero.>
                while options:
                    do_action: bool = True
                    
                    # Only one option, play tile automatically.
                    if len(options) == 1:
                        choice_domino = options[0]
                        do_action = False

                    # Get choice
                    while do_action:
                        # RANDOM MODE AI: Just picks the first option for every tile.
                        choice_domino = options[0]
                        break

                        # HARD MODE AI: Pick dominoes to give the longest/most-pips train.
                        # TODO
                    
                    # Add domino to branch and remove from options buffer.
                    board.branches[i_player].add_to_train(choice_domino)
                    player.hand.remove(choice_domino)
                    options.remove(choice_domino)

                    # Get new compare value
                    if choice_domino.end1_pips == compare_value:
                        new_compare_value: int = choice_domino.end2_pips
                    else:
                        new_compare_value: int = choice_domino.end1_pips

                    # Replace old compare_value
                    compare_value = new_compare_value
                    # Reset options
                    options: list[Domino] = [domino for domino in player.hand if domino.matches(compare_value)]

                    for domino in player.hand:
                        if domino.end2_pips == compare_value:
                            domino.flip()
                # </Continue playing tiles until options becomes zero./>
                else:
                    if board.branches[i_player].train[len(board.branches[i_player].train)-1] == board.middle_tile:
                        sleeprint(f"\nNo options\n\n\n\n\n\n\n\n\n")
                        board.branches[i_player].toggle_train_on()
                    else:
                        sleeprint(f"\nNo more options\n\n\n\n\n\n\n\n\n")
            # </AI calculates train./>
        # </Loop through each player to build their train./>
        print(f"\n\n\n\n\nAll Players' Trains:\n")
        cursor.draw_branches(board.branches[:constants.AMMT_PLAYERS])
        sleep(constants.SLEEP_TIME)

    def _turn(self) -> None:
        """All actions comprising one player's turn."""

        cur_player = self.players[self.turn_i]

        # Display all branches
        print(f"\n\n\n\n\n\n\n\n\n\nBoard:\n")
        cursor.draw_branches(self.board.branches)
        sleep(constants.SLEEP_TIME)
        sleeprint(f"\nPlayer {self.turn_i+1}: {self.players[self.turn_i].id}'s Turn\n")

        # Get play options
        branch_ends: list[tuple[Domino, str] | Domino] = []
        for branch in self.board.branches:
            # print(f"\n\nbranch={branch}")
            end_domino = branch.train[len(branch.train)-1]
            if branch.player:
                # print(f"branch has player")
                # print(f"branch == self.board.branches[self.turn_i]={branch == self.board.branches[self.turn_i]}")
                # print(f"not branch.train_on={not branch.train_on}")
                if branch == self.board.branches[self.turn_i] or not branch.train_on:
                    # print(f"appending domino {end_domino} w/ initials {branch.player.initials}")
                    branch_ends.append((end_domino, branch.player.id))
            else:
                # print(f"appending domino {end_domino}")
                if end_domino not in branch_ends: branch_ends.append(end_domino)
        print(f"branch_ends={branch_ends}")

        options: list[Domino] = []
        for domino in cur_player.hand:
            for item in branch_ends:
                value: int
                if type(item) == tuple:
                    value = item[0].end2_pips
                else:
                    value = item.end2_pips
            if domino.matches(value):
                if domino.end2_pips == value:
                    domino.flip()
                options.append(domino)


        print(f"{cur_player.id}'s hand: {cur_player.hand}")
        cursor.draw_list(cur_player.hand)

        # print(f"Options: {options}")
        # if options: cursor.draw_list(options)

        # <Real player make move.>
        if not cur_player.ai:
            # Parse command.
            while True:
                cmd_options = "\n'_-_ _-_ [player_id]'\t- play first domino on second domino - add player_id if playing on another player's branch"
                cmd_options += "\n'f _-_'\t\t\t- flip a domino in hand"
                cmd_options += "\n's _-_ _-_'\t\t- swap two dominos in hand\n"
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
                            sleeprint(f"\n\n\n\n\nPlayed domino {choice_domino}.\n")
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
                            if flip_domino in cur_player.hand:
                                cur_player.hand[cur_player.hand.index(flip_domino)].flip()
                                print(f"\n\n\n\n\nFlipped domino {flip_domino} in hand.\n")
                            else:
                                sleeprint(f"\nERROR: DOMINO NOT LISTED IN HAND.\n\n\n\n\n")
                        else:
                            value = int(arg2)
                            flipped: bool = False
                            for domino in cur_player.hand:
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
                        if swap_dom1 in cur_player.hand and swap_dom2 in cur_player.hand:
                            i_dom1 = cur_player.hand.index(swap_dom1)
                            i_dom2 = cur_player.hand.index(swap_dom2)
                            cur_player.hand[i_dom1], cur_player.hand[i_dom2] = cur_player.hand[i_dom2], cur_player.hand[i_dom1]
                            print(f"\n\n\n\n\nSwapped dominoes {swap_dom1} and {swap_dom2} in hand.\n")
                        else:
                            swap_doms: list[Domino] = [swap_dom1, swap_dom2]
                            display_doms = [domino for domino in swap_doms if domino not in cur_player.hand]
                            sleeprint(f"\nERROR: DOMINO(ES) {display_doms} NOT LISTED IN HAND.\n\n\n\n\n")
                    # Auto pick domino.
                    elif 'auto' in arg1:
                        # EASY PICK.
                        choice_domino = options[0]
                        sleeprint(f"\n\n\n\n\nAutomatically played domino {choice_domino}.\n", .5)
                        break
                    else:
                        raise ValueError
                except:
                    sleeprint(f"\nERROR: INVALID COMMAND SYNTAX.\n\n\n\n\n")
        # <AI make move.>
        else:...
                





        # if no_possible_moves              # TODO
        #    draw_tile()                    # TODO
        #    update_DrawPile()              # TODO
        #    if can_play                    # TODO
        #       play_tile()                 # TODO
        # else                              # TODO
        #    choose_move() ~                # TODO