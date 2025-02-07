import random
from database import initialize_database
from accountRepository import AccountRepository
from services import AccountService, TransactionService, StatementService

def generate_numeric_uuid():
    """Generate a 16-digit numeric UUID."""
    return ''.join(str(random.randint(0, 9)) for _ in range(16))

def main():
    initialize_database()
    repository = AccountRepository()
    account_service = AccountService(repository)
    transaction_service = TransactionService(repository)
    statement_service = StatementService(repository)

    while True:
        print("\n1. Log in\n2. Create Account\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            uuid = input("Enter your 16-digit UUID: ")
            customer = repository.find_customer_by_uuid(uuid)

            if customer:
                print(f"\nHello {customer.name}!")
                while True:
                    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Generate Statement\n5. Logout")
                    user_choice = input("Choose an option: ")

                    if user_choice == "1":
                        account = repository.find_account_by_id(customer.customer_id)
                        if account:
                            print(f"Balance: ${account.get_balance()}")
                        else:
                            print("Account not found.")

                    elif user_choice == "2":
                        amount = float(input("Enter deposit amount: "))
                        if amount > 0:
                            transaction_service.make_transaction(customer.customer_id, amount, "deposit")
                            print(f"Successfully deposited ${amount}.")
                        else:
                            print("Invalid amount. Please enter a positive value.")

                    elif user_choice == "3":
                        amount = float(input("Enter withdrawal amount: "))
                        transaction_service.make_transaction(customer.customer_id, amount, "withdraw")

                    elif user_choice == "4":
                        print(statement_service.generate_account_statement(customer.customer_id))

                    elif user_choice == "5":
                        print("Logging out...")
                        break  # Logout

                    else:
                        print("Invalid option. Please try again.")

            else:
                print("Invalid UUID. Please try again.")

        elif choice == "2":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            phone_number = input("Enter your phone number: ")
            uuid = account_service.create_account(name, email, phone_number)
            print(f"Your unique 16-digit UUID is: {uuid}")

        elif choice == "3":
            print("Goodbye!")
            break  # Exit the program

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
