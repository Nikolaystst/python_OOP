from abc import ABC, abstractmethod

from project.animal import Animal


class Cat(Animal, ABC):

    def make_sound(self):
        return "Meow meow!"
