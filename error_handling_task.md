**Task Description: Secure Banking System**

**Requirements:**
1. Create a `BankAccount` class that represents a simple bank account.
2. Implement methods for deposit, withdrawal, and balance inquiry within the `BankAccount` class.
3. Use proper error handling to handle scenarios such as insufficient funds for withdrawals or invalid input types.
4. Utilize the `assert` method to check certain conditions within the class methods, such as ensuring that the balance is always non-negative.
5. Implement a method to display the account details, including the account holder's name and current balance.
6. Create a separate function outside the class to demonstrate the `BankAccount` class by performing various transactions and handling errors.

**Sub-Tasks: Error Handling in BankAccount Class**

1. **Negative Deposit:**
    - Implement error handling in the `deposit` method to ensure that the deposited amount is greater than zero. Raise an appropriate exception if the input is invalid.

2. **Negative Withdrawal:**
    - Implement error handling in the `withdraw` method to ensure that the withdrawal amount is greater than zero. Raise an appropriate exception if the input is invalid.

3. **Insufficient Funds:**
    - Modify the `withdraw` method to handle scenarios where the withdrawal amount is greater than the current balance. Raise an exception specifically for insufficient funds.

4. **Invalid Input Type:**
    - Implement error handling in the `deposit` and `withdraw` methods to ensure that the input amounts are of numeric type (int or float). Raise an exception if the input is not valid.

5. **Non-Negative Balance Assertion:**
    - Use the `assert` method to check within the `withdraw` method that the resulting balance after withdrawal is non-negative. If the balance becomes negative, raise an exception.

**Starter Code:**

```python
class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        # Sub-Task 1: Error Handling - Negative Deposit
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero")
        self.balance += amount

    def withdraw(self, amount):
        # Sub-Task 2: Error Handling - Negative Withdrawal
        # Sub-Task 3: Error Handling - Insufficient Funds
        # Sub-Task 5: Non-Negative Balance Assertion
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero")
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal")
        # Sub-Task 5: Non-Negative Balance Assertion
        assert (self.balance - amount) >= 0, "Balance should not be negative after withdrawal"
        self.balance -= amount

    def balance_inquiry(self):
        return self.balance

    def display_account_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}")

# Additional function to demonstrate the BankAccount class and error handling
def demonstrate_bank_account():
    # Create an instance of the BankAccount class
    account = BankAccount(account_holder="John Doe", initial_balance=1000.0)

    try:
        # Perform transactions
        account.deposit(500.0)
        account.withdraw(200.0)
        account.withdraw(900.0)  # This should raise an exception due to insufficient funds

        # Display account details
        account.display_account_details()

        # Add more test cases and assert statements here

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to demonstrate the BankAccount class
demonstrate_bank_account()
```

**Task Instructions (Updated):**

1. Complete the `deposit` method in the `BankAccount` class to handle negative deposit amounts and raise an exception for invalid inputs.
2. Update the `withdraw` method to handle negative withdrawal amounts, insufficient funds, and non-negative balance assertions using proper error handling.
3. Implement error handling in the `deposit` and `withdraw` methods to ensure that the input amounts are of numeric type (int or float).
4. In the `demonstrate_bank_account` function, create test cases to cover the error scenarios mentioned in the sub-tasks and print informative error messages.
5. Use `assert` statements within the class methods to check conditions related to the sub-tasks and ensure the correctness of the code.
