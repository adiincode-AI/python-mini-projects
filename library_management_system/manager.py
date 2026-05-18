import json
import os
from models import User, Book
USER_FILE_PATH = "library_management_system/users.json"
BOOK_LIST_PATH = "library_management_system/books.json"


class UserManager():
    def __init__(self):
        self.user_list = []
        if os.path.exists(USER_FILE_PATH):
            with open(USER_FILE_PATH, "r") as file:

                try:
                    data = json.load(file)
                    for user_data in data:
                        user = User.from_dict(user_data)
                        self.user_list.append(user)
                except json.JSONDecodeError:
                    self.user_list = []

    def register_user(self, user):
        for existing_user in self.user_list:
            if existing_user.phonenumber == user.phonenumber:
                return False
        self.user_list.append(user)
        return True

    def save_user(self):

        with open(USER_FILE_PATH, "w") as file:
            json.dump([user.to_dict()
                      for user in self.user_list], file, indent=4)

    def login_user(self, phonenumber):
        for existing_user in self.user_list:
            if existing_user.phonenumber == phonenumber:
                return True
        return False


class LibraryManager():
    def __init__(self):
        self.books_list = []
        if os.path.exists(BOOK_LIST_PATH):
            with open(BOOK_LIST_PATH, "r")as file:
                try:
                    data = json.load(file)
                    for book_data in data:
                        book = Book.from_dict(book_data)
                        self.books_list.append(book)
                except json.JSONDecodeError:
                    self.books_list = []

    def borrow_book(self, book_title):
        for book in self.books_list:
            if book.title == book_title:
                if book.is_available:
                    book.is_available = False
                    return True
                return False
        return False

    def return_book(self, book_title):
        for book in self.books_list:
            if book.title == book_title:
                if not book.is_available:
                    book.is_available = True
                    return True
                return False
        return False

    def save_books(self):
        with open(BOOK_LIST_PATH, "w") as file:
            json.dump([book.to_dict()
                      for book in self.books_list], file, indent=4)

    def search_book(self, book_title):
        for book in self.books_list:
            if book.title == book_title:
                return book
        return None
