## This file version adds a list to the class's data attributes and modifies the
# deposit and withdraw method to add transaction details to the list. This file will
# implement the 'pytz' and 'datetime' module for local time to capture the date and
# time of the transaction as well as the amount.
######################################################################################

import datetime
import pytz

class Account:
    """Simple account class with balance"""

    @staticmethod
    #A static method is shared by all instances of the class
    def _current_time():  # this is a Static Method
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            # self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))
            self.transaction_list.append((Account._current_time(), amount))
            #line 30 now uses the static method created on line 15


    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
            #line 37 now adds transaction date and time info for a withdrawl and we had to
            #negate the 'amount' value.
        else:
            print("You can't withdraw more than your account balance.")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))

    def show_transaction(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1  #this gives the amount to withdraw a negative value which will be deducted
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    sabrina = Account("Sabrina", 0)
    sabrina.show_balance()

    sabrina.deposit(1000)
    sabrina.withdraw(500)

    sabrina.show_transaction()
