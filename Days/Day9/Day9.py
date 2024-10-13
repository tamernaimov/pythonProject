#try:
    # Code that may raise an exception
    #risky_operation(4,0)
#except Exception as e:
    # Code that runs if an exception occurs
    #print(f"An error occurred: {e}")
from fileinput import filename
from secrets import choice
from sys import excepthook



def add(num1, num2):
    return num1 + num2

def multiply(num1, num2):
    return num1 * num2

def calc():
    print("Welcome to the calculator!")
    print("Choose an operation:")
    print("1: Addition")
    print("2: Multiplication")

    choice = input("Enter 1 or 2: ")

    # Validate the choice
    if choice not in ['1', '2']:
        print("Invalid choice! Please enter 1 for addition or 2 for multiplication.")
        return  # Exit the function if the choice is invalid

    # Get user input for the numbers
    try:
        num1 = float(input("Enter the first number: "))  # Convert input to float
        num2 = float(input("Enter the second number: "))  # Convert input to float
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return # Exit the function if input is invalid

    # Perform the selected operation
    if choice == '1':
        result = add(num1, num2)
        print(f"The result of {num1} + {num2} = {result}")
    elif choice == '2':
        result = multiply(num1, num2)
        print(f"The result of {num1} * {num2} = {result}")

# Call the calculator function
#calc()

def readFromFiles():
    try:
        with open("../../otherFiles/mama.txt", "r")as file:
            content = file.read()

    except FileNotFoundError as e:
        print(e)
    else:
        print(content)

readFromFiles()