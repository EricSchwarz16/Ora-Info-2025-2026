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
    