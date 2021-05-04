import pygame, sys, os
import fill_board, load_images, piece

black_color = (0, 0, 0)
white_color = (255, 255, 255)
gray_color = (127, 127, 127)

size = (600, 600)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Python Chess")

#Program will run in a loop until variable exit is changed to True.
exit = False

clock = pygame.time.Clock()

boardLength = 8

board_grid = [[0 for x in range(0, boardLength)] for y in range(0, boardLength)] #Create an 8x8 grid with zeroes

board_grid = fill_board.fill(board_grid, boardLength) #Initialize the board with the pieces
square_size = 60
def drawboard():
    size = 60 # Square size in pixels
    
  #  boardLength = 8 # Makes an 8 by 8 board, can be changed to even numbers
    screen.fill(black_color)
    white = 0 # If white % 0, draws a white rectangle. Else draws black
    for i in range(1,boardLength+1):
        for z in range(1,boardLength+1):
            if white % 2 == 0:
                pygame.draw.rect(screen, white_color,[size*z,size*i,size,size]) #Draw white rectangle
            else:
                pygame.draw.rect(screen, gray_color, [size*z,size*i,size,size]) #Draw black rectangle
            if board_grid[i-1][z-1] != 0: #Check if a piece is on this rectangle
                piece = board_grid[i-1][z-1]
                board_grid[i-1][z-1].set_rect(size*z, size*i, size, size)
                if board_grid[i-1][z-1] != str("None"):
                    screen.blit(piece.image, piece.rect) #Draw the correct piece on the rectangle
                
            white +=1
        white-=1
    pygame.draw.rect(screen,black_color,[size,size,boardLength*size,boardLength*size],1) #Draws a border
    pygame.display.update()
    pygame.display.flip() #Update the display


selected = None
pos_x = None
pos_y = None
while not exit:
    drawboard() #Draw the board
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    #Game code
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            for x in range(1,9):
                for y in range(1,9):
                        if board_grid[x-1][y-1].get_rect().collidepoint(event.pos):
                            selected = board_grid[x-1][y-1]
                            print(selected)
                            pos_x = x
                            pos_y = y
        if event.type == pygame.MOUSEBUTTONUP:
            for x in range(1,9):
                for y in range(1,9):
                        if board_grid[x-1][y-1].get_rect().collidepoint(event.pos):
                            board_grid[x-1][y-1] = selected
                            board_grid[pos_x-1][pos_y-1] = piece.Piece("None", 60, 60)
                        
    clock.tick(60)

pygame.quit()


