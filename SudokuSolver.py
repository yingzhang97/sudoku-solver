import pygame
import requests

width = 455
inc = 50
white = (255,255,255)
black = (0,0,0)

#examples for test
# response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
# grid = response.json()['board']

grid = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]

def possible(row, column, number):
    global grid
    
    for i in range(0, 9):
        if grid[i][column] == number or grid[row][i] == number:
            return False   
    
    column0 = (column // 3) * 3
    row0 = (row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[row0+i][column0+j] == number:
                return False

    return True

isSolved = False
def sudoku_solver(screen):
    myfont = pygame.font.SysFont('Arial', 35)
    for i in range(0, 9):
        for j in range(0, 9):
            if(grid[i][j] == 0): 
                for k in range(1, 10):
                    if possible(i, j, k):                   
                        grid[i][j] = k
                        pygame.draw.rect(screen, (135,206,250), (j*inc+5, i*inc+5, inc-10, inc-10))
                        value = myfont.render(str(k), True, black)
                        screen.blit(value, (j*inc+15, i*inc))
                        pygame.display.update()
                        pygame.time.delay(20)
                        sudoku_solver(screen)
                        global isSolved
                        if(isSolved):
                            return
                        grid[i][j] = 0
                        pygame.draw.rect(screen, white, (j*inc+5, i*inc+5, inc-10, inc-10))
                        pygame.display.update()
                return               
    isSolved = True


def main():    
    pygame.init()
    screen = pygame.display.set_mode((width, width))
    pygame.display.set_caption("Sudoku Solver")
    screen.fill(white)
    myfont = pygame.font.SysFont('Times', 35)
   
    for i in range(0, 10):
        if(i%3 == 0):
            wide = 5
        else:
            wide = 2
        pygame.draw.line(screen, black, (inc*i, 0), (inc*i, inc*9), wide ) 
        pygame.draw.line(screen, black, (0, inc*i), (inc*9, inc*i), wide ) 
    pygame.display.update()
    
    for i in range(0, 9):
        for j in range(0, 9):
            if(0<grid[i][j]<10):
                value = myfont.render(str(grid[i][j]), True, black)
                screen.blit(value, (j*inc+15, i*inc))
    pygame.display.update()
            
   
    sudoku_solver(screen)
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
   
main()