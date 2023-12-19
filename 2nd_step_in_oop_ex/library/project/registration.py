# from project.library import Library
# from project.user import User
from library import Library
from user import User


class Registration:
    def add_user(self, user: User, library: Library) -> str or None:
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        library.user_records.append(user)

    def remove_user(self, user: User, library: Library) -> str or None:
        if user not in library.user_records:
            return "We could not find such user to remove!"

        library.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str, library: Library):
        flag = False
        for user_1 in library.user_records:
            if user_id == user_1.user_id:
                flag = True

            if user_id == user_1.user_id and new_username == user_1.username:
                return "Please check again the provided username - " \
                       "it should be different than the username used so far!"
            elif user_id == user_1.user_id and new_username != user_1.username:
                user_1.username = new_username
                try:
                    library.rented_books[new_username] = library.rented_books.pop(user_1.username)
                except KeyError:
                    pass
                return f"Username successfully changed to: {new_username} for user id: {user_id}"

        if not flag:
            return f"There is no user with id = {user_id}!"
