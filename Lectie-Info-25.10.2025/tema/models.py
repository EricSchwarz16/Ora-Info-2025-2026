class Medicine:
    def __init__(self, name, concentration, quantity, price):
        self.name = name
        self.concentration = concentration
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"{self.name} | {self.concentration} mg | {self.quantity} units | ${self.price} each"
