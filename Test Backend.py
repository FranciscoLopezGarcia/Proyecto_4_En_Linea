from Back import *
import unittest

class TestBack(unittest.TestCase):
    def test_in_bounds(self):
        tablero = Tablero()
        self.assertEqual(tablero.in_bounds(0, 0), True)
        self.assertEqual(tablero.in_bounds(7, 7), True)
        self.assertEqual(tablero.in_bounds(8, 8), False)
        self.assertEqual(tablero.in_bounds(-1, -1), False)
    def test_turn(self):
        tablero = Tablero()
        self.assertEqual(tablero.turn(0), True)
        self.assertEqual(tablero.turn(0), True)
        self.assertEqual(tablero.turn(0), True)
        self.assertEqual(tablero.turn(0), True)
        self.assertEqual(tablero.turn(0), True)
        self.assertEqual(tablero.turn(0), True)
        self.assertEqual(tablero.turn(0), True)
        self.assertEqual(tablero.turn(0), True)
        self.assertEqual(tablero.turn(0), False)
    def test_win_diagonal(self):
        tablero = Tablero()
        tablero.board[0][0] = 'X'
        tablero.board[1][1] = 'X'
        tablero.board[2][2] = 'X'
        tablero.board[3][3] = 'X'
        tablero.last_move = [3, 3]
        self.assertEqual(tablero.check_winner(), 'X')
        tablero.board[0][0] = 'O'
        tablero.board[1][1] = 'O'
        tablero.board[2][2] = 'O'
        tablero.board[3][3] = 'O'
        tablero.last_move = [3, 3]
        self.assertEqual(tablero.check_winner(), 'O')
    def test_win_vert(self):
        tablero = Tablero()
        tablero.board[0][0] = 'X'
        tablero.board[1][0] = 'X'
        tablero.board[2][0] = 'X'
        tablero.board[3][0] = 'X'
        tablero.last_move = [3, 0]
        self.assertEqual(tablero.check_winner(), 'X')
        tablero.board[0][0] = 'O'
        tablero.board[1][0] = 'O'
        tablero.board[2][0] = 'O'
        tablero.board[3][0] = 'O'
        tablero.last_move = [3, 0]
        self.assertEqual(tablero.check_winner(), 'O')
    def test_win_hor(self):
        tablero = Tablero()
        tablero.board[0][0] = 'X'
        tablero.board[0][1] = 'X'
        tablero.board[0][2] = 'X'
        tablero.board[0][3] = 'X'
        tablero.last_move = [0, 3]
        self.assertEqual(tablero.check_winner(), 'X')
        tablero.board[0][0] = 'O'
        tablero.board[0][1] = 'O'
        tablero.board[0][2] = 'O'
        tablero.board[0][3] = 'O'
        tablero.last_move = [0, 3]
        self.assertEqual(tablero.check_winner(), 'O')
    def test_win_diagonal2(self):
        tablero = Tablero()
        tablero.board[0][3] = 'X'
        tablero.board[1][2] = 'X'
        tablero.board[2][1] = 'X'
        tablero.board[3][0] = 'X'
        tablero.last_move = [3, 0]
        self.assertEqual(tablero.check_winner(), 'X')
        tablero.board[0][3] = 'O'
        tablero.board[1][2] = 'O'
        tablero.board[2][1] = 'O'
        tablero.board[3][0] = 'O'
        tablero.last_move = [3, 0]
        self.assertEqual(tablero.check_winner(), 'O')
    def test_win_vert2(self):
        tablero = Tablero()
        tablero.board[3][0] = 'X'
        tablero.board[3][1] = 'X'
        tablero.board[3][2] = 'X'
        tablero.board[3][3] = 'X'
        tablero.last_move = [3, 3]
        self.assertEqual(tablero.check_winner(), 'X')
        tablero.board[3][0] = 'O'
        tablero.board[3][1] = 'O'
        tablero.board[3][2] = 'O'
        tablero.board[3][3] = 'O'
        tablero.last_move = [3, 3]
        self.assertEqual(tablero.check_winner(), 'O')


if __name__ == '__main__':
    unittest.main()