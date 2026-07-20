class BankAccount:
    def __init__(self):
        self.__balance = 1000

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance:", self.__balance)

account = BankAccount()
account.deposit(500)
account.show_balance()