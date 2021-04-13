import pygame

black_color = (0, 0, 0)
white_color = (255, 255, 255)
gray_color = (127, 127, 127)

size = (600, 600)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Python Chess")

#Program will run in a loop until variable exit is changed to True.
exit = False

clock = pygame.time.Clock()



def drawboard():
    size = 60 # Square size in pixels
    
    boardLength = 8 # Makes an 8 by 8 board, can be changed to even numbers
    screen.fill(gray_color)
    white = 0 # If white % 0, draws a white rectangle. Else draws black
    for i in range(1,boardLength+1):
        for z in range(1,boardLength+1):
            if white % 2 == 0:
                pygame.draw.rect(screen, white_color,[size*z,size*i,size,size]) #Draw white rectangle
            else:
                pygame.draw.rect(screen, black_color, [size*z,size*i,size,size]) #Draw black rectangle
            white +=1
        white-=1
    pygame.draw.rect(screen,black_color,[size,size,boardLength*size,boardLength*size],1) #Draws a border for the rectangles
     
    pygame.display.flip() #Update the display



while not exit:
    drawboard() #Draw the board
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    #Game code


    screen.fill(gray_color)

    clock.tick(60)

pygame.quit()



