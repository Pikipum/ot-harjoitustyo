import unittest
from piece import Piece

class TestPiece(unittest.TestCase):
    def setUp(self):
        self.piece = Piece("BP", 0, 0)

    def test_piece_exists(self):
        self.assertNotEqual(self.piece, None)
    def test_is_right_piece(self):
        self.assertEqual(str(self.piece), "BP")