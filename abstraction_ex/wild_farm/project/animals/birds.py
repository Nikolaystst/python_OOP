from project.food import Meat, Vegetable, Fruit, Seed
from project.animals.animal import Bird


class Owl(Bird):

    def make_sound(self) -> str:
        return "Hoot Hoot"

    @property
    def what_does_it_eats(self):
        return [Meat]

    @property
    def gains(self):
        return 0.25


class Hen(Bird):

    def make_sound(self) -> str:
        return "Cluck"

    @property
    def what_does_it_eats(self):
        return [Meat, Vegetable, Fruit, Seed]

    @property
    def gains(self):
        return 0.35
