from service import *

class UI:
    def __init__(self):
        self.service = Service()
        
    def addMedicine(self):
        name = input("Enter medicine name: ")
        concentration = int(input("Enter concentration (mg/tablet or mg/mL): "))
        quantity = int(input("Enter quantity (number of tablets or bottles): "))
        price = int(input("Enter price per unit: "))
        self.service.addMedicine(Medicine(name, concentration, quantity, price))
    
    def get_medicines(self):
        result = self.service.getAllMedicines()
        
        if result:
            print("Found medicines:")
            for med in result:
                print(med)
        else:
            print("No medicines found.")

    
    def runUI(self):
        while True:
            print("""
                Choose the following operation:
                1: Add a medicine
                2: Show all medicines
                """)

            op = int(input())  

            if op == 1:
                self.addMedicine()
            elif op == 2:
                self.get_medicines()