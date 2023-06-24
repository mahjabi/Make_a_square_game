from cmath import inf
import pygame
from board import Board

pygame.init()

WIDTH = 500 - 8
HEIGHT = 650 - 8

# Home page variables
home_screen = pygame.display.set_mode((WIDTH, HEIGHT))
start_button_rect = pygame.Rect(200, 300, 100, 50)

# Game screen variables
game_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Make Square')
clock = pygame.time.Clock()

player = 0
playersigns = {
    0: 'H',  # Human
    1: 'A'  # AI
}

playerscores = {
    0: 0,
    1: 0
}

colors = {
    0: (255, 255, 255),
    1: (255, 99, 71)
}

board = Board(playersigns=playersigns)
checked_winners = [[False for _ in range(board.size)] for _ in range(board.size)]


def update_scores(gaO=0):
    # Render player scores
    if gaO == 0:
        # ... existing code for rendering scores
    else:
        # ... existing code for rendering scores


def game_over():
    # ... existing code for game over and displaying the winner


def display_winner(winner):
    # ... existing code for displaying the winner


def check_winner():
    # ... existing code for checking the winner


def minimax(board, depth, alpha, beta, maximizing_player):
    # ... existing code for the minimax algorithm


def get_ai_move(board):
    # ... existing code for getting AI move


# Home page loop
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if start_button_rect.collidepoint(event.pos):
                    # Start button clicked, transition to game screen
                    running = False
                    break

    home_screen.fill((51, 51, 51))
    pygame.draw.rect(home_screen, (255, 255, 255), start_button_rect)
    pygame.display.update()

# Game loop
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # ... existing code for player and AI moves

            pygame.display.update()
