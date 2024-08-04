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
    pass