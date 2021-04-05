import pygame

grid = [[0 for x in range(8)] for y in range(8)]

black_color = (0, 0, 0)
white_color = (255, 255, 255)

size = (1367, 720)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Poor man's chess")

#Program will run in a loop until variable exit is changed to True.
exit = False

clock = pygame.time.Clock()


while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    #Game code


    screen.fill(white_color)

    clock.tick(60)

pygame.quit()



def drawboard():
    square_size = 20