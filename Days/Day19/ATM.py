from Days.Day19.Account import Account


class ATM():


    def display_options(self,account):
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        num = int(input())

        if num == 1:
            account.check_balance()
        elif num == 2:
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif num == 3:
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif num > 3 | num < 1:
            print("not correct input")
