import sqlite3
import random
from models import Account, Customer
import datetime

def generate_numeric_uuid():
    """Generate a unique 16-digit numeric UUID."""
    return ''.join(str(random.randint(0, 9)) for _ in range(16))

class AccountRepository:
    def __init__(self, db_path="banking.db"):
        """Initialize database connection."""
        self.db_path = db_path

    def _connect(self):
        """Creates a new database connection per transaction to avoid concurrency issues."""
        return sqlite3.connect(self.db_path)

    def save_customer(self, customer):
        uuid = generate_numeric_uuid()
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO customers (uuid, name, email, phone_number) VALUES (?, ?, ?, ?)",
            (uuid, customer.name, customer.email, customer.phone_number)
        )
        conn.commit()
        customer_id = cursor.lastrowid
        conn.close()
        return customer_id, uuid  

    def find_customer_by_uuid(self, uuid):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT customer_id, uuid, name, email, phone_number FROM customers WHERE uuid = ?", (uuid,))
        row = cursor.fetchone()
        conn.close()
        return Customer(*row) if row else None

    def find_customer_by_id(self, customer_id):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT customer_id, uuid, name, email, phone_number FROM customers WHERE customer_id = ?", (customer_id,))
        row = cursor.fetchone()
        conn.close()
        return Customer(*row) if row else None

    def save_account(self, account):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO accounts (customer_id, account_number, balance) VALUES (?, ?, ?)",
            (account.customer_id, account.account_number, account.balance)
        )
        conn.commit()
        account_id = cursor.lastrowid
        conn.close()
        return account_id

    def find_account_by_id(self, account_id):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT account_id, customer_id, account_number, balance FROM accounts WHERE account_id = ?", (account_id,))
        row = cursor.fetchone()
        conn.close()
        return Account(*row) if row else None

    def find_accounts_by_customer_id(self, customer_id):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT account_id, customer_id, account_number, balance FROM accounts WHERE customer_id = ?", (customer_id,))
        rows = cursor.fetchall()
        conn.close()
        return [Account(*row) for row in rows]

    def update_account_balance(self, account):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE accounts SET balance = ? WHERE account_id = ?", 
            (account.balance, account.account_id)
        )
        conn.commit()
        conn.close()

    def save_transaction(self, account_id, transaction_type, amount):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO transactions (account_id, transaction_type, amount) VALUES (?, ?, ?)",
            (account_id, transaction_type, amount)
        )
        conn.commit()
        conn.close()

    def get_transactions_by_account_id(self, account_id):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT transaction_type, amount, transaction_date FROM transactions WHERE account_id = ? ORDER BY transaction_date DESC",
            (account_id,)
        )
        
        transactions = cursor.fetchall()
        
        conn.close()
        return transactions

    def save_transaction(self, account_id, transaction_type, amount):
        conn = self._connect()
        cursor = conn.cursor()

        transaction_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get current timestamp
        
        cursor.execute(
            "INSERT INTO transactions (account_id, transaction_type, amount, transaction_date) VALUES (?, ?, ?, ?)",
            (account_id, transaction_type, amount, transaction_date)
        )

        conn.commit()  # Ensure transaction is saved
        conn.close()
