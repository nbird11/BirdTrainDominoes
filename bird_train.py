"""Bird house-rules version of Mexican Train Dominoes.

AI players will calculate the best move based on all possible move options.
"""

from game import Game

def main():
    """Runs the game."""
    game = Game()
    game.gameloop()


if __name__ == '__main__':
    main()