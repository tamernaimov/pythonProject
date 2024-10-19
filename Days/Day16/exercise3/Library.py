from zoneinfo import available_timezones

from Days.Day16.exercise3.LibraryItem import LibraryItem
class Library():
    def __init__(self):
        self.items = []

    def addItem(self,library_item):
        self.items.append(library_item)

    def borrowItem(self,title):
        for i in range(len(self.items)):
            if self.items[i].title == title:
                self.items[i].is_available = False

    def returnItem(self,title):
        for i in range(len(self.items)):
            if self.items[i].title == title:
                self.items[i].is_available = True

    def displayAvaiableItems(self):
        avaiableItems = []
        for i in range(len(self.items)):
            if self.items[i].is_available == True:
                avaiableItems.append(self.items[i])

        for i in range(len(avaiableItems)):
            print(avaiableItems[i].title)


    def showItemDetails(self):
        for i in range(len(self.items)):
            self.items[i].showDetails()