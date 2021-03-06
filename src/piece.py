import pygame, sys, os

class Piece():

    def __init__(self,name,position_y, position_x):
        self.name = name
        self.position_y = position_y
        self.position_x = position_x
        if name == "None":
            self.image = pygame.image.load(os.path.join("images/blank.png")).convert_alpha()
        else:
            self.image = pygame.image.load(os.path.join("images/" + self.name + ".png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.position_x
        self.rect.y = self.position_y

    def get_pos(self):
        return self.position
    
    def __str__(self):
        return self.name

    def get_rect(self):
        return self.rect

    def set_rect(self, x, y, s, w):
        self.rect = pygame.Rect(x, y, s, w)
    
    def set_name(self, name):
        self.name = name
