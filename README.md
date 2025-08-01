📚 Library Management System (Console App - Python)

A basic Library Management System implemented in Python using Object-Oriented Programming (OOP). This system allows users to manage books, members, and borrowing/returning functionality through a console-based menu.

🧠 Features

Add, remove, and restore books

Add, remove, and restore members

Display available and deleted books/members

Borrow and return books

Ensure members can only borrow books matching their level (A, B, or C)

Track currently borrowed books

Simple menu-based navigation

🧩 Structure

The system has three main classes:

✅ Book

Represents a book in the library.

Attributes:

book_id

title

author

level (A = children, B = teens, C = adults)

available (default: True)

Method:

display_details() — prints book info

✅ Member

Represents a library member.

Attributes:

member_id

name

email

level

borrowed_books (list of books borrowed)

Method:

display_details() — prints member info

✅ Library

Handles the library system.

Attributes:

books — current available books

members — current registered members

deleted_books — soft-deleted books

deleted_members — soft-deleted members

borr_books — currently borrowed books

Key Methods:

add_book(), remove_book(), re_add_book()

add_member(), remove_member(), re_add_member()

borrow_book(member_id, book_id) — borrow logic

return_book(member_id, book_id) — return logic

display_books(), display_members(), etc.

run() — runs the console menu loop

🧪 How to Use

Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/library-management.git
cd library-management
Run the Python file:

bash
Copy
Edit
python filename.py
Use the menu to:

Add/remove books or members

Borrow or return books

View counts and lists

🔐 Borrowing Rules

A member can only borrow books that match their level:

A = children

B = teenagers

C = adults

A book cannot be borrowed if it's already checked out.

Borrowed books are marked as unavailable until returned.

✅ Sample Console Menu

markdown

Copy

Edit

**************** Welcome To The Library Management System ****************

*********************** 1- Books Options *********************************

1. Add book.
2. Remove book.
3. Re-add deleted book.
4. Show available books.
5. Show deleted books.

*********************** 2- Members Options *******************************

6. Add member.
7. Remove member.
8. Re-add deleted member.
9. Show available members.
10. Show deleted members.

*********************** 3- Library Options *******************************

11. Borrow a book.
12. Return a book.
13. Count of members in the library.
14. Count of books in the library.
15. Show borrowed books.
16. Exit.

📌 Note

The app uses soft deletion, meaning removed books and members are not lost and can be restored later.

Designed for educational purposes (OOP, data structures, menu handling).

🧑‍💻 Author

Ahmed Abdallatif
