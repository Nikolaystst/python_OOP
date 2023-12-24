class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    # @property
    # def name(self):
    #     return self.__name
    #
    # @name.setter
    # def name(self, value):
    #     self.__name = value
    #
    # @property
    # def age(self):
    #     return self.__age
    #
    # @age.setter
    # def age(self, value):
    #     self.__age = value


person = Person("George", 32)
print(person.get_name())
print(person.get_age())
