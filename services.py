#services
from models import Account, Customer

class AccountService:
    def __init__(self, repository):
        self.repository = repository
    
    def create_account(self, name, email, phone_number):
        customer = Customer(None, None, name, email, phone_number)
        customer_id, uuid = self.repository.save_customer(customer)  # Get customer_id and UUID

        account_number = f"ACCT{customer_id:04d}"
        account = Account(None, customer_id, account_number, 0.0)
        account_id = self.repository.save_account(account)

        print(f"Account created successfully! Your account number is: {account_number}")
        print(f"Your 16-digit UUID is: {uuid}")  # Show UUID for login

        return uuid  # Return UUID for future lookups


class TransactionService:
    def __init__(self, repository):
        self.repository = repository

    def make_transaction(self, account_id, amount, transaction_type):
        account = self.repository.find_account_by_id(account_id)
        if not account:
            print("Account not found.")
            return False

        if transaction_type == "deposit":
            success = account.deposit(amount)
        elif transaction_type == "withdraw":
            success = account.withdraw(amount)
        else:
            print("Invalid transaction type.")
            return False

        if success:
            self.repository.update_account_balance(account)
            self.repository.save_transaction(account.account_id, transaction_type, amount)
            print(f"{transaction_type.capitalize()} of ${amount} successful.")
        else:
            print(f"{transaction_type.capitalize()} failed.")



class StatementService:
    def __init__(self, repository):
        self.repository = repository
    
    def generate_account_statement(self, account_id):
        transactions = self.repository.get_transactions_by_account_id(account_id)

        if not transactions:
            return "No transactions found."

        statement = "Transaction | Amount | Date\n"
        statement += "-" * 40 + "\n"  # Divider line

        for transaction_type, amount, transaction_date in transactions:
            statement += f"{transaction_type.capitalize():<12} | ${amount:<6.2f} | {transaction_date}\n"

        return statement

