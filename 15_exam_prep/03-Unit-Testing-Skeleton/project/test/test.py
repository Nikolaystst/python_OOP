from project.tennis_player import TennisPlayer
import unittest


class TestTennisPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.test_1 = TennisPlayer("niki", 33, 59.95)

    def test_init(self):
        self.assertEqual("niki", self.test_1.name)
        self.assertEqual(33, self.test_1.age)
        self.assertEqual(59.95, self.test_1.points)
        self.assertEqual([], self.test_1.wins)

    def test_props_name_setter_val_error(self):
        with self.assertRaises(ValueError) as va:
            self.test_1.name = "ha"

        self.assertEqual("Name should be more than 2 symbols!", str(va.exception))

    def test_props_age_setter_val_error(self):
        with self.assertRaises(ValueError) as va:
            self.test_1.age = 17

        self.assertEqual("Players must be at least 18 years of age!", str(va.exception))

    def test_add_new_win_method_success_apend_new_tournament(self):
        self.test_1.add_new_win("nfs")
        self.assertEqual(["nfs"], self.test_1.wins)

    def test_add_new_win_method_fail_tourn_already_in_wined_tours(self):
        self.test_1.add_new_win("nfs")
        res = self.test_1.add_new_win("nfs")
        self.assertEqual("nfs has been already added to the list of wins!", res)

    def test_lt_method_other_is_better_than_me(self):
        self.test_2 = TennisPlayer("kiki", 31, 95.59)
        res = self.test_1.__lt__(self.test_2)
        self.assertEqual('kiki is a top seeded player and he/she is better than niki', res)

    def test_lt_method_i_am_better_than_other(self):
        self.test_2 = TennisPlayer("kiki", 31, 15.59)
        res = self.test_1.__lt__(self.test_2)
        self.assertEqual('niki is a better player than kiki', res)

    def test_str_method(self):
        self.test_1.add_new_win("nfs")
        self.test_1.add_new_win("heh")
        res = self.test_1.__str__()
        what_should_be = "Tennis Player: niki\n" \
                         "Age: 33\n" \
                         "Points: 60.0\n" \
                         "Tournaments won: nfs, heh"
        self.assertEqual(what_should_be, res)


if __name__ == "__main__":
    unittest.main()
