import numpy as np


class TicTacToe:
    def __init__(self):
        self.board = np.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])

        self.turn = 1

    def move(self, x, y):
        self.board[y][x] = self.turn
        self.turn *= -1

    def isValid(self, x, y):
        if self.board[y][x] == 0:
            return True

        return False

    def isDone(self):
        for row in self.board:
            if sum(row) == 3 or sum(row) == -3:
                return True

        for column in self.board.T:
            if sum(column) == 3 or sum(column) == -3:
                return True

        diagonal1 = sum((self.board[0][0], self.board[1][1], self.board[2][2]))
        diagonal2 = sum((self.board[2][0], self.board[1][1], self.board[0][2]))

        if diagonal1 == 3 or diagonal1 == -3 or diagonal2 == 3 or diagonal2 == -3:
            return True

        return False


tictactoe = TicTacToe()
tictactoe.move(0, 0)
tictactoe.move(1, 1)
tictactoe.move(2, 1)
tictactoe.move(0, 1)
tictactoe.move(1, 0)
tictactoe.move(2, 2)
print(tictactoe.board)
print(tictactoe.isDone())
