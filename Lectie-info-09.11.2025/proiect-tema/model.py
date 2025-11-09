class Medicine:
    def __init__(self, name, concentration, quantity, price):
        self.name = name
        self.concentration = concentration
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"{self.name}|{self.concentration}|{self.quantity}|{self.price}"
    
    def __str__(self):
        return f"{self.name}|{self.concentration}|{self.quantity}|{self.price}"
    
    def __eq__(self, other):
        return self.name == other.name
