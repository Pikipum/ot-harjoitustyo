WINDOW_WIDTH = 720
WINDOW_HEIGHT = 1360
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(WINDOW_WIDTH):
        for y in range(WINDOW_HEIGHT):
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)