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
    
    def deleteMedicine(self):
        name = input("Name of to be deleted medicine: ")
        self.service.deleteMedicine(name)


    def updateMedicine(self):
        name = input("Name of to be modified medicine: ")
        concentration = input("Concentration: ")
        quantity = input("Quantity: ")
        price = input("Price: ")
        self.service.updateMedicine(name, Medicine(name, concentration, quantity, price))

    def medicinesWithPriceLowerThan(self):
        price = input("Type in the reference price: ")
        self.printMedicines(self.service.getMedicinesWithAPriceLowerThan(price))


    def printMedicines(self, MedicineList : list[Medicine]):     # primeste ca parametru o lista de medicamente si o afiseaza
        
        if MedicineList:
            print("Found medicines:")
            for med in MedicineList:
                print(med)
        else:
            print("No medicines found.")
        

    
    def runUI(self):
        while True:
            print("""
Choose the following operation:
0: Exit
1: Add a medicine
2: Show all medicines
3: Delete a medicine
4: Update a medicine
5: Get all medicines with a price lower than
6: Undo
7: Redo
                """)

            op = int(input())  

            if op == 1:
                self.addMedicine()
            elif op == 2:
                self.printMedicines(self.service.getAllMedicines())
            elif op == 3:
                self.deleteMedicine()
            elif op == 4:
                self.updateMedicine()
            elif op == 5:
                self.medicinesWithPriceLowerThan()
            elif op == 6:
                self.service.Undo()
            elif op == 7:
                self.service.Redo()
            elif op == 0:
                break
