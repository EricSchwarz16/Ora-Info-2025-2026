from models import Medicine
from utils import *  # Import all utility functions for adding, deleting, updating, etc.

if __name__ == "__main__":
    medicine_inventory = []  # This is the inventory list where all medicines will be stored

    while True:
        print("""
            Choose the following operation:
            1: Add a medicine
            2: Delete medicine
            3: Update medicine
            4: See all available medicines containing a given string / all available medicines
            5: See all available medicines in short supply
            6: Undo and redo functionality
            7: Exit
        """)

        op = int(input())  # Get the user input for the desired operation

        if op == 1:
            # Add medicine
            name = input("Enter medicine name: ")
            concentration = int(input("Enter concentration (mg/tablet or mg/mL): "))
            quantity = int(input("Enter quantity (number of tablets or bottles): "))
            price = int(input("Enter price per unit: "))
            add_medicine(name, concentration, quantity, price, medicine_inventory)

        elif op == 2:
            # Delete medicine
            name = input("Enter medicine name to delete: ")
            concentration = int(input("Enter concentration (mg/tablet or mg/mL): "))
            delete_medicine(name, concentration, medicine_inventory)

        elif op == 3:
            # Update medicine
            name = input("Enter medicine name to update: ")
            concentration = int(input("Enter concentration (mg/tablet or mg/mL): "))
            quantity = int(input("Enter quantity to add: "))
            price = int(input("Enter price per unit: "))
            update_medicine(name, concentration, quantity, price, medicine_inventory)

        elif op == 4:
            # Search for medicines by name or see all available medicines
            search = input("Enter search string (leave empty to see all): ")
            result = get_medicines_by_name(search, medicine_inventory)
            if result:
                print("Found medicines:")
                for med in result:
                    print(med)
            else:
                print("No medicines found.")

        elif op == 5:
            # Short supply check
            threshold = int(input("Enter the quantity threshold to check short supply: "))
            result = get_short_supply_medicines(threshold, medicine_inventory)
            if result:
                print("Medicines in short supply:")
                for med in result:
                    print(med)
            else:
                print("No medicines in short supply.")

        elif op == 6:
            # Undo and redo functionality
            print("1: Undo")
            print("2: Redo")
            sub_op = int(input())

            
