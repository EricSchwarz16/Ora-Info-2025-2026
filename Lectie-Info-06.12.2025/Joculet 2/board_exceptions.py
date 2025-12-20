class OutsideBoardException(Exception):
    def __init__(self, message="The chosen position is outside the playing field"):
        super().__init__(message)

class InvalidPositionException(Exception):
    def __init__(self, message = "Row and column must be valid integers"):
        super().__init__(message)

class AlreadyOccupiedBlockedCell(Exception):
    def __init__(self, message = "This cell is already occupied/blocked!"):
        super().__init__(message)