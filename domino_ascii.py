from bird_train import Boneyard, Domino, Game

MAX_ASCII_BRANCH_LEN = 12

def main():
    game = Game()
    game.gameloop()

    for branch in game.board.branches[:4]:
        branch_cursor = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ]

        if len(branch.train) > MAX_ASCII_BRANCH_LEN:
            for domino in branch.train[len(branch.train)-MAX_ASCII_BRANCH_LEN:len(branch.train)]:
                branch_cursor = domino.add_ascii_to_cursor(branch_cursor)
        else:
            for domino in branch.train:
                branch_cursor = domino.add_ascii_to_cursor(branch_cursor)
        
        for row in branch_cursor:
            print(row)


if __name__ == '__main__':
    main()