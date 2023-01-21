from constants import *
import pygame
import os
import sys
pygame.font.init()


class Graphics:
    def __init__(self, board):
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Puissance4")
        self.BACKGROUD = pygame.transform.scale(pygame.image.load(
            os.path.join("assets", "background.png")), (WIDTH, HEIGHT))
        self.board = board

    def draw_winner(self, winner, players):
        color = RED if winner == 1 else YELLOW
        if winner == 1:
            winner = players[0]
        else:
            winner = players[1]
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
                if self.board.board[row][col] == 1:
                    pygame.draw.circle(
                        self.WIN, RED, (137 + 61 * col + 30, 84 + 51 * row + 25), 20)
                elif self.board.board[row][col] == 2:
                    pygame.draw.circle(
                        self.WIN, YELLOW, (137 + 61 * col + 30, 84 + 51 * row + 25), 20)

    def draw_current_player_circle(self):
        x = pygame.mouse.get_pos()[0]
        # making sure the circle is in the board limits
        if x < 137:
            x = 137
        elif x > 137 + 61 * 7:
            x = 137 + 61 * 7

        if self.board.player == 1:
            pygame.draw.circle(self.WIN, RED, (x, 50), 20)
        else:
            pygame.draw.circle(self.WIN, YELLOW, (x, 50), 20)

    def draw_window(self):
        self.WIN.fill(WHITE)
        self.WIN.blit(self.BACKGROUD, (0, 0))
        self.draw_circles()
        self.draw_current_player_circle()
        pygame.display.update()

    def drow_draw(self):
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(f"Draw!", 1, BLACK)
        # make the text under the board
        self.WIN.blit(text, (WIDTH//2 - text.get_width() //
                             2, 380))
        pygame.display.update()
        pygame.time.delay(3000)

    def reset_board(self, board):
        self.board.board = board
        self.draw_window()
