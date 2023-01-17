
from board import Board
from player import Player


class Game:
    def __init__(self):
        playerOne = input("Player 1 name : ")
        playerTwo = input("Player 2 name : ")
        # TODO : add color choice
        self.player1 = Player(playerOne)
        self.player2 = Player(playerTwo)
        self.board = Board([self.player1.name, self.player2.name])

    def run(self):
        self.board.run()
