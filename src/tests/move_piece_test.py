import unittest
from piece import Piece
import fill_board
import move_piece
import pygame

size = (600, 600)

screen = pygame.display.set_mode(size)


class TestMovepiece(unittest.TestCase):
    def setUp(self):
        board_grid = [[0 for x in range(0, 8h)] for y in range(0, 8)]
        grid = fill_board.fill(board_grid, 8)

    def test_board_exists(self):
        self.assertEqual(can_move(grid, 1, 1, 2, 1), True)