from models import *

class BookUtils:
    def __init__(self):
        pass
    
    def getBookFromLine(text: str) -> Book:
        details = text.split("|")
        title = details[0]
        author = details[1]
        DateOfPublic = int(details[2])
        publisher = details[3]
        price = float(details[4])
        quantity = int(details[5])
        
        return Book(title, author, DateOfPublic, publisher, price, quantity, isFromLoad=True)