from board import Board
from board_exceptions import *

class MinesweeperGame:
    def __init__(self):
        self.board = None  # We will initialize the board later with user input
        self.turn = 0  # Player 0 ('X') starts
        self.lives = [0, 0]  # We'll set the actual lives later
        self.players = ['X', 'O']  # Player symbols

    
    def switch_turn(self):
        """Switch turn between players."""
        self.turn = 1 - self.turn  # If it's 0, it will become 1, if it's 1, it becomes 0
    
    def current_player(self):
        """Return current player symbol: 'X' for player 0, 'O' for player 1."""
        return 'X' if self.turn == 0 else 'O'
    
    def make_move(self, row, col):
        """Handle a move: the current player chooses a cell."""
        symbol = self.current_player()
        try:
            # Try making the move (choosing a cell)
            hit_bomb = self.board.choose(row, col)
            
            if hit_bomb:
                # If the player hits a bomb, decrease their lives
                self.lives[self.turn] -= 1
                print(f"Player {self.current_player()} hit a bomb! They now have {self.lives[self.turn]} lives left.")
        
        except AlreadyOccupiedBlockedCell as e:
            print(e)  # Print error if the cell was already revealed
        except OutsideBoardException as e:
            print(e)  # Print error if the player chose an invalid position
    
    def is_game_over(self):
        """Check if the game is over."""
        # Check if any player has lost all their lives
        if self.lives[0] == 0:
            print("Player X loses!")
            return True
        if self.lives[1] == 0:
            print("Player O loses!")
            return True
        
        # Check if there are no more unchosen cells left
        if not self.board.has_unchosen():
            print("No more moves left. It's a draw!")
            return True
        
        return False
    
    def display_board(self):
        """Display the current state of the board."""
        print(self.board)
    
    def play(self):
        """Main game loop: players take turns until the game is over."""
        
        # Prompt user for board settings at the start of the game
        try:
            n = int(input("Enter the number of rows (n): "))
            m = int(input("Enter the number of columns (m): "))
            k = int(input("Enter the number of bombs (k): "))
            y = int(input("Enter the number of lives per player (y): "))
        except ValueError:
            print("Invalid input! Please enter valid integers.")
            return  # Exit if input is invalid
        
        # Initialize the board with user inputs
        self.board = Board(n, m, k)  # Create a new board with the user-defined parameters
        
        # Set player lives
        self.lives = [y, y]  # Each player starts with 'y' lives
        
        # Start the game loop after board setup
        while not self.is_game_over():
            self.display_board()  # Show the board after every turn
            print(f"Player {self.current_player()}'s turn.")
            
            # Get the row and column from the player
            try:
                row = int(input(f"Enter the row (0 to {self.board.n - 1}): "))
                col = int(input(f"Enter the col (0 to {self.board.m - 1}): "))
                
                # Make the move
                self.make_move(row, col)
                
            except ValueError:
                raise InvalidPositionException()
            
            # Switch turns after each move
            self.switch_turn()
        
        # The game is over, show the final board
        self.display_board()
        print("Game Over!")


# Start the game
game = MinesweeperGame()
game.play()
