from book_exceptions.book_date_exception import *
from book_exceptions.negative_book_fields_exception import *
from datetime import datetime

class Book:
    def __init__(self, title, author, DateOfPublish, publisher, price, quantity, isFromLoad=False):
        # validation
        
        if DateOfPublish < datetime.now().year and isFromLoad == False:
            raise BookDateException()
        
        if price < 0:
            raise NegativeBookPrice()
        
        if quantity < 0:
            raise NegativeBookQuantity()
        
        self.title = title
        self.author = author
        self.DateOfPublish = DateOfPublish
        self.publisher = publisher
        self.price = price
        self.quantity = quantity
    
    def __repr__ (self):
        return f"{self.title} | {self.author} | {self.DateOfPublish} | {self.publisher} | {self.price} | {self.quantity}"
    
    def __str__ (self):
        return f"{self.title} | {self.author} | {self.DateOfPublish} | {self.publisher} | {self.price} | {self.quantity}"
    
    def eq__(self, other):
        return self.title == other.title and self.author == other.author
