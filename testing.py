import constants
import cursor
from board import Board
from boneyard import Boneyard
from domino import Domino
from player import Player


def main():
    boneyard = Boneyard(12)
    board = Board(12, [Player(False), Player(False), Player(True), Player(True)])
    print(board)
    print(boneyard)
    for _ in range(5):
        for player in board.players:
            player.draw(boneyard)

    for branch in board.branches:
        branch.train.append(board.middle_tile)
        for player in board.players:
            for domino in player.hand:
                branch.train.append(domino)
    cursor.draw_branches(board.branches)


if __name__ == '__main__':
    main()