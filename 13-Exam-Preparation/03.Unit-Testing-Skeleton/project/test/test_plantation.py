import unittest

from project.plantation import Plantation


class TesPlantation(unittest.TestCase):
    def setUp(self) -> None:
        self.test_pl = Plantation(3)

    def test_init(self):
        self.assertEqual(3, self.test_pl.size)
        self.assertEqual({}, self.test_pl.plants)
        self.assertEqual([], self.test_pl.workers)

    def test_size_minus_value_setter_fail(self):
        with self.assertRaises(ValueError) as va:
            self.test_pl.size = -1

        self.assertEqual("Size must be positive number!", str(va.exception))

    def test_hire_worker_twice_val_err(self):
        self.test_pl.hire_worker("niki")
        with self.assertRaises(ValueError) as va:
            self.test_pl.hire_worker("niki")
        self.assertEqual("Worker already hired!", str(va.exception))
        self.assertEqual(["niki"], self.test_pl.workers)

    def test_hire_worker_first_time_success(self):
        result = self.test_pl.hire_worker("niki")
        self.assertEqual(["niki"], self.test_pl.workers)
        self.assertEqual("niki successfully hired.", result)

    def test_dunder_len_method(self):
        self.test_pl.hire_worker("niki")
        self.test_pl.hire_worker("kiki")
        self.test_pl.planting("niki", "koiche")
        self.test_pl.planting("niki", "moiche")
        self.test_pl.planting("kiki", "foiche")
        res = self.test_pl.__len__()
        self.assertEqual(3, res)

    def test_planting_method_fail_worker_not_in_workers(self):
        with self.assertRaises(ValueError) as va:
            self.test_pl.planting("niki", "kiki")

        self.assertEqual("Worker with name niki is not hired!", str(va.exception))

    def test_planting_method_fail_cause_of_max_len(self):
        self.test_pl.size = 0
        self.test_pl.hire_worker("niki")
        with self.assertRaises(ValueError) as va:
            self.test_pl.planting("niki", "kiki")

        self.assertEqual("The plantation is full!", str(va.exception))

    def test_planting_method_success_worker_as_a_key(self):
        self.test_pl.hire_worker("niki")
        self.test_pl.planting("niki", "koiche")
        res = self.test_pl.planting("niki", "moiche")
        self.assertEqual({"niki": ["koiche", "moiche"]}, self.test_pl.plants)
        self.assertEqual("niki planted moiche.", res)

    def test_planting_method_success_worker_as_a_new_key(self):
        self.test_pl.hire_worker("niki")
        res = self.test_pl.planting("niki", "koiche")
        self.assertEqual({"niki": ["koiche"]}, self.test_pl.plants)
        self.assertEqual("niki planted it's first koiche.", res)

    def test_str_method(self):
        self.test_pl.hire_worker("niki")
        self.test_pl.planting("niki", "k")
        res = ("Plantation size: 3\n"
               "niki\n"
               "niki planted: k")
        self.assertEqual(res, self.test_pl.__str__())

    def test_repr_method(self):
        self.test_pl.hire_worker("niki")
        self.test_pl.hire_worker("kiki")
        res = ("Size: 3\n"
               "Workers: niki, kiki")
        self.assertEqual(res, self.test_pl.__repr__())


if __name__ == "__main__":
    unittest.main()
