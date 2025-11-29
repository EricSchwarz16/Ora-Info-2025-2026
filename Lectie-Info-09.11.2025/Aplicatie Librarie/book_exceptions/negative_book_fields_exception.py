class NegativeBookPrice(Exception):
    def __init__(self, message):
        self.message = message
    
    def __init__(self):
        self.message = "Pretul este negativ, trebuie sa fie > 0"
        
    def __str__(self):
        return self.message
    
class NegativeBookQuantity(Exception):
    def __init__(self, message):
        self.message = message
    
    def __init__(self):
        self.message = "Cantitatea este negativa, trebuie sa fie > 0"
        
    def __str__(self):
        return self.message