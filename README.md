# Simple Banking

## Setup Guide

Follow these steps to set up and run the **Simple Banking** application.

### 1. Clone the Repository
First, clone the repository from your version control platform (GitHub, GitLab, etc.).
```sh
git clone <repository_url>
cd simple-banking
```

### 2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.
```sh
python -m venv venv
```

Activate the virtual environment:
- On Windows:
  ```sh
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```sh
  source venv/bin/activate
  ```


### 3. Initialize the Database
The application requires an SQLite database. Run the database initialization script:
```sh
python -c "from database import initialize_database; initialize_database()"
```
This will create the necessary tables:
- `customers`
- `accounts`
- `transactions`

### 4. Run the Application
Start the application by running:
```sh
python main.py
```

## Application Workflow

### 1. Creating an Account
- The user selects **Create Account**.
- The application asks for a name, email, and phone number.
- A **16-digit UUID** is generated for the user.
- The UUID and account details are stored in the database.
- The UUID is displayed, which will be used for logging in.

### 2. Logging In
- The user selects **Log in**.
- They enter their **16-digit UUID**.
- If valid, the system fetches and displays the user’s account information.

### 3. Banking Actions
After logging in, the user can:
- **Check Balance**: View their account balance.
- **Deposit**: Enter an amount to add funds to their account.
- **Withdraw**: Enter an amount to withdraw (if sufficient balance is available).
- **Generate Statement**: View a transaction history, displaying:
  ```
  Transaction | Amount | Date
  ```
- **Logout**: Exit the banking session.

### 4. Transactions and Statements
Each deposit or withdrawal is recorded in the `transactions` table, linked to the user’s `account_id`. The transaction history allows users to generate a statement showing all deposits and withdrawals sorted by date.

### 5. Exiting the Application
The user can exit at any time by selecting **Exit** in the main menu.

## Notes
- Ensure that the SQLite database file (`banking.db`) is properly created before running transactions.
- If you need to reset the database, delete `banking.db` and re-run the initialization script.

---
Enjoy using **Simple Banking**! 🚀

