from board import Board

class XOGame:
    def __init__(self):
        self.board = Board()
        self.turn = 1 # 1 pentru X, 0 pentru O 
    
    def makeMove(self, row: int, col: int):
        symbol = 'X' if self.turn else 'O'
        self.board.makeMove(symbol, row, col)
        
    
    def runGame(self):
        
        
        while not self.board.winningPlayer(): 
            print(f"Player {'X'if self.turn == 1 else 'O '} is moving")
            row = int(input("Choose the row: "))
            col = int(input("Choose the col: "))
            self.makeMove(row, col)
            print(self.board)
            
        print(self.board.winningPlayer())

XOGame().runGame()     
            