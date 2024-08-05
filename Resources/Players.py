import random, Resources.TicTacToe as TicTacToe

# Player class
class Player:
    def __init__(self, letter):
        self.letter = letter

    # we want all players to get their next move given a game
    def get_move(self, game:TicTacToe.Game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    #get the next move from the player
    def get_move(self, game:TicTacToe.Game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    # get the next move from the computer
    def get_move(self, game:TicTacToe.Game):
        square = random.randint(0,1000) % 9
        while square not in game.available_moves():
            square = random.randint(0,1000) % 9
        return square

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game: TicTacToe.Game):
        if len(game.available_moves()) == 9 or 8:
            square = random.randint(0,1000) % 9
        else:
            square = self.minimax(game, self.letter)
        return square

    def minimax(self, state:TicTacToe.Game, player:str)->int:
        max_player = 'X' # maximizer is always X (who goes first)
        other_player = 'O' if player == max_player else max_player

        if state.current_winner == other_player:
            return {'square': None, 'score': 1}
        elif not state.empty_squares():
            return {'square': None, 'score': 0}

        if player == max_player:
            best = {'square': None, 'score': -1000}
        else:
            best = {'square': None, 'score': 1000}

        for move in state.available_moves():
            state.make_move(move)
            sim_score = self.minimax(state, other_player)

            state.board[move] = ' '
            state.current_winner = None
            sim_score['square'] = move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best['square']
