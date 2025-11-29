class BookDateException(Exception):
    def __init__(self, message):
        self.message = message
    
    def __init__(self):
        self.message = "Anul este invalid"
        
    def __str__(self):
        return self.message