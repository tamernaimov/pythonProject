import string
import time


class password():
    def crackPassword(self,passw):

        temp = ""
        for ch in passw:
            for i in string.printable:
                if i == ch:
                    time.sleep(0.01)
                    print("No match found!")
                    temp += ch
                    break
                elif i != ch:
                    time.sleep(0.01)
                    print("No match found!")

            if passw == temp:
                print("PASSWORD FOUND")
                print("***********")
                print(passw)
