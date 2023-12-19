# from project.user import User
from user import User
from typing import List, Dict


class Library:
    def __init__(self):
        self.user_records: List = []
        self.books_available: Dict[str: List[str]] = {}
        self.rented_books: Dict[str: Dict[str: int]] = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        for username, b_name_days in self.rented_books.items():
            for book_name_1, days_to_return_1 in b_name_days.items():
                if book_name_1 == book_name:
                    return f'The book "{book_name}" is already rented and will be' \
                           f' available in {days_to_return_1} days!'

        if book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)

            if user.username not in self.rented_books.keys():
                self.rented_books[user.username] = {book_name: days_to_return}
            else:
                self.rented_books[user.username][book_name] = days_to_return

            return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, user: User):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"

        user.books.remove(book_name)
        self.books_available[author].append(book_name)
        del self.rented_books[user.username][book_name]
