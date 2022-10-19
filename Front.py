import unittest
from Back import *
class Juego():
    def __init__(self):
        self.fin = False
        self.uwu = Tablero()
    def printTablero(self):
        for x in range(8):
            for y in range(8):
                print(" " + self.uwu.board[x][y] + "  ", end="")
            print("\n")
            print(" " + str(self.uwu.board[x][y]) + "  ", end="")
            print("\n")
            print("\n     1    2    3    4    5    6    7    8   ", end="")
            for x in range(8):
                print("\n   +----+----+----+----+----+----+----+----+")
                print(x, " |", end="")
                for y in range(8):
                    if(self.uwu.board[x][y] == "0"):
                        print("", self.uwu.turno, end = "  |")
                    elif(self.uwu.board[x][y] == "1"):
                        print("", self.uwu.turno, end = "  |")
                    else:
                        print(" ", self.uwu.board[x][y], end= " |")
            print("\n   +----+----+----+----+----+----+----+----+")
    
    def play(self):
        while not self.fin:
            self.printTablero()
            valid_move = False
            while not valid_move:
                user_move = input(f"Turno de {self.uwu.which_turn()} elegi una columna entre 1 y 8: ")
                try:
                    valid_move = self.uwu.turn(int(user_move)-1)
                except:
                    print(f"Error, poner un valor en rango")

            self.fin = self.uwu.check_winner()
        
        self.printTablero()
        print(f"Fin del juego, {self.fin} es el ganador")

if __name__ == '__main__':
    mar = Juego()
    mar.play()




