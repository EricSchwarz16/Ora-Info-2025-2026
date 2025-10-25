undo_stack = []
redo_stack = []

def get_medicines_by_name(search: str, medicine_inventory: list):
    # Save the state of the search operation to the undo stack
    undo_stack.append(('get_by_name', list(medicine_inventory), search))
    
    if not search:
        return medicine_inventory
    
    # Filter and sort medicines by name if search string is provided
    filtered_medicines = [med for med in medicine_inventory if search in med.name]
    sorted_medicines = sorted(filtered_medicines, key=lambda med: med.name)
    return sorted_medicines

def get_short_supply_medicines(threshold: int, medicine_inventory: list):
    # Save the state of the short supply operation to the undo stack
    undo_stack.append(('get_short_supply', list(medicine_inventory), threshold))
    
    return [med for med in medicine_inventory if med.quantity < threshold]

# Redo function now handles get_medicines_by_name and get_short_supply_medicines
def redo(medicine_inventory: list):
    if not redo_stack:
        print("No actions to redo.")
        return
    
    last_action, previous_state, *additional_args = redo_stack.pop()
    undo_stack.append((last_action, list(medicine_inventory), *additional_args))
    
    # Reapply the action (here, we handle each action type)
    if last_action == 'add':
        medicine_inventory.append(Medicine(previous_state[-1].name, previous_state[-1].concentration, previous_state[-1].quantity, previous_state[-1].price))
        print(f"Redo {last_action} operation: {previous_state[-1].name} added back.")

    elif last_action == 'delete':
        for med in previous_state:
            if med.name == previous_state[-1].name and med.concentration == previous_state[-1].concentration:
                medicine_inventory.remove(med)

        print(f"Redo {last_action} operation: {previous_state[-1].name} deleted again.")
    elif last_action == 'update':
        for med in medicine_inventory:
            if med.name == previous_state[-1].name and med.concentration == previous_state[-1].concentration:
                med.quantity = previous_state[-1].quantity
                med.price = previous_state[-1].price
        print(f"Redo {last_action} operation: {previous_state[-1].name} updated again.")

    elif last_action == 'get_by_name':
        search = additional_args[0]
        if not search:
            print(f"Redo {last_action} operation: Returning full inventory.")
            return medicine_inventory
        filtered_medicines = [med for med in medicine_inventory if search in med.name]
        sorted_medicines = sorted(filtered_medicines, key=lambda med: med.name)
        print(f"Redo {last_action} operation: Returning medicines by name for search '{search}'")
        return sorted_medicines
    
    elif last_action == 'get_short_supply':
        threshold = additional_args[0]
        short_supply_medicines = [med for med in medicine_inventory if med.quantity < threshold]
        print(f"Redo {last_action} operation: Returning short supply medicines with threshold {threshold}")
        return short_supply_medicines
