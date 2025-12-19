from board import Board
from board_exceptions import *

class ObstructionGame:
    def __init__(self):
        self.board = Board()  # Board of 6x6 grid
        self.turn = 0  # Player 0 for 'X', Player 1 for 'O'
    
    def switch_turn(self):
        """Switch turn between players."""
        self.turn = 1 - self.turn  # If it's 0, it will become 1, if it's 1, it becomes 0
    
    def current_player(self):
        """Return current player symbol: 'X' for player 0, 'O' for player 1."""
        return 'X' if self.turn == 0 else 'O'
    
    def make_move(self, row, col):
        """Handles a move: place a symbol on the board and blocks neighboring cells."""
        symbol = self.current_player()
        try:
            # Try making the move on the board
            self.board.makeMove(symbol, row, col)
            # After the move, switch to the other player
            self.switch_turn()
        except (AlreadyOccupiedBlockedCell, OutsideBoardException) as e:
            # Handle invalid moves
            print(e)
    
    def is_game_over(self):
        """Check if the game is over. It is over if there are no more valid moves."""
        if not self.board.hasAvailableMove():
            # No more available moves left
            return True
        return False
    
    def display_board(self):
        """Print the current state of the board."""
        print(self.board)
    
    def play(self):
        """Main game loop: players take turns until the game is over."""
        while not self.is_game_over():
            self.display_board()
            print(f"Player {self.current_player()}'s turn.")
            
            # Get the row and column from the player
            try:
                row = int(input("Enter the row (0-5): "))
                col = int(input("Enter the col (0-5): "))
                
                # Make the move
                self.make_move(row, col)
                
            except ValueError:
                raise InvalidPositionException()
                #continue  # Ask for input again if invalid
            
        # The game is over, show the final board
        self.display_board()
        print(f"Game Over! Player {self.current_player()} cannot make a move.")
        

# Start the game
ObstructionGame().play()
