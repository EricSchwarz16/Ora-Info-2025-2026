from service import *

class UI2:
    def __init__(self):
        self.service = Service()        # Warum brauchen wir das ?
    
    def AddBook(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        DateOfPublish = input("Enter the date of publication for the book: ")
        publisher = input("Enter the publisher for the book: ")
        price = float(input("Enter the price of the book in €"))
        self.service.AddBook(Book(title, author, DateOfPublish, publisher, price))
    
    def DeleteBook(self):
        title = input("Title of to be deleted Book: ")
        author = input("Author of to be deleted Book: ")
        self.service.DeleteBook(title, author)
    
    def UpdateBook(self):
        title = input("Name of to be updated title: ")
        author = input("Name of to be updated author: ")
        
        title2 = input("Enter the title of the new book: ")
        author2 = input("Enter the author of the new book: ")
        DateOfPublish = input("Enter the date of publication for the new book: ")
        publisher = input("Enter the publisher for the new book: ")
        price = float(input("Enter the price of the new book in €"))
        self.service.UpdateBook(title, author, Book(title2, author2, DateOfPublish, publisher, price))
        
    
    def GetBooksByString(self):
        search_string = input("String to be used in searching: ")
        self.service.GetBooksByString(search_string)
    
    def GetBooksWithPriceLowerThan(self):
        price = float(input("Name the price of reference in €: "))
        self.service.GetBooksWithPriceLowerThan(price)
    
    def GetBooksWithPriceHigherThan(self):
        price = float(input("Name the price of reference in €: "))
        self.service.GetBooksWithPriceHigherThan(price)
    
    def RunUI(self):
        while True:
            print("""
Choose the following operation:
0 : Exit
1 : Add a book
2 : Delete a book
3 : Update a book
4 : Get books by a search string
5 : Get all books with a price lower than
6 : Get all books with a price higher than 
                  """
            )
            op = int(input(()))

            if op == 0:
                break

            elif op == 1:
                self.AddBook()
            
            elif op == 2:
                self.DeleteBook()
            
            elif op == 3:
                self.UpdateBook()
            
            elif op == 4:
                self.GetBooksByString()
            
            elif op == 5:
                self.GetBooksWithPriceLowerThan()
            
            elif op == 6:
                self.GetBooksWithPriceHigherThan()
            


