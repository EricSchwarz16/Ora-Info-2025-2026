from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

"""
GET
POST
PUT
PATCH
DELETE
"""

class DbRepo:   
    def __init__(self, db_path: str = "database.db"):
        self.db_path = db_path
    
    def get_connection(self):
        return sqlite3.connect(self.db_path)
    
    def get_events(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Events")
        return cursor.fetchall()
    
    def get_users(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users")
        return cursor.fetchall()
    
    def add_user(self, username, email, password):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        conn.commit()
    
    def update_user(self, id, username, email, password):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Users SET username = ?, email = ?, password = ? WHERE id = ?", (username, email, password, id))
        conn.commit()
        
    def delete_user(self, id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Users WHERE id = ?", (id,))
        conn.commit()
    
    def get_tickets(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Tickets")
        return cursor.fetchall()
    
    def get_user_orders(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM UserOrders")
        return cursor.fetchall()
        
data_base = DbRepo()

@app.route('/events', methods=['GET'])
def get_events():
    id = request.args.get('id')
    events = data_base.get_events()
    
    if id:
        events = [event for event in events if event[0] == int(id)]
        
    return jsonify(events)

@app.route('/users', methods=['GET'])
def get_users():
    users = data_base.get_users()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    name = request.args.get('username')
    email = request.args.get('email')
    password = request.args.get('password')

    print(name, email, password)
    data_base.add_user(name, email, password)
    return jsonify({"message": "Succes"}), 200

@app.route('/users', methods=['DELETE'])
def delete_user():
    id = request.args.get('id')
    data_base.delete_user(id)
    return jsonify({"message": "Succes"}), 200

@app.route('/users', methods=['PUT'])
def update_user():
    id = request.args.get('id')
    name = request.args.get('username')
    email = request.args.get('email')
    password = request.args.get('password')
    data_base.update_user(id, name, email, password)
    return jsonify({"message": "Succes"}), 200

@app.route('/tickets', methods=['GET'])
def get_tickets():
    tickets = data_base.get_tickets()
    return jsonify(tickets)

@app.route('/user_orders', methods=['GET'])
def get_user_orders():
    user_orders = data_base.get_user_orders()
    return jsonify(user_orders)

if __name__ == '__main__':
    app.run(debug=True)