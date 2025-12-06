from board_exceptions import *

class Board:
    # 3 linii 3 coloane, la inceput o sa fie matricea plina de simbolul '.'
    def __init__(self):
        self.A = [['.' for col in range(3)] for row in range(3)]         # pun variabilele cu self sa le putem folosi mai departe
        self.col = 3
        self.row = 3
            
    
    def __str__(self):
        board = ''
        for i in range (self.col):
            for e in self.A[i]:
                board += e + ' '

            board += '\n' 
        
        return board
    
    def isFull(self):
        pass
    
    def winningPlayer(self): #False in cazul in care nu am un castigator si nici egalitate, simbolul castigatorului in caz ca am un castigator sau U in cazul in care este egalitate
        pass
    
    def isPlaying(self):
        if not self.isFull() and not self.winningPlayer():
            return True
        
        return False
    
    def place_move(self, row, col, symbol):
        if row >= self.row or col >= self.col or row < 0 or col < 0:
            raise OutsideBoardException()

        if self.A[row][col] != '.':
            raise AlreadyPlacedSymbolException()


# print(str(Board()))


