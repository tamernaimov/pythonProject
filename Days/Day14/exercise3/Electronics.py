class Electronics():
    def __init__(self,year,model):
        self.__year = year
        self.__model = model

    def get_year(self):
        return self.__year

    def set_year(self,newyear):
        self.__year = newyear
        return self.__year

    def get_model(self):
        return self.__model

    def set_model(self, newmodel):
        self.__model = newmodel
        return self.__model


