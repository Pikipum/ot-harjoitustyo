import unittest
from piece import Piece
import fill_board
import move_piece
import pygame

size = (600, 600)

screen = pygame.display.set_mode(size)


class TestMovepiece(unittest.TestCase):
    def setUp(self):
        board_grid = [[0 for x in range(0, boardLength)] for y in range(0, boardLength)]
        grid = fill_board.fill(board_grid, 8)

    def test_board_exists(self):
        self.assertEqual(can_move(board_grid, 1, 1, 2, 1), True)