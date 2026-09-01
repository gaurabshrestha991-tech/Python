class LibraryBooks:
    def __init__(self, title):
        self.title = title
        self.is_issued = False
        
    def issue_book(self):
        if not self.is_issued:
            self.is_issued = True
            print("Book issued: ", self.title)
        else:
            print("Book is already issued")
            
    def return_book(self):
        if self.is_issued:
           self.is_issued = False
           print("Book returned: ", self.title)
        else:
            print("Book was not issued")
            
book = LibraryBooks("Python Programming")

book.issue_book()
book.return_book()
book.return_book()
                
