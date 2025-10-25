from models import Medicine

def add_medicine(name : str, concentration : int, quantity : int, price : int, medicine_Inventory: list):
    medicine_to_be_added = Medicine(name, concentration, quantity, price)

    for med in medicine_Inventory:
        if med.name == medicine_to_be_added.name and med.concentration == medicine_to_be_added.concentration:
            update_medicine(name, concentration, quantity + med.quantity, med.price, medicine_Inventory)
            return
    
        medicine_Inventory.append(medicine_to_be_added)

def delete_medicine(name: str, concentration: int, medicine_inventory: list):
    for med in medicine_inventory:
        if med.name == name and med.concentration == concentration:
            medicine_inventory.remove(med)
            print(f"Medicine '{name}' removed successfully.")
            return
        
    print("Medicine not found for deletion.")

def update_medicine(name: str, concentration: int, quantity: int, price: int, medicine_inventory: list):
    """
    Updates an existing medicine in the inventory with the given parameters (name, concentration, quantity, price).
    The existing medicine is found using its name and concentration and updated with the new values.
    """
    for med in medicine_inventory:
        if med.name == name and med.concentration == concentration: 
            med.quantity = med.quantity + quantity
            med.price = price
            print(f"Medicine '{med.name}' updated successfully!")
            return  # Stop after updating

    print("Medicine not found for update.")

        

            



