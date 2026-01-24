import sqlite3

class DbRepo:   
    def __init__(self, db_path: str = "sqlite3.db"):
        self.db_path = db_path
    
    def get_connection(self):
        return sqlite3.connect(self.db_path)
    
    def get_chat_messages(self, id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ChatMessage WHERE chat_id = ?", (id,))
        return cursor.fetchall()
    
    def add_chat_message(self, content, sender_id, chat_id, timestamp):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ChatMessage (content, sender_id, chat_id, timestamp) VALUES (?, ?, ?, ?)", (content, sender_id, chat_id, timestamp))
        conn.commit()
    
    """
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
    """