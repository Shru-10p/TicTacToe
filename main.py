import Resources.TicTacToe as TicTacToe
import Resources.Players as Players

def play(game:TicTacToe.Game, player_1:Players.Player, player_2:Players.Player, print_game=True):
    if print_game:
        game.print_board_nums()
    letter = 'X'
    while game.empty_squares():
        if letter == 'X':
            square = player_1.get_move(game)
        else:
            square = player_2.get_move(game)
        if game.make_move(square):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!',end='\n\n')
                return letter
            letter = 'O' if letter == 'X' else 'X'
    if print_game:
        print('It\'s a tie!')

def menu():
    print('\nWelcome to Tic Tac Toe!',end='\n\n')
    print('Choose your opponent:')
    print('1. Human')
    print('2. Random Computer')
    print('3. None, i\'ve had enough.\n')
    choice = input('Enter your choice: ')
    return choice

def main():
    while True:
        choice = menu()
        if choice == '1':
            player_1 = Players.HumanPlayer('X')
            player_2 = Players.HumanPlayer('O')
            play(TicTacToe.Game(), player_1, player_2)
        elif choice == '2':
            player_1 = Players.HumanPlayer('X')
            player_2 = Players.RandomComputerPlayer('O')
            play(TicTacToe.Game(), player_1, player_2)
        elif choice == '3':
            print('\nThanks for playing!\n')
            break
        else:
            print('Invalid choice. Try again.')

if __name__ == '__main__':
    main()