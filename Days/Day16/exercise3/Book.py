from Days.Day16.exercise3.LibraryItem import LibraryItem

class Book(LibraryItem):
    def __init__(self,title,year,is_available,author,number_of_pages):
        super().__init__(title,year,is_available)
        self.author = author
        self.number_of_pages = number_of_pages

    def showDetails(self):
        print(f"title: {self.title}")
        print(f"year: {self.year}")
        print(f"is_available: {self.is_available}")
        print(f"author: {self.author}")
        print(f"number of pages: {self.number_of_pages}")
        print()
        print()
        print()
        print()
        print()
        print()