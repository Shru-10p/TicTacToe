class Game:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # we will use a single list to represent 3x3 board
        self.current_winner = None
        self.player = 'X'

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
            print('-------------')

    # static method is a method that belongs to the class and not the object of the class
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
            print('-------------')


    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    # make a move on the board
    def make_move(self, square):
        if self.board[square] == ' ':
            self.board[square] = self.player
            if self.winner(square, self.player):
                self.current_winner = self.player
            self.player = 'O' if self.player == 'X' else 'X'
            return True
        return False

    # check if the last move was a winning move
    def winner(self, square, player):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == player for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == player for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == player for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == player for spot in diagonal2]):
                return True
        return False
