from models import Medicine

undo_stack = []
redo_stack = []

def add_medicine(name: str, concentration: int, quantity: int, price: int, medicine_inventory: list):
    # Save current state to undo stack before operation
    undo_stack.append(('add', list(medicine_inventory)))
    
    medicine_to_be_added = Medicine(name, concentration, quantity, price)

    for med in medicine_inventory:
        if med.name == medicine_to_be_added.name and med.concentration == medicine_to_be_added.concentration:
            update_medicine(name, concentration, quantity + med.quantity, med.price, medicine_inventory)
            return
    
    medicine_inventory.append(medicine_to_be_added)
    redo_stack.append(('add', list(medicine_inventory)))
    print(f"Medicine '{name}' added successfully!")

def delete_medicine(name: str, concentration: int, medicine_inventory: list):
    # Save current state to undo stack before operation
    undo_stack.append(('delete', list(medicine_inventory)))
    redo_stack.append(('delete', list(medicine_inventory)))
    
    for med in medicine_inventory:
        if med.name == name and med.concentration == concentration:
            medicine_inventory.remove(med)
            print(f"Medicine '{name}' removed successfully.")
            return
    
    print("Medicine not found for deletion.")
    redo_stack.append(('add', list(medicine_inventory)))

def update_medicine(name: str, concentration: int, quantity: int, price: int, medicine_inventory: list):
    undo_stack.append(('update', list(medicine_inventory)))
    
    for med in medicine_inventory:
        if med.name == name and med.concentration == concentration: 
            med.quantity = med.quantity + quantity
            med.price = price
            print(f"Medicine '{med.name}' updated successfully!")
            return  
    
    print("Medicine not found for update.")
    redo_stack.append(('update', list(medicine_inventory)))

def get_medicines_by_name(search: str, medicine_inventory: list):
    undo_stack.append(('get_by_name', list(medicine_inventory)))
    
    if not search:
        return medicine_inventory
      
    filtered_medicines = [med for med in medicine_inventory if search in med.name]
    sorted_medicines = sorted(filtered_medicines, key=lambda med: med.name)
    redo_stack.append(('get_by_name', list(medicine_inventory), search))
    return sorted_medicines

def get_short_supply_medicines(threshold: int, medicine_inventory: list):
    
    undo_stack.append(('get_short_supply', list(medicine_inventory)))
    redo_stack.append(('get_short_supply', list(medicine_inventory), threshold))
    
    return [med for med in medicine_inventory if med.quantity < threshold]


def undo(medicine_inventory: list):
    if not undo_stack:
        print("No actions to undo.")
        return
    
    last_action, previous_state = undo_stack.pop()
    redo_stack.pop()
    
    medicine_inventory[:] = previous_state
    print(f"Undo {last_action} operation.")

def redo(medicine_inventory: list):
    if not redo_stack:
        print("No actions to redo.")
        return
    
    last_action, previous_state, *additional_args = redo_stack[-1]
    
    if last_action == 'add':
        medicine_inventory.append(Medicine(previous_state[-1].name, previous_state[-1].concentration, previous_state[-1].quantity, previous_state[-1].price))
        print(f"Redo {last_action} operation: {previous_state[-1].name} added again.")

    elif last_action == 'delete':
        for med in previous_state:
            if med.name == previous_state[-1].name and med.concentration == previous_state[-1].concentration:
                medicine_inventory.remove(med)
        print(f"Redo {last_action} operation: {previous_state[-1].name} deleted.")

    elif last_action == 'get_by_name':
        search = additional_args[0]
        if not search:
            print(f"Redo {last_action} operation: Returning full inventory.")
            return medicine_inventory
        filtered_medicines = [med for med in medicine_inventory if search in med.name]
        sorted_medicines = sorted(filtered_medicines, key=lambda med: med.name)
        print(f"Redo {last_action} operation: Returning medicines by name for search '{search}'")
        result = get_medicines_by_name(search, medicine_inventory)
        if result:
            print("Found medicines:")
            for med in result:
                print(med)
        else:
            print("No medicines found.")
        return sorted_medicines
    
    elif last_action == 'get_short_supply':
        threshold = additional_args[0]
        short_supply_medicines = [med for med in medicine_inventory if med.quantity < threshold]
        print(f"Redo {last_action} operation: Returning short supply medicines with threshold {threshold}")
        return short_supply_medicines