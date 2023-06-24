from cmath import inf
import pygame
from board import Board
pygame.init()

WIDTH = 500-8
HEIGHT = 650-8
#Home page
home_screen = pygame.display.set_mode((WIDTH, HEIGHT))
avatar_img1 = pygame.image.load("human.png")
avatar_img2 = pygame.image.load("ai.png")
avatar_img1 = pygame.transform.scale(avatar_img1, (200, 200))
avatar_img2 = pygame.transform.scale(avatar_img2, (200, 250))
avatar_rect1 = avatar_img1.get_rect(left=10, top=140)
avatar_rect2 = avatar_img2.get_rect(left=300, top=130)
start_button_font = pygame.font.SysFont('Times New Roman', 40,bold=True)
start_button_text = start_button_font.render('Start Game', True, (255, 99,100))
start_button_text1 = start_button_font.render('Exit', True, (255, 255,255))
start_button_rect = start_button_text.get_rect(left=160,top=400)
start_button_rect1 = start_button_text1.get_rect(left=220,top=450)
score_font = pygame.font.SysFont('Times New Roman', 40,bold=True)
Home_text = score_font.render(f"Make Square", True, (255, 255, 255))
HomeText_rect = Home_text.get_rect(left=150, top=20)
Home_text2 = score_font.render(f"VS", True, (255, 255, 0))
HomeText_rect2 = Home_text2.get_rect(left=WIDTH//2, top=250)
#game screen var
game_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Make Square')
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Make Square')
clock = pygame.time.Clock()

player = 0
playersigns = {
    0: 'H',     # Human 
    1: 'A'      # AI
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
        avatar_img1 = pygame.image.load("human.png")
        avatar_img2 = pygame.image.load("ai.png")
        avatar_img1 = pygame.transform.scale(avatar_img1, (100, 100))
        avatar_img2 = pygame.transform.scale(avatar_img2, (110, 125))
        avatar_rect1 = avatar_img1.get_rect(left=65, top=535)
        avatar_rect2 = avatar_img2.get_rect(left=320, top=525)
        screen.blit(avatar_img1, avatar_rect1)
        screen.blit(avatar_img2, avatar_rect2)
        pygame.draw.line(screen, (255, 99, 71), (WIDTH//2, 520), (WIDTH//2, 626), 3)
        score_font = pygame.font.SysFont('Times New Roman', 24,bold=True)
        player1_score_text = score_font.render(f"Player: {playerscores[0]}", True, (255, 255, 255))
        player2_score_text = score_font.render(f"AI: {playerscores[1]}", True, (255, 255, 255))
        score_rect1 = player1_score_text.get_rect(left=80, top=500)
        score_rect2 = player2_score_text.get_rect(left=350, top=500)
        screen.blit(player1_score_text, score_rect1)
        screen.blit(player2_score_text, score_rect2)
        pygame.display.update()
    else:
        avatar_img1 = pygame.image.load("human.png")
        avatar_img2 = pygame.image.load("ai.png")
        avatar_img1 = pygame.transform.scale(avatar_img1, (100, 100))
        avatar_img2 = pygame.transform.scale(avatar_img2, (110, 125))
        avatar_rect1 = avatar_img1.get_rect(left=65, top=535)
        avatar_rect2 = avatar_img2.get_rect(left=320, top=525)
        screen.blit(avatar_img1, avatar_rect1)
        screen.blit(avatar_img2, avatar_rect2)
        pygame.draw.line(screen, (255, 99, 71), (WIDTH//2, 520), (WIDTH//2, 626), 3)
        score_font = pygame.font.SysFont('Times New Roman', 24,bold=True)
        player1_score_text = score_font.render(f"Player: {playerscores[0]-playerscores[0]}", True, (255, 255, 255))
        player2_score_text = score_font.render(f"AI: {playerscores[1]-playerscores[1]}", True, (255, 255, 255))
        score_rect1 = player1_score_text.get_rect(left=80, top=500)
        score_rect2 = player2_score_text.get_rect(left=350, top=500)
        screen.blit(player1_score_text, score_rect1)
        screen.blit(player2_score_text, score_rect2)
        pygame.display.update()

def game_over():
    '''
    Checks if there's a winner or all cells of the board are filled: True
    Otherwise: False
    '''
    global player, playerscores, checked_winners, colors
    if Board.all_filled(board.board):
        print('\nFinal score:')
        print(f'Player {playerscores[0]}')
        print(f'AI {playerscores[1]}', end='\n\n')

        winner = None
        if playerscores[0] == playerscores[1]:
            print('\nDraw!')
        elif playerscores[0] > playerscores[1]:
            print('\nPlayer won!')
            winner = 'Player'
        else:
            print('\nAI won!')
            winner = 'AI'

        # Display winner and scores on a new screen
        display_winner(winner)
        pygame.time.delay(3000)
        board.clear()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        board.draw(screen, checked_winners, colors)
        pygame.display.update()
        update_scores(1)
        player = 0
        playerscores = {
            0: 0,
            1: 0
        }
        
        checked_winners = [[False for _ in range(board.size)] for _ in range(board.size)]
        return True

    return False


def display_winner(winner):
    # Create a new screen for displaying the winner
    winner_screen = pygame.display.set_mode((400, 400))
    winner_screen.fill((51, 51, 51))
    font = pygame.font.SysFont('arial', 30)
    text = font.render(f"{winner} wins!", True, (255, 255, 255))
    text_rect = text.get_rect(left=135, top=80)
    if winner == 'AI':
        avatar_img = pygame.image.load("ai.png")
    elif winner == 'Player':
        avatar_img = pygame.image.load("human.png")
    else:
        avatar_img = pygame.image.load("draw.png")
    avatar_img = pygame.transform.scale(avatar_img, (150, 150))
    avatar_rect = avatar_img.get_rect(left=125, top=120)
    winner_screen.blit(avatar_img, avatar_rect)

    # Render player scores
    score_font = pygame.font.SysFont('arial', 24)
    player1_score_text = score_font.render(f"Player: {playerscores[0]}", True, (255, 255, 255))
    player2_score_text = score_font.render(f"AI: {playerscores[1]}", True, (255, 255, 255))
    score_rect1 = player1_score_text.get_rect(left=150, top=300)
    score_rect2 = player2_score_text.get_rect(left=170, top=340)
    winner_screen.blit(player1_score_text, score_rect1)
    winner_screen.blit(player2_score_text, score_rect2)

    winner_screen.blit(text, text_rect)
    pygame.display.flip()
def check_winner():
    global board, winner_checked, playersigns, playerscores, colors
    winner, cells = Board.check_winner(board.board, checked_winners, playersigns)
    if winner != None:
        playerscores[winner] += 1
        update_scores()

        print(f'Player {playerscores[0]}')
        print(f'AI {playerscores[1]}', end='\n\n')
        
        board.draw(screen, checked_winners, colors)
        board.draw_line(screen, cells[0], cells[2], colors[winner])
        board.draw_line(screen, cells[2], cells[3], colors[winner])
        board.draw_line(screen, cells[3], cells[1], colors[winner])
        board.draw_line(screen, cells[1], cells[0], colors[winner])
        pygame.display.update()
        pygame.time.delay(500)

        for i, j in cells:
            checked_winners[i][j] = True

def minimax(board, depth, alpha, beta, maximizing_player):
    '''
    maximizing player: AI
    '''
    global playersigns, checked_winners
    scores = {
        0: -1,      # Human
        1: +1       #AI
    }
    winner, _ =  Board.check_winner(board, checked_winners, playersigns)
    if winner != None:
        return scores[winner]
    elif Board.all_filled(board) or depth == 0:
        return 0

    if maximizing_player:
        max_eval = -inf
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ' ':
                    board[i][j] = playersigns[1]
                    eval = minimax(board, depth-1, alpha, beta, maximizing_player=False)
                    board[i][j] = ' '
                    max_eval = max(eval, max_eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = inf
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ' ':
                    board[i][j] = playersigns[0]
                    eval = minimax(board, depth-1, alpha, beta, maximizing_player=True)
                    board[i][j] = ' '
                    min_eval = min(eval, min_eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def get_ai_move(board):
    max_score = -inf
    best_move = None
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ' ':
                board[i][j] = playersigns[1]    # Turn for AI
                score = minimax(board, 4, +inf, -inf, False) # Turn for Player
                board[i][j] = ' '
                print(score,max_score)
                if score > max_score:
                    max_score = score
                    #print(max_score)
                    best_move = i, j
    return best_move

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if start_button_rect.collidepoint(event.pos):
                    # Start button clicked, transition to game screen
                    running = False
                    break
    home_screen.fill((51, 51, 51))
    pygame.draw.rect(home_screen, (51, 51, 51), start_button_rect)
    home_screen.blit(Home_text,HomeText_rect)
    home_screen.blit(avatar_img1,avatar_rect1)
    home_screen.blit(avatar_img2,avatar_rect2)
    home_screen.blit(Home_text2,HomeText_rect2)
    home_screen.blit(start_button_text, start_button_rect)
    home_screen.blit(start_button_text1, start_button_rect1)
    pygame.display.update()
board.draw(screen, checked_winners, colors)
pygame.display.update()
while True:
    # Set refresh rate
    clock.tick(60)

    # Event Listener
    for event in pygame.event.get():
        # If cross button event is triggered
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            #print(pos)
            
            # Player's move
            if board.update(i=pos[1] // (WIDTH // board.size), j=pos[0] // ((HEIGHT-150) // board.size), player=player):
                check_winner()

                board.draw(screen, checked_winners, colors)
                pygame.display.update()
                
                if game_over():
                    continue
                update_scores()
                
                # AI's move
                player = (player + 1) % 2
                cell = get_ai_move(board.board)

                board.update(i=cell[0], j=cell[1], player=player)
                check_winner()

                board.draw(screen, checked_winners, colors)
                pygame.display.update()
                update_scores()
                
                # Player's move
                player = (player + 1) % 2
                game_over()
    pygame.display.update()