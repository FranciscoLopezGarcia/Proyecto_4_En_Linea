import unittest

class Tablero():
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.turno = 0
        self.last_move = [-1, -1]

    def which_turn(self):
        players = ['X', 'O']
        return players[self.turno % 2]
    
    def in_bounds(self, x, y):
        return (x >= 0 and x < 8 and y >= 0 and y < 8)

    def turn(self, column):
        for i in range(7, -1, -1):
            if self.board[i][column] == ' ':
                self.board[i][column] = self.which_turn()
                self.last_move = [i, column]

                self.turno += 1
                return True

        return False

    def check_winner(self):
        last_row = self.last_move[0]
        last_col = self.last_move[1]
        last_letter = self.board[last_row][last_col]

        directions = [[[-1, 0], 0, True], 
                      [[1, 0], 0, True], 
                      [[0, -1], 0, True],
                      [[0, 1], 0, True],
                      [[-1, -1], 0, True],
                      [[1, 1], 0, True],
                      [[-1, 1], 0, True],
                      [[1, -1], 0, True]]
        
        for a in range(4):
            for d in directions:
                r = last_row + (d[0][0] * (a+1))
                c = last_col + (d[0][1] * (a+1))

                if d[2] and self.in_bounds(r, c) and self.board[r][c] == last_letter:
                    d[1] += 1
                else:
                    d[2] = False

        for i in range(0, 7, 2):
            if (directions[i][1] + directions[i+1][1] >= 3):
                return last_letter   

        return False


## Test Backend ##
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

if __name__ == '__main__':
    unittest.main()