from repository import Repository, TxtRepository
from models import Book
from book_exceptions.book_date_exception import BookDateException
from book_exceptions.negative_book_fields_exception import *

class Service:
    def __init__(self):
        self.repo = TxtRepository("book.txt")
    
    def AddBook(self, title, author, DateOfPublic, publisher, price, quantity):
        try:
            self.repo.AddBook(title, author, DateOfPublic, publisher, price, quantity)
        except (BookDateException, NegativeBookPrice, NegativeBookQuantity) as e:
            raise e
    
    def DeleteBook(self, title : str, author : str):
        self.repo.DeleteBook(title, author)
    
    def UpdateBook(self, title : str, author : str, NewBook : Book):
        self.repo.UpdateBook(title, author, NewBook)
    
    def GetBooksByString(self, search_string : str):
        return  self.repo.GetBooksByString(search_string)
    
    def GetBooksWithPriceLowerThan(self, price : float):
        return self.repo.GetBooksWithPriceLowerThan(price)
    
    def GetBooksWithPriceHigherThan(self, price : float):
        return self.repo.GetBooksWithPriceHigherThan(price)
    

        