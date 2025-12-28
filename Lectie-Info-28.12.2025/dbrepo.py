import sqlite3
from typing import Optional


class DbRepo:
    def __init__(self, db_path: str = "database.db"):
        self.db_path = db_path
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row  # permite acces prin nume de coloana
        self.cursor = self.connection.cursor()
        self.init_db()

    def init_db(self):
        """Initializeaza tabelele daca nu exista"""
        # Tabel pentru utilizatori
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INTEGER
            )
        """)

        # Tabel pentru produse
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER DEFAULT 0
            )
        """)

        # Tabel pentru comenzi
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                order_date TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (product_id) REFERENCES products(id)
            )
        """)

        self.connection.commit()

    # ==================== USERS ====================
    def add_user(self, name: str, email: str, age: Optional[int] = None) -> int:
        """Adauga un utilizator nou"""
        self.cursor.execute(
            "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
            (name, email, age)
        )
        self.connection.commit()
        return self.cursor.lastrowid

    def get_user(self, user_id: int) -> Optional[dict]:
        """Returneaza un utilizator dupa ID"""
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = self.cursor.fetchone()
        return dict(row) if row else None

    def get_all_users(self) -> list[dict]:
        """Returneaza toti utilizatorii"""
        self.cursor.execute("SELECT * FROM users")
        return [dict(row) for row in self.cursor.fetchall()]

    def update_user(self, user_id: int, name: str = None, email: str = None, age: int = None):
        """Actualizeaza un utilizator"""
        updates = []
        values = []
        if name:
            updates.append("name = ?")
            values.append(name)
        if email:
            updates.append("email = ?")
            values.append(email)
        if age is not None:
            updates.append("age = ?")
            values.append(age)

        if updates:
            values.append(user_id)
            query = f"UPDATE users SET {', '.join(updates)} WHERE id = ?"
            self.cursor.execute(query, values)
            self.connection.commit()

    def delete_user(self, user_id: int):
        """Sterge un utilizator"""
        self.cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.connection.commit()

    # ==================== PRODUCTS ====================
    def add_product(self, name: str, price: float, quantity: int = 0) -> int:
        """Adauga un produs nou"""
        self.cursor.execute(
            "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
            (name, price, quantity)
        )
        self.connection.commit()
        return self.cursor.lastrowid

    def get_product(self, product_id: int) -> Optional[dict]:
        """Returneaza un produs dupa ID"""
        self.cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        row = self.cursor.fetchone()
        return dict(row) if row else None

    def get_all_products(self) -> list[dict]:
        """Returneaza toate produsele"""
        self.cursor.execute("SELECT * FROM products")
        return [dict(row) for row in self.cursor.fetchall()]

    def update_product(self, product_id: int, name: str = None, price: float = None, quantity: int = None):
        """Actualizeaza un produs"""
        updates = []
        values = []
        if name:
            updates.append("name = ?")
            values.append(name)
        if price is not None:
            updates.append("price = ?")
            values.append(price)
        if quantity is not None:
            updates.append("quantity = ?")
            values.append(quantity)

        if updates:
            values.append(product_id)
            query = f"UPDATE products SET {', '.join(updates)} WHERE id = ?"
            self.cursor.execute(query, values)
            self.connection.commit()

    def delete_product(self, product_id: int):
        """Sterge un produs"""
        self.cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        self.connection.commit()

    # ==================== ORDERS ====================
    def add_order(self, user_id: int, product_id: int, quantity: int) -> int:
        """Adauga o comanda noua"""
        self.cursor.execute(
            "INSERT INTO orders (user_id, product_id, quantity) VALUES (?, ?, ?)",
            (user_id, product_id, quantity)
        )
        self.connection.commit()
        return self.cursor.lastrowid

    def get_order(self, order_id: int) -> Optional[dict]:
        """Returneaza o comanda dupa ID"""
        self.cursor.execute("SELECT * FROM orders WHERE id = ?", (order_id,))
        row = self.cursor.fetchone()
        return dict(row) if row else None

    def get_all_orders(self) -> list[dict]:
        """Returneaza toate comenzile"""
        self.cursor.execute("SELECT * FROM orders")
        return [dict(row) for row in self.cursor.fetchall()]

    def get_user_orders(self, user_id: int) -> list[dict]:
        """Returneaza comenzile unui utilizator"""
        self.cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        return [dict(row) for row in self.cursor.fetchall()]

    def delete_order(self, order_id: int):
        """Sterge o comanda"""
        self.cursor.execute("DELETE FROM orders WHERE id = ?", (order_id,))
        self.connection.commit()

    # ==================== UTILITY ====================
    def close(self):
        """Inchide conexiunea la baza de date"""
        self.connection.close()


# Exemplu de utilizare
if __name__ == "__main__":
    db = DbRepo()

    # Adauga utilizatori
    user_id = db.add_user("Ion Popescu", "ion@email.com", 25)
    print(f"Utilizator adaugat cu ID: {user_id}")

    # Adauga produse
    product_id = db.add_product("Laptop", 2500.99, 10)
    print(f"Produs adaugat cu ID: {product_id}")

    # Adauga comanda
    order_id = db.add_order(user_id, product_id, 2)
    print(f"Comanda adaugata cu ID: {order_id}")

    # Afiseaza toti utilizatorii
    print("\nToti utilizatorii:")
    for user in db.get_all_users():
        print(f"  {user}")

    # Afiseaza toate produsele
    print("\nToate produsele:")
    for product in db.get_all_products():
        print(f"  {product}")

    # Afiseaza toate comenzile
    print("\nToate comenzile:")
    for order in db.get_all_orders():
        print(f"  {order}")

    # Update utilizator
    db.update_user(user_id, age=26)
    print(f"\nUtilizator actualizat: {db.get_user(user_id)}")

    db.close()
