from random import randint
from board_exceptions import *  # Import exceptions

class Board:
    def __init__(self, n, m, k):
        self.n = n  # Number of rows
        self.m = m  # Number of columns
        self.k = k  # Number of bombs
        self.board = [['.' for _ in range(m)] for _ in range(n)]
        self.bombs = set()  # Track bomb positions
        self.revealed = set()  # Track revealed positions
        self.place_bombs()

    def place_bombs(self):
        """Randomly place k bombs on the board."""
        placed = 0
        while placed < self.k:
            row = randint(0, self.n - 1)
            col = randint(0, self.m - 1)
            if (row, col) not in self.bombs:
                self.bombs.add((row, col))
                placed += 1

    def __str__(self):
        """Display the board with hidden and revealed positions."""
        board_display = ''
        for i in range(self.n):
            for j in range(self.m):
                if (i, j) in self.revealed:
                    if (i, j) in self.bombs:
                        board_display += 'B '  # Show bomb if revealed
                    else:
                        board_display += 'C '  # Show chosen cell
                else:
                    board_display += '. '  # Hidden cell
            board_display += '\n'
        return board_display

    def choose(self, row, col):
        """Handle a player choosing a square."""
        # Check if the chosen position is outside the board
        if row < 0 or row >= self.n or col < 0 or col >= self.m:
            raise OutsideBoardException()  # Raise OutsideBoardException if outside bounds
        
        # Check if the cell has already been revealed (or chosen)
        if (row, col) in self.revealed:
            raise AlreadyOccupiedBlockedCell()  # Cell already chosen/revealed
        
        # Mark the position as revealed
        self.revealed.add((row, col))

        # Check if it's a bomb
        if (row, col) in self.bombs:
            return True  # Player hit a bomb
        return False  # It's an empty square

    def has_unchosen(self):
        """Check if there are any unchosen cells left."""
        return len(self.revealed) < self.n * self.m

    def remaining_bombs(self):
        """Count how many bombs are left on the board."""
        return len(self.bombs - self.revealed)
