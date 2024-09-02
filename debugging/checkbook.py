#!/usr/bin/python3

class Checkbook:
    def __init__(self):
        """
        Initializes a new Checkbook instance with a starting balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits a specified amount into the checkbook and updates the balance.

        Args:
            amount (float): The amount of money to deposit. Should be positive.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the checkbook if sufficient funds are available.

        Args:
            amount (float): The amount of money to withdraw. Should be positive.
        """
        if amount > self.balance:
            # If there are insufficient funds, print an error message
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance of the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to interact with the user and perform checkbook operations.
    """
    cb = Checkbook()  # Create a new Checkbook instance
    while True:
        # Prompt the user for an action
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        
        if action.lower() == 'exit':
            # Exit the loop and end the program
            break
        elif action.lower() == 'deposit':
            try:
                # Prompt for the deposit amount and convert to float
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    # Check if the amount is positive
                    print("Please enter a positive amount.")
                else:
                    # Perform the deposit operation
                    cb.deposit(amount)
            except ValueError:
                # Handle invalid (non-numeric) input
                print("Invalid input. Please enter a numeric value.")
        elif action.lower() == 'withdraw':
            try:
                # Prompt for the withdrawal amount and convert to float
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    # Check if the amount is positive
                    print("Please enter a positive amount.")
                else:
                    # Perform the withdrawal operation
                    cb.withdraw(amount)
            except ValueError:
                # Handle invalid (non-numeric) input
                print("Invalid input. Please enter a numeric value.")
        elif action.lower() == 'balance':
            # Print the current balance
            cb.get_balance()
        else:
            # Handle invalid commands
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    # Run the main function if this script is executed
    main()
