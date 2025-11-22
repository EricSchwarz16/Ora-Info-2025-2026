class Book:
    def __init__(self, title, author, DateOfPublish, publisher, price, quantity):
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
