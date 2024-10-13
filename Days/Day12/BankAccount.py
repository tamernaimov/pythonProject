class BankAccount:
    def __init__(self,account_number,balance,owner):
        self.account_owner = account_number
        self.balance = balance
        self.owner = owner

        #Deposit,withdraw,get_balance
    def deposit(self,depositAmount):
        self.balance += depositAmount
    def withdraw(self,withdrawAmount):
        self.balance -= withdrawAmount
    def get_balance(self):
        return self.balance