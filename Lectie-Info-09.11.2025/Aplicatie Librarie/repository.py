from models import Book
from book_utils import BookUtils
from book_exceptions.book_date_exception import *
from datetime import datetime

class Repository:
    def __init__ (self):
        self.BookList = []
        self.LoadData()
        print(self.BookList)
    
    def AddBook(self, title, author, DateOfPublic, publisher, price, quantity):
        b = Book(title, author, DateOfPublic, publisher, price, quantity)
        
        for ExistingBook in self.BookList:
            if ExistingBook.title == b.title and ExistingBook.author == b.author:
                ExistingBook.quantity += b.quantity
                return 
            
        self.BookList.append(b)
        self.SaveData()
    
    def DeleteBook(self, title : str, author : str):
        for b in self.BookList:
            if b.title == title and b.author == author:
                self.BookList.remove(b)
        
        self.SaveData()
    
    def UpdateBook(self, title : str, author : str, NewBook : Book):
        for i, b in enumerate(self.BookList):
            if b.title == title and b.author == author:
                self.BookList[i] = NewBook
                break
        
        self.SaveData()
    
    def GetBooksByString(self, search_string : str):
        if not search_string:
            return self.BookList
        
        return [
            book for book in self.BookList
                if search_string in book.title or search_string in book.author
        ]

    def GetBooksWithPriceLowerThan(self, price : float):
        return [
            book for book in self.BookList
                if book.price < price
        ]

    def GetBooksWithPriceHigherThan(self, price: float):
        return [
            book for book in self.BookList
            if book.price > price
        ]
    
    def SaveData(self):
        pass
    
    def LoadData(self):
        pass


class TxtRepository(Repository):
    def __init__(self, file : str):
        self.file = file
        super().__init__()
        print(self.BookList)
    
    def SaveData(self):
        with open(self.file, "w") as f:
           for book in self.BookList:
              f.write(str(book))
              f.write("\n")

    def LoadData(self):
        with open(self.file) as file:
            for line in file:
                self.BookList.append(BookUtils.getBookFromLine(line))
