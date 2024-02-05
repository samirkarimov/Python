class Book:
    def __init__(self, title, author, isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
class UsedBook:
    def __init__(self,title,author,isbn,age):
        pass    

class Library:
    def __init__(self):
        self.books=[]
        

    def add_book(self, book):
        self.books.append(book)
       

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn==isbn:
                self.books.remove(book)
       

    def display_books(self):
        for book in self.books:
            print(f"{book.title},{book.author},{book.isbn}")
        

# Menu-driven program to interact with the library
library = Library()

while True:
    print("\nLibrary Management System")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Display all books")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        t=input('Type book title: ')
        a=input('Type book author: ')
        i=input('Type book isbn: ')
        book=Book(t,a,i)
        library.add_book(book)
        
    elif choice == '2':
        isbn=input('Type wanted isbn number: ')
        library.remove_book(isbn)
    elif choice == '3':
        library.display_books()
        pass
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
