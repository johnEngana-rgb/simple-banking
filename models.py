#models
class Account:
    def __init__(self, account_id, customer_id, account_number, balance=0.0):
        self.account_id = account_id
        self.customer_id = customer_id
        self.account_number = account_number
        self.balance = balance
    
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

class Customer:
    def __init__(self, customer_id, uuid, name, email, phone_number):
        self.customer_id = customer_id
        self.uuid = uuid
        self.name = name
        self.email = email
        self.phone_number = phone_number

