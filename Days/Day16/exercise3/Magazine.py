from Days.Day16.exercise3.LibraryItem import LibraryItem

class Magazine(LibraryItem):
    def __init__(self,title,year,is_available,issue_number,publisher):
        super().__init__(title,year,is_available)
        self.issue_number = issue_number
        self.publisher = publisher

    def showDetails(self):
        print(f"title: {self.title}")
        print(f"year: {self.year}")
        print(f"is_available: {self.is_available}")
        print(f"author: {self.issue_number}")
        print(f"number of pages: {self.publisher}")
