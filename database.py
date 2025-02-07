import sqlite3

def initialize_database():
    conn = sqlite3.connect("banking.db")
    cursor = conn.cursor()
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            uuid TEXT UNIQUE NOT NULL,  -- 16-digit unique number as TEXT
            name TEXT,
            email TEXT,
            phone_number TEXT
        )
    """)

    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS accounts (
            account_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            account_number TEXT UNIQUE,
            balance REAL,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    """)
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INTEGER,
            transaction_type TEXT,
            amount REAL,
            FOREIGN KEY (account_id) REFERENCES accounts(account_id)
        )
    """)
    conn.commit()
    conn.close()
