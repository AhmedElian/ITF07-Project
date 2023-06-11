class Book:
    def __init__(self, book_id, title, author, level):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.level = level
        self.available = True

    def display_details(self):
        print(f'Book ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Level: {self.level}')


class Member:
    def __init__(self, member_id, name, email, level):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.level = level
        self.borrowed_books = []

    def display_details(self):
        print(f'Member ID: {self.member_id} | Name: {self.name} | Email: {self.email} | Level: {self.level} | Borrowed Books: {len(self.borrowed_books)}')


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.deleted_books = []
        self.deleted_members = []
        self.borr_books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)
        self.deleted_books.append(book)

    def re_add_book(self, book):
        self.books.append(book)
        self.deleted_books.remove(book)
        book.available = True

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        self.members.remove(member)
        self.deleted_members.append(member)

    def re_add_member(self, member):
        self.members.append(member)
        self.deleted_members.remove(member)

    def display_books(self):
        if self.books:
            print(' Available Books '.center(50, '*'))
            for book in self.books:
                if book.available:
                    book.display_details()
        else:
            print('No Available Books.')

    def display_borr_book(self):
        if self.borr_books:
            print(' Borrowed Books '.center(50, '*'))
            for book in self.borr_books:
                book.display_details()
        else:
            print('No Borrowed Books.')

    def display_deleted_books(self):
        if self.deleted_books:
            print(' Deleted Books '.center(50, '*'))
            for book in self.deleted_books:
                book.display_details()
        else:
            print('No Deleted Books.')

    def display_members(self):
        if self.members:
            print(' Available Members '.center(50, '*'))
            for member in self.members:
                member.display_details()
        else:
            print('No available members.')

    def display_deleted_members(self):
        if self.deleted_members:
            print(' Deleted Members '.center(50, '*'))
            for member in self.deleted_members:
                member.display_details()
        else:
            print('No Deleted Members.')

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book

    def find_deleted_book_by_id(self, book_id):
        for book in self.deleted_books:
            if book.book_id == book_id:
                return book

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member

    def find_deleted_member_by_id(self, member_id):
        for member in self.deleted_members:
            if member.member_id == member_id:
                return member

    def borrow_book(self, member_id, book_id):
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_id(book_id)
        if member is None or book is None:
            print('Invalid member ID or book ID.')
            return

        if not book.available:
            print('Book is not available.')
            return

        if member.level.lower() != book.level.lower():
            print("Member's level is not suitable for borrowing this book.")

        book.available = False
        member.borrowed_books.append(book)
        self.borr_books.append(book)
        print('Book borrowed successfully.')

    def return_book(self, member_id, book_id):
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_id(book_id)
        if member is None or book is None:
            print('Invalid member ID or book ID.')

        if book in member.borrowed_books:
            book.available = True
            member.borrowed_books.remove(book)
            self.borr_books.remove(book)
            print('Book returned successfully.')
        else:
            print('Member has not borrowed this book.')

    def display_menu(self):
        print(' Welcome To The Library Management System '.center(50, '*'))
        print(' 1- Books Options '.center(50, '*'))
        print('1. Add book.')
        print('2. Remove book.')
        print('3. Re-add deleted book.')
        print('4. Show available books.')
        print('5. Show deleted books.')
        print(' 2- Members Options '.center(50, '*'))
        print('6. Add member.')
        print('7. Remove member.')
        print('8. Re-add deleted member.')
        print('9. Show available members.')
        print('10. Show deleted members.')
        print(' 3- Library Options '.center(50, '*'))
        print('11. Borrow a book.')
        print('12. Return a book.')
        print('13. Count of members in the library.')
        print('14. Count of books in the library.')
        print('15. Show borrowed books.')
        print('16. Exit.')

    def run(self):
        count_id = 1
        count_member = 1
        levels = ['A', 'B', 'C']
        while True:
            self.display_menu()
            try:
                choice = int(input('Enter your choice: '))

                if choice == 1:
                    title = input('* Enter title: ')
                    author = input('* Enter author: ')
                    level = input('* Enter level (A for children | B for teenagers | C for adults): ')
                    if level.upper() not in levels:
                        raise ValueError()

                    book = Book(count_id, title, author, level.upper())
                    self.add_book(book)
                    print('Book added successfully.')
                    count_id += 1

                elif choice == 2:
                    book_id = int(input('Enter book ID to remove: '))
                    book = self.find_book_by_id(book_id)
                    if book:
                        self.remove_book(book)
                        print('Book removed successfully.')
                    else:
                        print('Book not found.')

                elif choice == 3:
                    book_id = int(input('Enter book ID to re-add: '))
                    book = self.find_deleted_book_by_id(book_id)
                    if book in self.deleted_books:
                        self.re_add_book(book)
                        print('Book re-added successfully.')
                    else:
                        print('Deleted book not found.')

                elif choice == 4:
                    self.display_books()

                elif choice == 5:
                    self.display_deleted_books()

                elif choice == 6:
                    name = input('* Enter name: ')
                    email = input('* Enter email: ')
                    level = input('* Enter level (A for children | B for teenagers | C for adults): ')
                    if level.upper() not in levels:
                        raise ValueError()

                    member = Member(count_member, name, email, level.upper())
                    self.add_member(member)
                    count_member += 1
                    print('Member added successfully.')

                elif choice == 7:
                    member_id = int(input('Enter member ID to remove: '))
                    member = self.find_member_by_id(member_id)
                    if member:
                        self.remove_member(member)
                        print('Member removed successfully.')
                    else:
                        print('Member not found.')

                elif choice == 8:
                    member_id = int(input('Enter member ID to re-add: '))
                    member = self.find_deleted_member_by_id(member_id)
                    if member and member in self.deleted_members:
                        self.re_add_member(member)
                        print('Member re-added successfully.')
                    else:
                        print('Deleted member not found.')

                elif choice == 9:
                    self.display_members()

                elif choice == 10:
                    self.display_deleted_members()

                elif choice == 11:
                    member_id = int(input('Enter member ID: '))
                    book_id = int(input('Enter book ID: '))
                    self.borrow_book(member_id, book_id)

                elif choice == 12:
                    member_id = int(input('Enter member ID: '))
                    book_id = int(input('Enter book ID: '))
                    self.return_book(member_id, book_id)

                elif choice == 13:
                    print('Number of Members: ', len(self.members))

                elif choice == 14:
                    print('Number of Books: ', len(self.books))
                elif choice == 15:
                    self.display_borr_book()
                elif choice == 16:
                    print('Thank You For Using The Library Management System.')
                    break

                else:
                    print("Invalid choice.")

            except ValueError:
                print('Invalid level.')

            except:
                print("Library Management System Exiting...")


lib = Library()
lib.run()
