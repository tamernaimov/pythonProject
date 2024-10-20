class User():
    def __init__(self,name):
        self.__name = name
        self.__password = "aaa"

    def getPassword(self):
        return self.__password

