from project.food import Vegetable, Fruit, Meat
from project.animals.animal import Mammal


class Mouse(Mammal):

    def make_sound(self) -> str:
        return "Squeak"

    @property
    def what_does_it_eats(self):
        return [Vegetable, Fruit]

    @property
    def gains(self):
        return 0.1


class Dog(Mammal):

    def make_sound(self) -> str:
        return "Woof!"

    @property
    def what_does_it_eats(self):
        return [Meat]

    @property
    def gains(self):
        return 0.4


class Cat(Mammal):

    def make_sound(self) -> str:
        return "Meow"

    @property
    def what_does_it_eats(self):
        return [Meat, Vegetable]

    @property
    def gains(self):
        return 0.3


class Tiger(Mammal):

    def make_sound(self) -> str:
        return "ROAR!!!"

    @property
    def what_does_it_eats(self):
        return [Meat]

    @property
    def gains(self):
        return 1
