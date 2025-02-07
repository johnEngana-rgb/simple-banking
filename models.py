#models
class Account:
    def __init__(self, account_id, customer_id, account_number, balance):
        self.account_id = account_id
        self.customer_id = customer_id
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance


class Customer:
    def __init__(self, customer_id, uuid, name, email, phone_number):
        self.customer_id = customer_id
        self.uuid = uuid
        self.name = name
        self.email = email
        self.phone_number = phone_number

