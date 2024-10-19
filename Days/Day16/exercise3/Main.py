from Days.Day16.exercise3.LibraryItem import LibraryItem
from Days.Day16.exercise3.Book import Book
from Days.Day16.exercise3.Magazine import Magazine
from Days.Day16.exercise3.Library import Library

favbook = Book("OhioBook!",2005,True,"Lionel Messi",43)
favmagazine = Magazine("oklahoma",2005,True,5681,"Haaland")
mortagonovo = Library()

mortagonovo.addItem(favbook)
mortagonovo.addItem(favmagazine)

mortagonovo.displayAvaiableItems()
mortagonovo.showItemDetails()