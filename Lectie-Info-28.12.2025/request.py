import requests

# requests.post("http://127.0.0.1:5000/users", params={"username": "test2", "password": "parola", "email": "ds"})
requests.put("http://127.0.0.1:5000/users", params={"id" : 3, "username": "test2", "password": "parola", "email": "ds"})
