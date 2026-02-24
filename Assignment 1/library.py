#Jash's Library 
class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"

class Library:
    def __init__(self):
        self.books = {}  # Store books with book_id as key

    def add_book(self, title, author, book_id):
        if book_id in self.books:
            print(f"Error: Book ID {book_id} already exists.")
        else:
            new_book = Book(title, author, book_id)
            self.books[book_id] = new_book
            print(f"Book '{title}' added successfully!")

    def display_books(self):
        if not self.books:
            print("The library is currently empty.")
        else:
            print("\n--- Library Collection ---")
            for book in self.books.values():
                print(book)

    def borrow_book(self, book_id):
        book = self.books.get(book_id)
        if not book:
            print("Error: Book not found.")
        elif book.is_borrowed:
            print(f"Error: '{book.title}' is already borrowed.")
        else:
            book.is_borrowed = True
            print(f"Success: You have borrowed '{book.title}'.")

    def return_book(self, book_id):
        book = self.books.get(book_id)
        if not book:
            print("Error: Book not found.")
        elif not book.is_borrowed:
            print(f"Error: '{book.title}' was not borrowed.")
        else:
            book.is_borrowed = False
            print(f"Success: You have returned '{book.title}'.")

def main():
    library = Library()
    
    # Optional: Pre-fill some books
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "101")
    library.add_book("1984", "George Orwell", "102")

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")

        if choice == '1':
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            bid = input("Enter Book ID: ")
            library.add_book(title, author, bid)
        elif choice == '2':
            library.display_books()
        elif choice == '3':
            bid = input("Enter Book ID to borrow: ")
            library.borrow_book(bid)
        elif choice == '4':
            bid = input("Enter Book ID to return: ")
            library.return_book(bid)
        elif choice == '5':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

