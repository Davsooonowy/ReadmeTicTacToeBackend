import random

class TicTacToe:
    EMPTY_CELL = ' '
    CROSS_CELL = 'X'
    NOUGHT_CELL = 'O'

    def __init__(self):
        self.board = [self.EMPTY_CELL] * 9
        self.current_winner = None

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == self.EMPTY_CELL]

    def make_move(self, square, cell_type):
        if self.board[square] == self.EMPTY_CELL:
            self.board[square] = cell_type
            if self.winner(square, cell_type):
                self.current_winner = cell_type
            return True
        return False

    def winner(self, square, cell_type):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == cell_type for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == cell_type for spot in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == cell_type for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == cell_type for spot in diagonal2]):
                return True
        return False

class MCTS:
    def __init__(self, game):
        self.game = game

    def get_move(self):
        available_moves = self.game.available_moves()
        return random.choice(available_moves)