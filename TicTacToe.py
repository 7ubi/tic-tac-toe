import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("tic tac toe")

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
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != 0:
            print(str(board[i][0]) + " has won")

    for i in range(3):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != 0:
            print(str(board[0][i]) + " has won")

    if board[0][0] != 0 and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return 
        # print(str(board[0][0]) + " has won")

    if board[2][0] != 0  and board[2][0] == board[1][1] and board[2][0] == board[0][2]:
        print(str(board[0][0]) + " has won")


def main():
    currentPlayer = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                i = int(y / 200)
                j = int(x / 200)
                if board[i][j] == 0:
                    board[i][j] = Players[currentPlayer]
                    currentPlayer = (currentPlayer + 1)%2
                    winner()
        screen.fill(pygame.Color(255, 255, 255))
        drawPlayField()
        drawBoard()
        
        pygame.display.update()

main()