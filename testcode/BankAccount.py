class BankAccount:
    def __init__(self):
        self.__balance=0

    def deposit(self, amount):
        if amount > 0:
            self.__balance+=amount
            print(f"Deposited: ${amount}. New balance:#{self.__balance}")
        else:
            print("Deposit amount must be positive.")


    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew:${amount}. New balance:${self.__balance}")
        else:
            print("There should be money to withdraw")


my_account = BankAccount()
my_account.deposit(100)
my_account.deposit(150)
my_account.withdraw(50)
my_account.withdraw(300)  # This should print an error message
my_account.withdraw(-20)  # This should also print an error message