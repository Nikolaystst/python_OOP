from project.truck_driver import TruckDriver
import unittest


class TestTruckDriver(unittest.TestCase):
    def setUp(self) -> None:
        self.test_1 = TruckDriver("niki", 15)

    def test_init(self):
        self.assertEqual("niki", self.test_1.name)
        self.assertEqual(15, self.test_1.money_per_mile)
        self.assertEqual({}, self.test_1.available_cargos)
        self.assertEqual(0, self.test_1.earned_money)
        self.assertEqual(0, self.test_1.miles)

    def test_earned_money_property_fail(self):
        with self.assertRaises(ValueError) as va:
            self.test_1.earned_money = -5

        self.assertEqual("niki went bankrupt.", str(va.exception))

    def test_went_bancrupcy(self):
        self.test_1.money_per_mile = 0.01
        self.test_1.add_cargo_offer("dgr", 9999)
        with self.assertRaises(ValueError) as va:
            self.test_1.drive_best_cargo_offer()
        self.assertEqual("niki went bankrupt.", str(va.exception))

    def test_add_cargo_offer_method_fail(self):
        self.test_1.available_cargos["dgr"] = 15
        with self.assertRaises(Exception) as ex:
            self.test_1.add_cargo_offer("dgr", 15)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_method_success(self):
        res = self.test_1.add_cargo_offer("dgr", 15)
        self.assertEqual({"dgr": 15}, self.test_1.available_cargos)
        self.assertEqual("Cargo for 15 to dgr was added as an offer.", res)

    def test_drive_best_cargo_offer_fail(self):
        res = self.test_1.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", res)

    def test_drive_best_cargo_offer_success(self):
        self.test_1.add_cargo_offer("dgr", 15)
        self.test_1.add_cargo_offer("hs", 5)
        res = self.test_1.drive_best_cargo_offer()
        self.assertEqual(225, self.test_1.earned_money)
        self.assertEqual(15, self.test_1.miles)
        self.assertEqual("niki is driving 15 to dgr.", res)

    def test_check_for_activities_method(self):
        self.test_1.earned_money = 11750
        self.test_1.check_for_activities(10000)
        self.assertEqual(0, self.test_1.earned_money)

    def test_eat_method(self):
        self.test_1.earned_money = 7500
        self.test_1.eat(250)
        self.assertEqual(7480, self.test_1.earned_money)

    def test_sleep_method(self):
        self.test_1.earned_money = 7500
        self.test_1.sleep(1000)
        self.assertEqual(7455, self.test_1.earned_money)

    def test_pump_gas_method(self):
        self.test_1.earned_money = 7500
        self.test_1.pump_gas(1500)
        self.assertEqual(7000, self.test_1.earned_money)

    def test_repair_truck_method(self):
        self.test_1.earned_money = 7500
        self.test_1.repair_truck(10000)
        self.assertEqual(0, self.test_1.earned_money)

    def test_repr_method(self):
        res = self.test_1.__repr__()
        self.assertEqual("niki has 0 miles behind his back.", res)


if __name__ == "__main__":
    unittest.main()
