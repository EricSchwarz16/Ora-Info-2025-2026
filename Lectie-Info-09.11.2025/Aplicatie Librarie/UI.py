from service import *
from book_exceptions.book_date_exception import BookDateException

class UI2:
    def __init__(self):
        self.service = Service()        # Warum brauchen wir das ?
    
    def input_float(self, prompt):
        value = input(prompt).strip().replace(",", ".")
        return float(value)

    def AddBook(self):
        try:
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            DateOfPublic = int(input("Enter the date of publication for the book: ")) # poate pusca aici daca nu dam un int
            publisher = input("Enter the publisher for the book: ")
            price = self.input_float("Enter the price of the book in €: ")
            quantity = int(input("Enter quantity: "))
            self.service.AddBook(title, author, DateOfPublic, publisher, price, quantity)
        except ValueError as e:
            print(f"Enter valid fields for date and price: {e}")
        except (BookDateException, NegativeBookPrice, NegativeBookQuantity) as e:
            print(e)
    
    def DeleteBook(self):
        title = input("Title of to be deleted Book: ")
        author = input("Author of to be deleted Book: ")
        self.service.DeleteBook(title, author)
    
    def UpdateBook(self):
        # Identify old book
        title = input("Name of to be updated title: ")
        author = input("Name of to be updated author: ")

        # New book data
        title2 = input("Enter the title of the new book: ")
        author2 = input("Enter the author of the new book: ")
        DateOfPublic = int(input("Enter the date of publication for the new book: "))
        publisher = input("Enter the publisher for the new book: ")
        price = self.input_float("Enter the price of the new book in €: ")

        old_books = self.service.GetBooksByString("") 
        
        old_book = None

        for b in old_books:
            if b.title == title and b.author == author:
                old_book = b
                break

        if old_book is None:
            print("Book not found.")
            return

        if title2 == title and author2 == author:
            new_quantity = old_book.quantity + 1
        else:
            new_quantity = 1

        new_book = Book(title2, author2, DateOfPublic, publisher, price, new_quantity)
        self.service.UpdateBook(title, author, new_book)
        print("Book updated successfully.")

        
    
    def GetBooksByString(self):
        search_string = input("String to be used in searching: ")
        books = self.service.GetBooksByString(search_string)
        for b in books:
            print(b)
    
    def GetBooksWithPriceLowerThan(self):
        price = self.input_float("Name the price of reference in €: ")
        books = self.service.GetBooksByString(price)
        for b in books:
            print(b)
    
    def GetBooksWithPriceHigherThan(self):
        price = self.input_float("Name the price of reference in €: ")
        books = self.service.GetBooksByString(price)
        for b in books:
            print(b)
    
    def RunUI(self):
        while True:
            print("""
Choose the following operation:
0 : Exit
1 : Add a book
2 : Delete a book
3 : Update a book
4 : Get books by a search string or all of them when input string does not have any characters
5 : Get all books with a price lower than
6 : Get all books with a price higher than 
                  """
            )
            op = int(input())

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
            


