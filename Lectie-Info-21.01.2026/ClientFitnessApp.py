import requests
from datetime import datetime

urlActivities = "http://127.0.0.1:5000/activities"
urlActivity = "http://127.0.0.1:5000/activity"

r = requests.get(urlActivities)
cache = r.json()
print("Data was loaded:", cache)

while True:
    print("\n=== Fitness Tracker ===")
    print("Option 1: Get all activities")
    print("Option 2: Get activity by ID")
    print("Option 3: Add activity")
    print("Option 4: Delete activity")
    print("Option 5: Exit")
    
    option = input("Enter your option: ")
    
    if option == "1":
        print("\nAll activities:")
        for activity in cache:
            print(f"ID: {activity['id']}, Calories: {activity['calories']}, Duration: {activity['duration']} min, Date: {activity['date']}")
    
    elif option == "2":
        id = int(input("Enter activity ID: "))
        r = requests.get(urlActivity, params={"id": id})
        if r.status_code == 200:
            activity = r.json()
            print(f"\nActivity found: ID: {activity['id']}, Calories: {activity['calories']}, Duration: {activity['duration']} min, Date: {activity['date']}")
        else:
            print("Activity not found.")

    elif option == "3":
        calories = int(input("Calories burnt: "))
        duration = int(input("Duration (minutes): "))
        date = input("Date (DD-MM-YYYY) or press Enter for today: ")
        
        if not date:
            date = datetime.now().strftime("%d-%m-%Y")
        
        r = requests.post(urlActivity, json={"calories": calories, "duration": duration, "date": date})
        if r.status_code == 201:
            new_activity = r.json()
            cache.append(new_activity)
            print(f"Activity added successfully with ID: {new_activity['id']}")
        else:
            print("Failed to add activity.")
    
    elif option == "4":
        id = int(input("Enter activity ID to delete: "))
        r = requests.delete(urlActivity, params={"id": id})
        if r.status_code == 200:
            cache = [activity for activity in cache if activity['id'] != id]
            print("Activity deleted successfully.")
        else:
            print("Activity not found.")
    
    elif option == "5":
        print("Goodbye!")
        break
    
    else:
        print("Invalid option. Please try again.")
