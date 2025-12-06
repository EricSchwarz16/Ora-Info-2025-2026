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
        for i in range(self.row):
            for j in range(self.col):
                if self.A[i][j] == '.':
                    return False
        
        return True
    
    def makeMove(self, symbol : str, row : int, col : int):
        self.A[row][col] = symbol
        

    
    def winningPlayer(self): #False in cazul in care nu am un castigator si nici egalitate, simbolul castigatorului in caz ca am un castigator sau U in cazul in care este egalitate
        for i in range(self.row):                   # 1) fiecare combinatie pe linie
            ok = 1
            for j in range(1, self.col):
                if self.A[i][j] != self.A[i][j-1]:
                    ok = 0
            
            if ok:
                return self.A[i][0]
        
        for j in range(self.col):                    # 2) fiecare combinatie pe coloane
            ok = 1
            for i in range(1, self.row):
                if self.A[i][j] != self.A[i-1][j]:
                    ok = 0
            
            if ok:
                return self.A[0][j]
        
        ok = 1
        for i in range(1, self.row):                                         # 3.1) diagonala principala
            if self.A[i][i] != self.A[i - 1][i - 1]:
                ok == 0
            
        if ok:
            return self.A[0][0]
        
        # 3.2) diagonala secundara

        i, j = 1, self.col
        ok = 1
        while i < self.row:
            if self.A[i][j] != self.A[i - 1][j + 1]:
                ok = 0
            
            i += 1
            j -= 1
        
        if ok:
            return self.A[0][self.col]

        # verificare egalitate

        if self.isFull():
            return 'U'

        return False

            


             
        

            

        
        
        
        

        

        


    
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


