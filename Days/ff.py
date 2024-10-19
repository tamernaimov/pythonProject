import string
import time

password = "afnadksnfkjadsnfkjasdnfkj"
temp = ""
for ch in password:
    for i in string.printable:
        if i == ch:
            time.sleep(0.01)
            print("No match found!")
            temp += ch
            break
        elif i!= ch:
            time.sleep(0.01)
            print("No match found!")

    if password == temp:
        print("PASSWORD FOUND")
        print("***********")
        print(password)