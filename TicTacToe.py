import pygame
import math

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("tic tac toe")
myfont = pygame.font.SysFont('Arial', 60)

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

Players = [1, 2]

def drawPlayField():
    pygame.draw.rect(screen, pygame.Color(0, 0, 0), (0, 198, 600, 4))
    pygame.draw.rect(screen, pygame.Color(0, 0, 0), (0, 398, 600, 4))
    pygame.draw.rect(screen, pygame.Color(0, 0, 0), (198, 0, 4, 600))
    pygame.draw.rect(screen, pygame.Color(0, 0, 0), (398, 0, 4, 600))

def drawBoard():
    for i in range(3):
        for j in range(3):
            if board[j][i] == 1:
                pygame.draw.line(screen, pygame.Color(0, 0, 0), (i * 200 + 20, j * 200 + 20), ((i * 200 + 180, j * 200 + 180)))
                pygame.draw.line(screen, pygame.Color(0, 0, 0), (i * 200 + 180, j * 200 + 20), ((i * 200 + 20, j * 200 + 180)))
            if board[j][i] == 2:
                pygame.draw.circle(screen, pygame.Color(0, 0, 0), (i * 200 + 100, j * 200 + 100), 90, 1)

def winner():
    winner = None
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != 0:
            winner = board[i][0]

    for i in range(3):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != 0:
            winner =  board[0][i]

    if board[0][0] != 0 and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        winner = board[0][0]
        

    if board[2][0] != 0  and board[2][0] == board[1][1] and board[2][0] == board[0][2]:
        winner = board[2][0]
    
    o = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                o += 1
    
    if(winner == None and o == 0):
        return 0
    else:
        return winner
        


def drawWinner():
    
    if winner() == 0:
        text = myfont.render("It's a tie!", True, (255, 0, 0))
        textRect = text.get_rect()
        textRect.center = (300, 200)
        screen.blit(text, textRect)
        pygame.display.update()
    if winner() == 1:
        text = myfont.render("Winner is X!", True, (255, 0, 0))
        textRect = text.get_rect()
        textRect.center = (300, 200)
        screen.blit(text, textRect)
        pygame.display.update()
    if winner() == 2:
        text = myfont.render("Winner is O!", True, (255, 0, 0))
        textRect = text.get_rect()
        textRect.center = (300, 200)
        screen.blit(text, textRect)
        pygame.display.update()
    restart = myfont.render("Press any key to restart!", True, (255, 0, 0))
    restartRect = restart.get_rect()
    restartRect.center = (300, 400)
    screen.blit(restart, restartRect)
    pygame.display.update()
    
    

scores = [0, -10, 10] #min X max O

def AIMove():
    bestScore = -math.inf
    indexI = 0
    indexJ = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                continue
            board[i][j] = Players[1]
            score = minimax(False)
            board[i][j] = 0
            if score > bestScore:
                bestScore = score
                indexI = i
                indexJ = j
    board[indexI][indexJ] = Players[1]

def minimax(isMaximizing):
    result = winner()
    if result != None:
        return scores[result]
    
    if isMaximizing: #o
        bestScore = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] != 0:
                    continue
                board[i][j] = Players[1]
                score = minimax(False)
                board[i][j] = 0
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] != 0:
                    continue
                board[i][j] = Players[0]
                score = minimax(True)
                board[i][j] = 0
                if score < bestScore:
                    bestScore = score
        return bestScore


def notPlaying():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                global board
                board = [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]
                ]               
                playing()

def playing():
    screen.fill(pygame.Color(255, 255, 255))
    drawPlayField()
    pygame.display.update()
    board[1][1] = 2
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                i = int(y / 200)
                j = int(x / 200)
                if board[i][j] == 0:
                    board[i][j] = Players[0]
                    AIMove()
        screen.fill(pygame.Color(255, 255, 255))
        drawPlayField()
        drawBoard()
        if(winner() != None):
            drawWinner()
            pygame.display.update()
            
            notPlaying()
        pygame.display.update()

playing()