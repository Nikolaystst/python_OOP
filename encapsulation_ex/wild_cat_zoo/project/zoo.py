from typing import List

from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Lion or Cheetah or Tiger, price: int) -> str:
        if self.__animal_capacity > len(self.animals):
            if self.__budget < price:
                return "Not enough budget"

            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        return "Not enough space for animal"

    def hire_worker(self, worker: Vet or Keeper or Caretaker) -> str:
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
        except IndexError:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        payment = sum([w.salary for w in self.workers])
        if self.__budget >= payment:
            self.__budget -= payment
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        payment_animals = sum([a.money_for_care for a in self.animals])
        if self.__budget >= payment_animals:
            self.__budget -= payment_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        result = []
        lions = [l_0 for l_0 in self.animals if l_0.__class__.__name__ == "Lion"]
        cheetahs = [c for c in self.animals if c.__class__.__name__ == "Cheetah"]
        tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]
        result.append(f"You have {len(self.animals)} animals")
        result.append(f"----- {len(lions)} Lions:")
        for l in lions:
            result.append(f"{l.__repr__()}")
        result.append(f"----- {len(tigers)} Tigers:")
        for t in tigers:
            result.append(f"{t.__repr__()}")
        result.append(f"----- {len(cheetahs)} Cheetahs:")
        for c in cheetahs:
            result.append(f"{c.__repr__()}")

        return "\n".join(result)

    def workers_status(self) -> str:
        result = []
        keepers = [l_0 for l_0 in self.workers if l_0.__class__.__name__ == "Keeper"]
        caretakers = [c for c in self.workers if c.__class__.__name__ == "Caretaker"]
        vets = [t for t in self.workers if t.__class__.__name__ == "Vet"]
        result.append(f"You have {len(self.workers)} workers")
        result.append(f"----- {len(keepers)} Keepers:")
        for k in keepers:
            result.append(f"{k.__repr__()}")
        result.append(f"----- {len(caretakers)} Caretakers:")
        for c in caretakers:
            result.append(f"{c.__repr__()}")
        result.append(f"----- {len(vets)} Vets:")
        for v in vets:
            result.append(f"{v.__repr__()}")

        return "\n".join(result)
