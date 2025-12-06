class OutsideBoardException(Exception):
    def __init__(self, message):
        self.message = message
    
    def __init__(self):
        self.message = "The chosen position is outside the playing field"
    
    def __str__(self):
        return self.message
    

class AlreadyPlacedSymbolException(Exception):
    def __init__(self, message):
        self.message = message
    
    def __init__(self):
        self.message = 'The chosen position already has a symbol placed'
    
    def __str__(self):
        return self.message

class GameAlreadyFinished(Exception):
    def __init__(self, message):
        self.message = message
    
    def __init__(self):
        self.message = 'Game is already finished. You cannot make any other moves!'
    
    def __str__(self):
        return self.message

class InvalidSymbolException(Exception):
    def __init__(self, message):
        self.message = message
    
    def __init__(self):
        self.message = 'You cannot use another symbol besides X or O!'
    
    def __str__(self):
        return self.message

class NotPlayerTurnException(Exception):
    def __init__(self, message):
        self.message = message
    
    def __init__(self):
        self.message = 'You cannot move if the other player has to move. It is not your turn!'
    
    def __str__(self):
        return self.message
    
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
    
    def place_move(self, row, col, symbol):
        if row >= self.row or col >= self.col or row < 0 or col < 0:
            raise OutsideBoardException()

        if self.A[row][col] != '.':
            raise AlreadyPlacedSymbolException()


# print(str(Board()))


