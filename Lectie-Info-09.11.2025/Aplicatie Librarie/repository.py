from models import Book

class Repository:
    def __init__ (self):
        self.BookList = []
        self.LoadData()
    
    def AddBook(self, b : Book):
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
        
        self.saveData()
    
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


class TxtRepository(Repository):
    def __init__(self, file : str):
        self.file = file
        super().__init__()
    
    def SaveData(self):
        pass

    def LoadData(self):
        with open(self.file) as file:
            for line in file:
                details = line.split("|")
                title = details[0]
                author = details[1]
                DateOfPublic = details[2]
                publisher = details[3]
                price = float(details[4])
                quantity = int(details[5])

                self.BookList.append(Book(title, author, DateOfPublic, publisher, price, quantity))
