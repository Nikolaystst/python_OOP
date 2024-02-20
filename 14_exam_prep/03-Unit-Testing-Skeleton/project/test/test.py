from project.robot import Robot
import unittest


class TestRobot(unittest.TestCase):
    def setUp(self) -> None:
        self.robo_1 = Robot("1", "Entertainment", 59, 95)

    def test_class_uppers(self):
        self.assertEqual(['Military', 'Education', 'Entertainment', 'Humanoids'], Robot.ALLOWED_CATEGORIES)
        self.assertEqual(1.5, Robot.PRICE_INCREMENT)

    def test_init(self):
        self.assertEqual("1", self.robo_1.robot_id)
        self.assertEqual("Entertainment", self.robo_1.category)
        self.assertEqual(59, self.robo_1.available_capacity)
        self.assertEqual(95, self.robo_1.price)
        self.assertEqual([], self.robo_1.hardware_upgrades)
        self.assertEqual([], self.robo_1.software_updates)

    def test_category_setter_fail(self):
        with self.assertRaises(ValueError) as va:
            self.robo_1.category = "sex"

        self.assertEqual("Category should be one of "
                         "'['Military', 'Education'"
                         ", 'Entertainment', 'Humanoids']'", str(va.exception))

    def test_price_setter_fail(self):
        with self.assertRaises(ValueError) as va:
            self.robo_1.price = -5

        self.assertEqual("Price cannot be negative!", str(va.exception))

    def test_upgrade_method_fail_hardware_comp_in_hardware_updates(self):
        self.robo_1.hardware_upgrades = ["dadada"]
        res = self.robo_1.upgrade("dadada", 32.5)
        self.assertEqual("Robot 1 was not upgraded.", res)

    def test_upgrade_method_success(self):
        res = self.robo_1.upgrade("dadada", 32.5)
        self.assertEqual(["dadada"], self.robo_1.hardware_upgrades)
        self.assertEqual(143.75, self.robo_1.price)
        self.assertEqual('Robot 1 was upgraded with dadada.', res)

    def test_update_method_fail_older_version(self):
        self.robo_1.update(3.11, 5)
        res = self.robo_1.update(1.1, 3)
        self.assertEqual("Robot 1 was not updated.", res)

    def test_update_method_fail_need_of_capacity(self):
        res = self.robo_1.update(3.11, 555)
        self.assertEqual("Robot 1 was not updated.", res)

    def test_update_method_success_twice_in_a_row(self):
        res = self.robo_1.update(3.11, 5)
        self.assertEqual([3.11], self.robo_1.software_updates)
        self.assertEqual(54, self.robo_1.available_capacity)
        self.assertEqual('Robot 1 was updated to version 3.11.', res)
        res = self.robo_1.update(3.12, 5)
        self.assertEqual([3.11, 3.12], self.robo_1.software_updates)
        self.assertEqual(49, self.robo_1.available_capacity)
        self.assertEqual('Robot 1 was updated to version 3.12.', res)

    def test_greater_than_method_self_price_bigger_than_others(self):
        self.robo_2 = Robot("2", "Entertainment", 59, 55)
        res = self.robo_1.__gt__(self.robo_2)
        self.assertEqual('Robot with ID 1 is more expensive than Robot with ID 2.', res)

    def test_greater_than_method_same_prices(self):
        self.robo_2 = Robot("2", "Entertainment", 59, 95)
        res = self.robo_1.__gt__(self.robo_2)
        self.assertEqual('Robot with ID 1 costs equal to Robot with ID 2.', res)

    def test_greater_than_method_self_price_lower_than_others(self):
        self.robo_2 = Robot("2", "Entertainment", 59, 100)
        res = self.robo_1.__gt__(self.robo_2)
        self.assertEqual('Robot with ID 1 is cheaper than Robot with ID 2.', res)


if __name__ == "__main__":
    unittest.main()
