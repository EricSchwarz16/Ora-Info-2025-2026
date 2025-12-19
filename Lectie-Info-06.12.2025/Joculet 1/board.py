from board_exceptions import *

class Board:
    def __init__(self):
        # 6x6 grid, initially filled with '.'
        self.A = [['.' for _ in range(6)] for _ in range(6)]
        self.row = 6
        self.col = 6
    
    def __str__(self):
        board = ''
        for i in range(self.row):
            for j in range(self.col):
                board += self.A[i][j] + ' '
            board += '\n'
        return board

    def isFull(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.A[i][j] == '.':
                    return False
        return True

    def blockNeighbors(self, row, col):
        # Block cells around the placed cell (row, col)
        # We need to block the 8 neighbors (all 8 directions around a cell)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.row and 0 <= c < self.col and self.A[r][c] == '.':
                self.A[r][c] = 'B'  # mark as blocked cell with 'X' or 'O' depending on whose turn it is

    def makeMove(self, symbol: str, row: int, col: int):
        # Check if the cell is within bounds
        if row < 0 or row >= self.row or col < 0 or col >= self.col:
            raise OutsideBoardException()
        
        # Check if the cell is already blocked or filled
        if self.A[row][col] != '.':
            raise AlreadyOccupiedBlockedCell()
        
        # Place the symbol
        self.A[row][col] = symbol
        
        # Block neighboring cells
        self.blockNeighbors(row, col)

    def hasAvailableMove(self):
        # Check if there's any empty space remaining on the board
        for i in range(self.row):
            for j in range(self.col):
                if self.A[i][j] == '.':
                    return True
        return False

    def winningPlayer(self):
        # Check if there is a player who has no available move (loses the game)
        if not self.hasAvailableMove():
            return "No available moves left."
        
        return None  # No winner yet, game can continue
