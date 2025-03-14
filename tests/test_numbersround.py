import unittest
from core.numbers_round import NumbersRound


class TestNumbersRound(unittest.TestCase):

    def setUp(self):
        self.numbers_round = NumbersRound()

    def test_get_number_selections_valid(self):
        numbers = self.numbers_round.get_number_selections(2, 4)
        self.assertEqual(len(numbers), 6)
        self.assertEqual(sum(1 for number in numbers if number in self.numbers_round.large_numbers), 2)
        self.assertEqual(sum(1 for number in numbers if number in self.numbers_round.small_numbers), 4)

    def test_get_number_selections_invalid_large(self):
        with self.assertRaises(ValueError):
            self.numbers_round.get_number_selections(5, 1)

    def test_get_number_selections_invalid_small(self):
        with self.assertRaises(ValueError):
            self.numbers_round.get_number_selections(1, 1)

    def test_get_number_selections_invalid_total(self):
        with self.assertRaises(ValueError):
            self.numbers_round.get_number_selections(2, 5)

    def test_find_target_number(self):
        target_number = self.numbers_round.find_target_number()
        self.assertTrue(101 <= target_number <= 999)


if __name__ == '__main__':
    unittest.main()
