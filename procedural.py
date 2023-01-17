import pygame
import os
pygame.font.init()

WIDTH, HEIGHT = 700, 450

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# giving the window a title
pygame.display.set_caption("Puissance4")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
FPS = 60


# to get the lowest empty row we will use a function

BACKGROUD = pygame.transform.scale(pygame.image.load(
    os.path.join("assets", "background.png")), (WIDTH, HEIGHT))


def get_lowest_empty_row(board, col):
    for row in range(5, -1, -1):
        if board[row][col] == 0:
            return row
    return -1


def get_coloumn(x):  # based pn the x position of the mouse click
    # since the board starts at the x = 137 and the single grid is 61 width
    col = (x - 137) // 61
    # checking that the col is in the range
    if col > 6:
        col = 6
    elif col < 0:
        col = 0
    return col


# check for the winner
def check_winner(board):
    # check for horizontal
    for row in range(6):
        for col in range(4):
            if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] and board[row][col] != 0:
                return board[row][col]

    # check for vertical
    for row in range(3):
        for col in range(7):
            if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] and board[row][col] != 0:
                return board[row][col]

    # check for positive diagonal
    for row in range(3):
        for col in range(4):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] and board[row][col] != 0:
                return board[row][col]

    # check for negative diagonal
    for row in range(3, 6):
        for col in range(4):
            if board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3] and board[row][col] != 0:
                return board[row][col]

    return 0

# drawing the winner to the screen


def draw_winner(winner):
    color = RED
    if winner == 1:
        winner_text = "Yellow wins"
        color = YELLOW
    elif winner == 2:
        winner_text = "Red wins"
    else:
        winner_text = "Tie"
    font = pygame.font.SysFont("comicsans", 50)
    text = font.render(winner_text, True, color)
    WIN.blit(text, (WIDTH//2 - text.get_width() //
             2, 380))
    pygame.display.update()
    pygame.time.delay(3000)


def draw_circles(board):
    for row in range(6):
        for col in range(7):
            if board[row][col] == 1:
                pygame.draw.circle(
                    WIN, YELLOW, (137 + 61 * col + 30, 84 + 51 * row + 25), 20)
            elif board[row][col] == 2:
                pygame.draw.circle(
                    WIN, RED, (137 + 61 * col + 30, 84 + 51 * row + 25), 20)
    pygame.display.update()

# a function to follow the mouse with the circle of the current player


def current_player_circle(TURN):
    x = pygame.mouse.get_pos()[0]
    # making sure the circle is in the board limits
    if x < 137:
        x = 137
    elif x > 137 + 61 * 7:
        x = 137 + 61 * 7

    # drawing the circle
    if TURN == 1:
        pygame.draw.circle(WIN, YELLOW, (x, 50), 20)
    elif TURN == 2:
        pygame.draw.circle(WIN, RED, (x, 50), 20)
    pygame.display.update()


def draw_window(BOARD, TURN):
    WIN.fill(WHITE)
    WIN.blit(BACKGROUD, (0, 0))
    draw_circles(BOARD)
    current_player_circle(TURN)
    pygame.display.update()


def main():
    # handling the players
    TURN = 1  # it can be 1 or 2 => 1 for yellow and 2 for red
    # making the board
    BOARD = [[0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]]
    # here is how the board will behave
    #  if an element is 0 it means that it is empty
    #  if an element is 1 it means that it is yellow
    #  if an element is 2 it means that it is red
    # the clock is used to control the fps
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)  # ? this is to make sure that the game runs at 60 fps
        # handling quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            # get the x and y of the mouse when it clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                selected_col = get_coloumn(x)
                lowes_empty_row = get_lowest_empty_row(BOARD, selected_col)
                # skipping if the column is full
                if (lowes_empty_row == -1):
                    continue
                BOARD[lowes_empty_row][selected_col] = TURN
                # checking for the winner
                winner = check_winner(BOARD)
                if winner != 0:
                    draw_window(BOARD, TURN)  # drawing the last circle
                    draw_winner(winner)
                    run = False
                    break
                # the other player will play now
                TURN = 2 if TURN == 1 else 1

            # getting the current position of the mouse to draw the circle of the current player

        draw_window(BOARD, TURN)
    main()


if __name__ == "__main__":
    main()

# making the code above with classes : OOP
# in this game we will have 4 classes : Board, Player, Game and Main
