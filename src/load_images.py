import pygame, sys, os

#Load placeholder images for the project

def load(screen):
    dict = {}

    dict["BP"] = pygame.image.load(os.path.join("images/chess_pawn_60.png")).convert_alpha()
    dict["BK"] = pygame.image.load(os.path.join("images/chess_pawn_60.png")).convert_alpha()
    dict["BT"] = pygame.image.load(os.path.join("images/chess_pawn_60.png")).convert_alpha()
    dict["BQ"] = pygame.image.load(os.path.join("images/chess_pawn_60.png")).convert_alpha()
    dict["BH"] = pygame.image.load(os.path.join("images/chess_pawn_60.png")).convert_alpha()
    dict["BB"] = pygame.image.load(os.path.join("images/chess_pawn_60.png")).convert_alpha()
    dict["WP"] = pygame.image.load(os.path.join("images/chess_pawn_60.png")).convert_alpha()
    dict["WK"] = pygame.image.load(os.path.join("images/chess_pawn_60.png")).convert_alpha()
    dict["WQ"] = pygame.image.load(os.path.join("images/chess_pawn_60.png")).convert_alpha()
    dict["WB"] = pygame.image.load(os.path.join("images/chess_pawn_60.png")).convert_alpha()
    dict["WT"] = pygame.image.load(os.path.join("images/chess_pawn_60.png")).convert_alpha()
    dict["WH"] = pygame.image.load(os.path.join("images/chess_pawn_60.png")).convert_alpha()

    return dict