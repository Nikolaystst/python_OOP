from project.employee import Employee
# from employee import Employee
from project.person import Person
# from person import Person


class Teacher(Employee, Person):
    def teach(self):
        return "teaching..."
