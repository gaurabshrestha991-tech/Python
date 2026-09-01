#       BankAccount Class

class BankAccount:
    
    def __init__(self, balance=0):
        self.balance = balance
        
    def deposite(self, amount):
        self.balance += amount
        print("Amount Deposited: ", amount)
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn: ", amount)
        else:
            print("Insufficient balance")
        
    def check_balance(self):
        print("Total Balance: ", self.balance)
        
amount = BankAccount(100000)

amount.check_balance()
amount.deposite(50000)
amount.check_balance
amount.withdraw(100000)
amount.check_balance()
