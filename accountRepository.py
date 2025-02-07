#accountRepository
import sqlite3
from models import Account, Customer
import random

def generate_numeric_uuid():
    """Generate a unique 16-digit numeric UUID."""
    return ''.join(str(random.randint(0, 9)) for _ in range(16))

class AccountRepository:
    def __init__(self):
        self.conn = sqlite3.connect("banking.db")
        self.cursor = self.conn.cursor()
    
    def save_customer(self, customer):
        uuid = generate_numeric_uuid()
        self.cursor.execute(
            "INSERT INTO customers (uuid, name, email, phone_number) VALUES (?, ?, ?, ?)",
            (uuid, customer.name, customer.email, customer.phone_number)
        )
        self.conn.commit()
        return self.cursor.lastrowid, uuid  # Return customer_id and generated UUID

    def find_customer_by_uuid(self, uuid):
        self.cursor.execute("SELECT * FROM customers WHERE uuid = ?", (uuid,))
        row = self.cursor.fetchone()
        if row:
            return Customer(*row)
        return None
    
    def save_account(self, account):
        self.cursor.execute(
            "INSERT INTO accounts (customer_id, account_number, balance) VALUES (?, ?, ?)",
            (account.customer_id, account.account_number, account.balance)
        )
        self.conn.commit()
        return self.cursor.lastrowid
    
    def find_account_by_id(self, account_id):
        self.cursor.execute("SELECT * FROM accounts WHERE account_id = ?", (account_id,))
        row = self.cursor.fetchone()
        if row:
            return Account(*row)
        return None
    
    def find_customer_by_id(self, customer_id):
        self.cursor.execute("SELECT * FROM customers WHERE customer_id = ?", (customer_id,))
        row = self.cursor.fetchone()
        if row:
            return Customer(*row)
        return None
    
    def update_account_balance(self, account):
        self.cursor.execute(
            "UPDATE accounts SET balance = ? WHERE account_id = ?", 
            (account.balance, account.account_id)
        )
        self.conn.commit()

    def save_transaction(self, account_id, transaction_type, amount):
        self.cursor.execute(
            "INSERT INTO transactions (account_id, transaction_type, amount) VALUES (?, ?, ?)",
            (account_id, transaction_type, amount)
        )
        self.conn.commit()

    def get_transactions_by_account_id(self, account_id):
        self.cursor.execute(
            "SELECT transaction_type, amount FROM transactions WHERE account_id = ?", 
            (account_id,)
        )
        return self.cursor.fetchall()
