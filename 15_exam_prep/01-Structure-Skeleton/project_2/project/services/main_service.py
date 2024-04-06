from project_2.project.services.base_service import BaseService
from project_2.project.robots.male_robot import MaleRobot


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, capacity=self.CAPACITY)

    def details(self):
        return f"""{self.name} Main Service:
Robots: {self._get_names()}"""


# a = MaleRobot("niki", "sex", 59)
# b = MaleRobot("kiki", "sex", 69)
# c = MainService("haha")
# c.robots.append(a)
# c.robots.append(b)
# print(c.details())
