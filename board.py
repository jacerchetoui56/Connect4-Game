from constants import *
import pygame
import os
import sys
pygame.font.init()


class Board:
    def __init__(self, players):
        self.board = [[0 for i in range(7)] for j in range(6)]
        self.players = players[:]
        self.player = 1
        self.winner = 0
        self.game_over = False
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Puissance4")
        self.BACKGROUD = pygame.transform.scale(pygame.image.load(
            os.path.join("assets", "background.png")), (WIDTH, HEIGHT))

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

    def draw_winner(self):
        color = RED if self.winner == 1 else YELLOW
        if self.winner == 1:
            winner = self.players[0]
        else:
            winner = self.players[1]
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(f"{winner} wins!", 1, color)
        # make the text under the board
        self.WIN.blit(text, (WIDTH//2 - text.get_width() //
                             2, 380))
        pygame.display.update()
        pygame.time.delay(3000)

    def draw_circles(self):
        for row in range(6):
            for col in range(7):
                if self.board[row][col] == 1:
                    pygame.draw.circle(
                        self.WIN, RED, (137 + 61 * col + 30, 84 + 51 * row + 25), 20)
                elif self.board[row][col] == 2:
                    pygame.draw.circle(
                        self.WIN, YELLOW, (137 + 61 * col + 30, 84 + 51 * row + 25), 20)

    def current_player_circle(self):
        x = pygame.mouse.get_pos()[0]
        # making sure the circle is in the board limits
        if x < 137:
            x = 137
        elif x > 137 + 61 * 6:
            x = 137 + 61 * 6

        if self.player == 1:
            pygame.draw.circle(self.WIN, RED, (x, 50), 20)
        else:
            pygame.draw.circle(self.WIN, YELLOW, (x, 50), 20)

    def draw_window(self):
        self.WIN.fill(WHITE)
        self.WIN.blit(self.BACKGROUD, (0, 0))
        self.draw_circles()
        self.current_player_circle()
        pygame.display.update()

    def reset_board(self):
        self.board = [[0 for i in range(7)] for j in range(6)]
        self.player = 1
        self.winner = 0
        self.game_over = False

    def run(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(FPS)
            self.draw_window()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.game_over:
                        col = self.get_coloumn(pygame.mouse.get_pos()[0])
                        row = self.get_lowest_empty_row(col)
                        if row != -1:
                            self.board[row][col] = self.player
                            self.winner = self.check_winner()
                            if self.winner != 0:
                                self.draw_window()
                                self.game_over = True
                                self.draw_winner()
                                self.reset_board()
                                break
                            if self.player == 1:
                                self.player = 2
                            else:
                                self.player = 1
        # the game will always replay
        self.run()
