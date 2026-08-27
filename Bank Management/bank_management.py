# ==============================================================================
# BANK MANAGEMENT SYSTEM
# A simple terminal-based banking application written in Python.
# Features: Create Account, Deposit, Withdraw, Check Balance, View All Accounts.

import os
import json

# File where account data will be permanently saved
DATA_FILE = "bank_accounts.json"

def load_accounts():
    """Loads account data from the JSON file. Returns an empty dict if file missing."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}

def save_accounts(accounts):
    """Saves the current accounts dictionary to the JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(accounts, file, indent=4)

def create_account(accounts):
    """Registers a new user account with a unique account number."""
    print("\n--- CREATE NEW ACCOUNT ---")
    acc_num = input("Enter a unique account number: ").strip()
    
    if not acc_num:
        print("❌ Account number cannot be empty.")
        return
        
    if acc_num in accounts:
        print("❌ Account number already exists! Please try a different one.")
        return
        
    name = input("Enter account holder's name: ").strip()
    if not name:
        print("❌ Name cannot be empty.")
        return

    try:
        initial_deposit = float(input("Enter initial deposit amount ($): "))
        if initial_deposit < 0:
            print("❌ Initial deposit cannot be negative.")
            return
    except ValueError:
        print("❌ Invalid amount. Please enter a valid number.")
        return

    # Store account details
    accounts[acc_num] = {
        "name": name,
        "balance": initial_deposit
    }
    
    save_accounts(accounts)
    print(f"✅ Account successfully created for {name}!")

def deposit_money(accounts):
    """Deposits funds into an existing account."""
    print("\n--- DEPOSIT MONEY ---")
    acc_num = input("Enter account number: ").strip()
    
    if acc_num not in accounts:
        print("❌ Account not found.")
        return
        
    try:
        amount = float(input("Enter amount to deposit ($): "))
        if amount <= 0:
            print("❌ Deposit amount must be greater than zero.")
            return
    except ValueError:
        print("❌ Invalid amount. Please enter a valid number.")
        return

    accounts[acc_num]["balance"] += amount
    save_accounts(accounts)
    print(f"✅ successfully deposited ${amount:.2f}. New Balance: ${accounts[acc_num]['balance']:.2f}")

def withdraw_money(accounts):
    """Withdraws funds from an account if sufficient balance exists."""
    print("\n--- WITHDRAW MONEY ---")
    acc_num = input("Enter account number: ").strip()
    
    if acc_num not in accounts:
        print("❌ Account not found.")
        return
        
    try:
        amount = float(input("Enter amount to withdraw ($): "))
        if amount <= 0:
            print("❌ Withdrawal amount must be greater than zero.")
            return
    except ValueError:
        print("❌ Invalid amount. Please enter a valid number.")
        return

    if accounts[acc_num]["balance"] < amount:
        print("❌ Insufficient funds! Withdrawal denied.")
        return

    accounts[acc_num]["balance"] -= amount
    save_accounts(accounts)
    print(f"✅ Successfully withdrew ${amount:.2f}. Remaining Balance: ${accounts[acc_num]['balance']:.2f}")

def check_balance(accounts):
    """Displays the details and current balance of an account."""
    print("\n--- CHECK BALANCE ---")
    acc_num = input("Enter account number: ").strip()
    
    if acc_num not in accounts:
        print("❌ Account not found.")
        return
        
    acc = accounts[acc_num]
    print(f"👤 Account Holder: {acc['name']}")
    print(f"💰 Current Balance: ${acc['balance']:.2f}")

def display_all_accounts(accounts):
    """Lists all active accounts stored in the system."""
    print("\n--- ALL ACCOUNTS LIST ---")
    if not accounts:
        print("No active accounts found in the system.")
        return
        
    print(f"{'Acc No.':<15} {'Holder Name':<25} {'Balance':<15}")
    print("-" * 55)
    for acc_num, details in accounts.items():
        print(f"{acc_num:<15} {details['name']:<25} ${details['balance']:<15.2f}")

def main():
    """Main application control loop."""
    accounts = load_accounts()
    
    while True:
        print("\n" + "="*40)
        print("     🏦 MAIN BANKING MENU 🏦     ")
        print("="*40)
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View All Accounts")
        print("6. Exit")
        print("="*40)
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            create_account(accounts)
        elif choice == '2':
            deposit_money(accounts)
        elif choice == '3':
            withdraw_money(accounts)
        elif choice == '4':
            check_balance(accounts)
        elif choice == '5':
            display_all_accounts(accounts)
        elif choice == '6':
            print("\nThank you for using our Bank Management System. Have a Good Day!")
            break
        else:
            print("❌ Invalid selection. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
