class Book:
    def __init__(self, title, author, isbn):
        # TODO: Initialize attributes (Title, Author, ISBN)
        pass

class Library:
    def __init__(self):
        # TODO: Initialize the book collection (use a list)
        pass

    def add_book(self, book):
        # TODO: Implement the method to add a book to the library
        pass

    def remove_book(self, isbn):
        # TODO: Implement the method to remove a book from the library
        pass

    def display_books(self):
        # TODO: Implement the method to display all books in the library
        pass

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
        # TODO: Ask the user for book details and add the book to the library
        pass
    elif choice == '2':
        # TODO: Ask the user for the ISBN and remove the book from the library
        pass
    elif choice == '3':
        # TODO: Display all books in the library
        pass
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
