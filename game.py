
from board import Board
from player import Player
# these modules are used to make the input colored
from colorama import init
init()

YELLOW = "\x1b[1;33;40m"
RED = "\x1b[1;31;40m"


class Game:
    def __init__(self):
        # making the input colored
        print(f"\n{RED}Player 1 name : ", end='')
        playerOne = input()
        print(f"\n{YELLOW}Player 2 name : ", end='')
        playerTwo = input()
        # TODO : add color choice
        self.player1 = Player(playerOne)
        self.player2 = Player(playerTwo)
        self.board = Board([self.player1.name, self.player2.name])

    def run(self):
        self.board.run()
