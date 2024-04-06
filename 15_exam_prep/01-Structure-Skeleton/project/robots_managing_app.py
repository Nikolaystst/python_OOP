from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type != "MainService" and service_type != "SecondaryService":
            raise Exception("Invalid service type!")
        if service_type == "MainService":
            self.services.append(MainService(name))
        elif service_type == "SecondaryService":
            self.services.append(SecondaryService(name))

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type != "FemaleRobot" and robot_type != "MaleRobot":
            raise Exception("Invalid robot type!")
        if robot_type == "FemaleRobot":
            self.robots.append(FemaleRobot(name, kind, price))
        elif robot_type == "MaleRobot":
            self.robots.append(MaleRobot(name, kind, price))

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        rob_1 = None
        ser_1 = None
        for rob in self.robots:
            if rob.name == robot_name:
                rob_1 = rob
                break
        for ser in self.services:
            if ser.name == service_name:
                ser_1 = ser
                break

        if rob_1.__class__.__name__ == "FemaleRobot" and ser_1.__class__.__name__ == "MainService":
            return "Unsuitable service."
        if rob_1.__class__.__name__ == "MaleRobot" and ser_1.__class__.__name__ == "SecondaryService":
            return "Unsuitable service."

        if ser_1.capacity <= len(ser_1.robots):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(rob_1)
        ser_1.robots.append(rob_1)
        return f"Successfully added {rob_1.name} to {ser_1.name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        rob_1 = None
        ser_1 = None
        for ser in self.services:
            if ser.name == service_name:
                ser_1 = ser
                break

        for rob in ser_1.robots:
            if rob.name == robot_name:
                rob_1 = rob
                break

        if rob_1 is None:
            raise Exception("No such robot in this service!")

        self.robots.append(rob_1)
        ser_1.robots.remove(rob_1)
        return f"Successfully removed {rob_1.name} from {ser_1.name}."

    def feed_all_robots_from_service(self, service_name: str):
        ser_1 = None
        for ser in self.services:
            if ser.name == service_name:
                ser_1 = ser
                break

        for robot in ser_1.robots:
            robot.eating()

        return f"Robots fed: {len(ser_1.robots)}."

    def service_price(self, service_name: str):
        price = 0
        ser_1 = None
        for ser in self.services:
            if ser.name == service_name:
                ser_1 = ser
                break

        for rob in ser_1.robots:
            price += rob.price

        return f"The value of service {service_name} is {price:.2f}."

    def __str__(self):
        result = []
        for service in self.services:
            result.append(service.details())

        return "\n".join(result)
