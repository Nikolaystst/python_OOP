from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):

        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."

        self.users.append(User(first_name, last_name, driving_license_number))
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):

        if vehicle_type not in BaseVehicle.available_vehicles:
            return f"Vehicle type {vehicle_type} is inaccessible."

        for veh in self.vehicles:
            if veh.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."

        if vehicle_type == "CargoVan":
            self.vehicles.append(CargoVan(brand, model, license_plate_number))
        elif vehicle_type == "PassengerCar":
            self.vehicles.append(PassengerCar(brand, model, license_plate_number))

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif route.start_point == start_point and route.end_point == end_point and route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            elif route.start_point == start_point and route.end_point == end_point and route.length > length:
                route.is_locked = True

        self.routes.append(Route(start_point, end_point, length, len(self.routes) + 1))
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        use_1 = None
        car_1 = None
        route_1 = None
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                if user.is_blocked:
                    return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
                use_1 = user
                break
        for car in self.vehicles:
            if car.license_plate_number == license_plate_number:
                if car.is_damaged:
                    return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
                car_1 = car
                break
        for route in self.routes:
            if route.route_id == route_id:
                if route.is_locked:
                    return f"Route {route_id} is locked! This trip is not allowed."
                route_1 = route
                break

        car_1.drive(route_1.length)
        if is_accident_happened:
            car_1.is_damaged = True
            use_1.decrease_rating()
        elif not is_accident_happened:
            use_1.increase_rating()

        return car_1.__str__()

    def repair_vehicles(self, count: int):
        vehicles = [car for car in self.vehicles if car.is_damaged]
        vehicles = sorted(vehicles, key=lambda x: [x.brand, x.model])
        counter = 0
        for i in range(count):
            try:
                vehicles[i].is_damaged = False
                vehicles[i].recharge()
                counter += 1
            except IndexError:
                pass

        return f"{counter} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda x: -x.rating)
        res = ["*** E-Drive-Rent ***"]
        for user in sorted_users:
            res.append(user.__str__())
        return "\n".join(res)
