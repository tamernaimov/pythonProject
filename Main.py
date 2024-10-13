from Days.Day12.BankAccount import BankAccount
from Days.Day12.Car import Car
from Days.Day12.Student import Student

print("EXERCISE 1:")
student = Student("Maria",15,10)
student.displayInfo()
print()
print("EXERCISE 2:")
homeCar = Car("Toyota","Tasd",2131)
homeCar.printStats()
homeCar.update_year(2005)
homeCar.printStats()

print("EXERCISE 3:")
bankAccount = BankAccount(1287057,10000,"Maria")
print(bankAccount.get_balance())
bankAccount.withdraw(1000)
print(bankAccount.get_balance())
bankAccount.deposit(10000)
print(bankAccount.get_balance())