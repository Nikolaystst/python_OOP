from project.movie import Movie
import unittest


class TestMovie(unittest.TestCase):
    def setUp(self) -> None:
        self.test_1 = Movie("niki", 1990, 5.9)

    def test_init(self):
        self.assertEqual("niki", self.test_1.name)
        self.assertEqual(1990, self.test_1.year)
        self.assertEqual(5.9, self.test_1.rating)
        self.assertEqual([], self.test_1.actors)

    def test_wrong_name_setter(self):
        with self.assertRaises(ValueError) as va:
            self.test_1.name = ""

        self.assertEqual("Name cannot be an empty string!", str(va.exception))

    def test_wrong_year_setter(self):
        with self.assertRaises(ValueError) as va:
            self.test_1.year = 1886

        self.assertEqual("Year is not valid!", str(va.exception))

    def test_add_actor_method_twice(self):
        self.assertEqual([], self.test_1.actors)
        self.test_1.add_actor("koko")
        self.test_1.add_actor("doko")
        self.assertEqual(["koko", "doko"], self.test_1.actors)

    def test_add_actor_method_twice_fail_same_name(self):
        self.assertEqual([], self.test_1.actors)
        self.test_1.add_actor("koko")
        result = self.test_1.add_actor("koko")
        self.assertEqual("koko is already added in the list of actors!", result)

    def test_greater_than_method_our_movie_win(self):
        self.test_2 = Movie("kiki", 1990, 3.5)
        result = self.test_1.__gt__(self.test_2)
        self.assertEqual('"niki" is better than "kiki"', result)

    def test_greater_than_method_2nd_movie_win(self):
        self.test_2 = Movie("kiki", 1990, 9.5)
        result = self.test_1.__gt__(self.test_2)
        self.assertEqual('"kiki" is better than "niki"', result)

    def test_repr_method_result_string(self):
        self.test_1.add_actor("koko")
        self.test_1.add_actor("doko")
        result = self.test_1.__repr__()
        self.assertEqual("Name: niki\n"
                         "Year of Release: 1990\n"
                         "Rating: 5.90\n"
                         "Cast: koko, doko", result)


if __name__ == "__main__":
    unittest.main()
