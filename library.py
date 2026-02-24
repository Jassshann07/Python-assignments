class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - [{status}]"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print(f"Book added: {title}")

    def display_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("\n--- Library Catalog ---")
            for book in self.books:
                print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_available:
                    book.is_available = False
                    print(f"You have successfully borrowed '{book.title}'.")
                    return
                else:
                    print(f"Sorry, '{book.title}' is already borrowed.")
                    return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_available:
                    book.is_available = True
                    print(f"You have successfully returned '{book.title}'.")
                    return
                else:
                    print(f"'{book.title}' was already in the library.")
                    return
        print(f"Book '{title}' does not belong to this library.")

def main():
    my_library = Library()
    
    
    my_library.add_book("Bad Guyzzz", "Jashanvir Singh", "6969")
    my_library.add_book("2023", "Rohit Sharma", "49")

    while True:
        print("\n--- Library Menu ---")
        print("1. View All Books")
        print("2. Add a New Book")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            my_library.display_books()
        elif choice == '2':
            t = input("Enter Title: ")
            a = input("Enter Author: ")
            i = input("Enter ISBN: ")
            my_library.add_book(t, a, i)
        elif choice == '3':
            t = input("Enter the title of the book to borrow: ")
            my_library.borrow_book(t)
        elif choice == '4':
            t = input("Enter the title of the book to return: ")
            my_library.return_book(t)
        elif choice == '5':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()