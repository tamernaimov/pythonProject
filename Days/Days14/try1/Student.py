class Student():
    def __init__(self,name,grade):
        self.__name = name
        self.__grade = grade

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name
        return self.__name

    def get_grade(self):
        return self.__grade

    def set_grade(self,grade):
        self.__grade = grade
        return self.__grade


    #class Appliance with abstract methods turn_on() and turn_off().Then, implement concrete classes WashingMachine and
    # Refrigerator that inherit from Appliance and provide their specific implementations.


