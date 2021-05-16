import pygame, sys, os
import fill_board, load_images, piece, move_piece

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



new = pygame.image.load(os.path.join("images/new_game.png")).convert_alpha()
new_rect = pygame.Rect(0, 0, 120, 60)
load = pygame.image.load(os.path.join("images/load_game.png")).convert_alpha()
load_rect = pygame.Rect(200, 0, 120, 60)
quit = pygame.image.load(os.path.join("images/quit.png")).convert_alpha()
quit_rect = pygame.Rect(400, 0, 120, 60)

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
    screen.blit(new, [0, 0, 60, 120])
    screen.blit(load, [200, 0, 60, 120])
    screen.blit(quit, [400, 0, 60, 120])
    pygame.display.update()
    pygame.display.flip() #Update the display


#Variables used for tracking moves
selected = None
selected_pos_x = None
selected_pos_y = None
destination_pos_x = None
destination_pos_y = None
whites_turn = True #White gets the first move

while not exit:
    drawboard() #Draw the board
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    #Game code
    
        if event.type == pygame.MOUSEBUTTONDOWN: #Clicking down selects a piece, dragging it moves it.
            if new_rect.collidepoint(event.pos):
                board_grid = fill_board.fill(board_grid, boardLength) #If clicked new game, format the grid again
                whites_turn = True
                continue
            if load_rect.collidepoint(event.pos):
                continue
            if quit_rect.collidepoint(event.pos):
                exit = True
            for x in range(1,9): #Go through the board
                for y in range(1,9):
                        if board_grid[x-1][y-1].get_rect().collidepoint(event.pos): #Check if the click lined up with a piece
                            if whites_turn and board_grid[x-1][y-1].name.startswith("W"):
                                selected = board_grid[x-1][y-1] #Save selected piece
                                print(selected)
                                selected_pos_x = x #Save the x and y coordinates of the selected piece
                                selected_pos_y = y
                                whites_turn = False
                            elif whites_turn == False and board_grid[x-1][y-1].name.startswith("B"):
                                selected = board_grid[x-1][y-1] #Save selected piece
                                print(selected)
                                selected_pos_x = x #Save the x and y coordinates of the selected piece
                                selected_pos_y = y
                                whites_turn = True
        if event.type == pygame.MOUSEBUTTONUP: #Releasing mouse button will move the piece
            for x in range(1,9): #Go through the board
                for y in range(1,9):
                        if board_grid[x-1][y-1].get_rect().collidepoint(event.pos):  #Check if the click lined up with a piece
                            destination_pos_x = x
                            destination_pos_y = y
                            if move_piece.can_move(board_grid, selected_pos_x, selected_pos_y, destination_pos_x, destination_pos_y): #Check if move is valid
                                board_grid[x-1][y-1] = selected #Execute the move
                                board_grid[selected_pos_x-1][selected_pos_y-1] = piece.Piece("None", 60, 60) #Replace old position with a blank
                            else:
                                continue
                        
    clock.tick(60)

pygame.quit()


