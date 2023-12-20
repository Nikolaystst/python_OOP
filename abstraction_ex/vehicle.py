from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: int) -> None:
        pass

    @abstractmethod
    def refuel(self, fuel: int) -> None:
        pass


class Car(Vehicle):
    AIRCON = 0.9

    def drive(self, distance: int) -> None:
        needed_fuel = distance * (self.fuel_consumption + Car.AIRCON)
        if needed_fuel > self.fuel_quantity:
            return
        self.fuel_quantity -= needed_fuel

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIRCON = 1.6

    def drive(self, distance: int) -> None:
        needed_fuel = distance * (self.fuel_consumption + Truck.AIRCON)
        if needed_fuel > self.fuel_quantity:
            return
        self.fuel_quantity -= needed_fuel

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
