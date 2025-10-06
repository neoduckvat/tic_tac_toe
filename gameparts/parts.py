class Board:
    def __init__(self, field_size=3):
        self.field_size = field_size
        self.board = [[' ' for _ in range(field_size)] for _ in range(field_size)]

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * (self.field_size * 2 - 1))

    def make_move(self, row, column, symbol):
        if self.board[row][column] != ' ':
            raise ValueError('Ячейка уже занята')
        self.board[row][column] = symbol
