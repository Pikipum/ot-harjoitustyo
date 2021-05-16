import unittest
from piece import Piece
import pygame

size = (600, 600)

screen = pygame.display.set_mode(size)

class TestPiece(unittest.TestCase):
    def setUp(self):
        self.piece = Piece("BP", 60, 60)

    def test_piece_exists(self):
        self.assertNotEqual(self.piece, None)
    def test_is_right_piece(self):
        self.assertEqual(self.piece.name, "BP")