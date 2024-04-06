from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 30)

    def details(self):
        final = [f"{self.name} Main Service:\nRobots:"]
        if self.robots:
            for robot in self.robots:
                final.append(robot.name)
        else:
            final.append("none")
        return " ".join(final)


# a = MaleRobot("niki", "sex", 59)
# b = MaleRobot("kiki", "sex", 69)
# c = MainService("haha")
# c.robots.append(a)
# c.robots.append(b)
# print(c.details())

