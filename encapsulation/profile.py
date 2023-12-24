class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value) -> None or ValueError:
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        len_1 = len(value) >= 8
        upper_1 = len([p for p in value if p.isupper()]) >= 1
        digit_1 = len([p for p in value if p.isdigit()]) >= 1

        if not len_1 or not upper_1 or not digit_1:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = len(value)

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * self.__password}'


# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)