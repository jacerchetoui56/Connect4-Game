from constants import *
import pygame
import os
import sys
from graphics import Graphics
pygame.font.init()


class Board:
    def __init__(self, players):
        self.board = [[0 for i in range(7)] for j in range(6)]
        self.players = players[:]
        self.player = 1
        self.winner = 0
        self.game_over = False
        self.graphics = Graphics(self)

    def get_lowest_empty_row(self, col):
        for row in range(5, -1, -1):
            if self.board[row][col] == 0:
                return row
        return -1

    def get_coloumn(self, x):
        col = (x - 137) // 61
        if col > 6:
            col = 6
        elif col < 0:
            col = 0
        return col

    def check_draw(self):
        for col in range(7):
            if self.board[0][col] == 0:
                return False
        return True

    def check_winner(self):
        # check for horizontal
        for row in range(6):
            for col in range(4):
                if self.board[row][col] == self.board[row][col + 1] == self.board[row][col + 2] == self.board[row][col + 3] and self.board[row][col] != 0:
                    return self.board[row][col]

        # check for vertical
        for row in range(3):
            for col in range(7):
                if self.board[row][col] == self.board[row + 1][col] == self.board[row + 2][col] == self.board[row + 3][col] and self.board[row][col] != 0:
                    return self.board[row][col]

        # check for positive diagonal
        for row in range(3):
            for col in range(4):
                if self.board[row][col] == self.board[row + 1][col + 1] == self.board[row + 2][col + 2] == self.board[row + 3][col + 3] and self.board[row][col] != 0:
                    return self.board[row][col]

        # check for negative diagonal
        for row in range(3, 6):
            for col in range(4):
                if self.board[row][col] == self.board[row - 1][col + 1] == self.board[row - 2][col + 2] == self.board[row - 3][col + 3] and self.board[row][col] != 0:
                    return self.board[row][col]
        return 0

    def reset_board(self):
        self.board = [[0 for i in range(7)] for j in range(6)]
        self.graphics.reset_board(self.board)
        self.player = 1
        self.winner = 0
        self.game_over = False

    def run(self):
        while True:
            self.graphics.draw_window()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.game_over:
                        x = event.pos[0]
                        col = self.get_coloumn(x)
                        row = self.get_lowest_empty_row(col)
                        if row != -1:
                            self.board[row][col] = self.player
                            self.winner = self.check_winner()
                            if self.winner != 0:
                                self.graphics.draw_window()
                                self.graphics.draw_winner(
                                    self.winner, self.players)
                                self.game_over = True
                                self.reset_board()
                            elif self.check_draw():
                                self.graphics.draw_window()
                                self.graphics.drow_draw()
                                self.game_over = True
                                self.reset_board()
                            self.player = 2 if self.player == 1 else 1
        self.run()
