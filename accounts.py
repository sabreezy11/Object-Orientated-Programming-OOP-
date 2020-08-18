class Account:
    """Simple account class with balance"""

    def __init__(self, name, balance): #__init__ is used to initialize a class
        self.name = name
        self.balance = balance
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount #adding 'amount' to 'balance'
            self.show_balance()

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount #deducting 'amount' from 'balance'
        else:
            print("You can't withdraw more than your account balance.")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))


if __name__ == '__main__':
    sabrina = Account("Sabrina", 0)
    sabrina.show_balance()

    sabrina.deposit(1000)
    # sabrina.show_balance()  ##this is now implemented in 'deposit' method

    sabrina.withdraw(1500)
    # sabrina.show_balance()  ##this is now implemented in 'withdraw' method


