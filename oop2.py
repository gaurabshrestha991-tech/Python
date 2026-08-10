class BankAccount:
    def __init__(self, owner_name, phone_no, deposit=0):
        self.owner_name = owner_name # self -> object ,owner_name attribute 
        self.__phone_no = phone_no
        self.bank_name  = "ABC Bank"

        if BankAccount.is_valid_amount(deposit):
            self.__balance = deposit
        else:
            print("Deposit amount must be a positive value. Initializing to 0.")
            self.__balance = 0

    @property
    def phone_no(self):  # getter
        return f'{"X" * 7}{self.__phone_no[-3:]}'

    @property
    def balance(self):  # getter
        return self.__balance

    @balance.setter
    def balance(self, new_amount):
        if BankAccount.is_valid_amount(new_amount):
            self.__balance = new_amount
            print("Amount changed successfully!")
        else:
            print("Amount is Invalid")
  

    @staticmethod
    def is_valid_amount(amount): # is_valid_amount -> called as methods
        if amount < 0:
            return False
        return True

    def show_info(self):
        print(f"""
----------- Bank Account -----------
Owner Name = {self.owner_name}
Phone Number = {self.phone_no}
Current Balance = {self.balance}
Bank name = {self.bank_name}
------------------------------------
""")

    def __str__(self):
        return f"BankAccount(Owner: {self.owner_name}, Phone: {self.phone_no}, Balance: {self.balance})"


ram_account = BankAccount("Ram", "9816691655", 20000)

# ram_account.show_info()

# ram_account.__balance = -10000 This is showing you can't directly access private attributes. 

# print(ram_account.__balance)

# print(ram_account.__dict__) # Name mangling -> changing private attribute name

# ram_account.balance

# print(ram_account)

ram_account.show_info()
ram_account.balance = 1000

ram_account.show_info()

#Encapsulation -> keeping data members and operations and actions in packed in same place, 
# and protectiing data from garbage values using access modifiers
