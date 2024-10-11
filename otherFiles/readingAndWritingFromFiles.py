from gettext import gettext


with open('ex1', 'w') as file:
    file.write("Apple \nBanana \nCherry")


with open('ex1', 'r') as file:
    content = file.read()
    print(content)

with open('ex1', 'a') as file:
    file.write("\nmango")


print("dada")
