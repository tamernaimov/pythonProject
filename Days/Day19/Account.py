class Account():
    def __init__(self,balance):
        self.__balance = balance


    def get_balance(self):
        return self.__balance
    def set_balance(self,money):
        self.__balance = money
        return self.__balance

    def check_balance(self):
        print(self.__balance)

    def deposit(self,amount):
        self.__balance +=amount
        return self.__balance
    def withdraw(self,amount):
        if(amount > self.__balance):
            print("you cant withdraw that much!")
        else:
            self.__balance -= amount
        return self.__balance