import pygame

pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))
color = 0

w, h = width // 3, height // 3
grid = [['' for j in range(3)] for i in range(3)]
ai, human = 'X', 'O'
current_player = ai
available = [(i, j) for i in range(3) for j in range(3)]


def minimax(board: list, depth: int, is_maximizing: bool):
    # alpha beta pruning in future updates
    scores = {'X': 10, 'O': -10, 'Tie': 0}      # defining the scores for each player

    if game_over():
        return scores[game_over()]              # base case

    if is_maximizing:
        best_score = -20

        for i in range(3):
            for j in range(3):
                if board[i][j] == '':       # checking if the spot is available
                    board[i][j] = ai        # simulating its play
                    score = minimax(board, depth + 1, False)
                    if score == 20:         # don't know why but sometimes the score gets 20
                        score = 0
                    board[i][j] = ''        # returning to the previous value
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 20                     # same :P

        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = human
                    score = minimax(board, depth + 1, True)
                    if score == 20:
                        score = 0
                    board[i][j] = ''
                    best_score = min(score, best_score)

        return best_score


def make_a_move():                  # calculating the best move for ai
    global grid, current_player
    best_score = -20
    for i in range(3):
        for j in range(3):
            if grid[i][j] == '':
                grid[i][j] = ai
                score = minimax(grid, 0, False)
                grid[i][j] = ''
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    grid[best_move[0]][best_move[1]] = ai
    current_player = human
    available.remove(best_move)


def game_over():
    winner = None
    for i in range(3):
        if grid[i][2] != '' and grid[i][0] == grid[i][1] == grid[i][2]:     # horizontal
            winner = grid[i][0]
        elif grid[0][i] != '' and grid[0][i] == grid[1][i] == grid[2][i]:   # vertical
            winner = grid[0][i]

    if grid[2][2] != '' and grid[0][0] == grid[1][1] == grid[2][2]:
        winner = grid[0][0]                                                 # diagonal
    elif grid[0][2] != '' and grid[0][2] == grid[1][1] == grid[2][0]:
        winner = grid[0][2]

    if len(available) == 0 and not winner:
        winner = 'Tie'

    return winner


FPS = 60
make_a_move()

clock = pygame.time.Clock()
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_player == human:             # human turn
                j, i = pygame.mouse.get_pos()
                i //= h
                j //= w
                if grid[i][j] == '':                # checking if the spot is available
                    grid[i][j] = human
                    available.remove((i, j))
                    make_a_move()

    pygame.draw.line(screen, color, (0, h), (width, h), 5)
    pygame.draw.line(screen, color, (0, h * 2), (width, h * 2), 5)      # drawing the board
    pygame.draw.line(screen, color, (w, 0), (w, height), 5)
    pygame.draw.line(screen, color, (w * 2, 0), (w * 2, height), 5)

    for i in range(3):
        for j in range(3):
            x = w * j + w // 2
            y = h * i + h // 2
            if grid[i][j] == ai:        # drawing the X
                pygame.draw.line(screen, color, [x - w // 3, y - h // 3], [x + w // 3, y + h // 3], 7)
                pygame.draw.line(screen, color, [x - w // 3, y + h // 3], [x + w // 3, y - h // 3], 7)
            elif grid[i][j] == human:   # drawing the O
                pygame.draw.circle(screen, color, (x, y), w // 3, 7)

    if game_over():
        print(game_over())
        break

    pygame.display.update()
