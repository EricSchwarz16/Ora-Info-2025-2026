import requests
urlFees = "http://127.0.0.1:5000/fees"
urlFee = "http://127.0.0.1:5000/fee"
r = requests.get(urlFees)

cache = r.json()
print("Data was loaded:", cache)

while(True):
    print("Option 1: Get all fees")
    print("Option 2: Get fee by ID")
    print("Option 3: Add fee")
    print("Option 4: Delete fee")
    
    option = input("Enter your option: ")
    
    if option == "1":
        print(cache)
    if option == "3":
        id = int(input("id: "))
        date = input("date: ")
        value = input("value: ")
        requests.post(urlFee, json={"id": id, "date": date, "value": value})
        cache.append({"id": id, "date": date, "value": value})
        
        
