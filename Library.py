class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_read = False

    def __str__(self):
        return f"{self.title} by {self.author}"


def display():
    print("Library:")
    print("1. Add Books")
    print("2. View Books")
    print("3. Mark Book as read")
    print("4. Exit\n")


#To add number of books in the library
def add_book(books):
    n = int(input("Enter the number of books you want to add: "))
    if n > 0:
        for _ in range(n):
            title = input("Enter the Book name: ")
            author = input("Enter the Author name: ")
            book = Book(title, author)
            books.append(book)
        print("Books added successfully!\n")
    else:
        print("Please enter a positive number.\n")

#To show saved books in the library
def view_books(books):
    if len(books) == 0:
        print("List is empty.")
    else:
        print("Books:")
        for index, book in enumerate(books):
            print(f"{index+1}. {book}\n")


#to mark/remove books that are read
def books_read(books):
    view_books(books)
    book_index = int(input("Enter the number to mark as read: "))
    if book_index <= len(books):
        read = books.pop(book_index-1)
        print(f"{read} marked as read!\n")
    else:
        print("Invalid number.\n")


def main():
    books = []
    while True:
        display()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_book(books)
        elif choice == '2':
            view_books(books)
        elif choice == '3':
            books_read(books)
        elif choice == '4':
            print("Exiting program.\n")
            break
        else:
            print("Please try again.\n")


if __name__ == "__main__":
    main()
