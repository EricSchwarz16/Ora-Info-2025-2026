from repository import Repository, TxtRepository
from models import Book

class Service:
    def __init__(self):
        self.repo = TxtRepository("book.txt")
    
    def AddBook(self, b : Book):
        self.repo.AddBook(b)
    
    def DeleteBook(self, title : str, author : str):
        self.repo.DeleteBook(title, author)
    
    def UpdateBook(self, title : str, author : str, NewBook : Book):
        self.repo.UpdateBook(title, author, NewBook)
    
    def GetBooksByString(self, search_string : str):
        self.repo.GetBooksByString(search_string)
    
    def GetBooksWithPriceLowerThan(self, price : float):
        self.repo.GetBooksWithPriceLowerThan(price)
    
    def GetBooksWithPriceHigherThan(self, price : float):
        self.repo.GetBooksWithPriceHigherThan(price)
    
    

        