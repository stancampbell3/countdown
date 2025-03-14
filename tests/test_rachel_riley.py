import unittest
from core.rachel_riley import RachelRiley, validate_solution


class TestRachelRiley(unittest.TestCase):

    def setUp(self):
        self.rachel_riley = RachelRiley()

    def test_validate_solution_correct(self):
        target = 532
        selection = [25, 50, 75, 100, 3, 6]
        solution = "100 * 5 + 25 + 7"
        difference = validate_solution(target, selection, solution)
        self.assertEqual(difference, 0)

    def test_validate_solution_incorrect(self):
        target = 532
        selection = [25, 50, 75, 100, 3, 6]
        solution = "100 * 5 + 25 + 6"
        difference = validate_solution(target, selection, solution)
        self.assertNotEqual(difference, 0)

    def test_validate_solution_invalid_usage(self):
        target = 532
        selection = [25, 50, 75, 100, 3, 6]
        solution = "100 * 5 + 25 + 25"
        difference = validate_solution(target, selection, solution)
        self.assertNotEqual(difference, 0)

    def test_find_solution(self):
        target = 532
        selection = [5, 100, 30, 2, 3, 4]
        solution = self.rachel_riley.find_solution(target, selection)
        self.assertIsNotNone(solution)
        print(solution)
        self.assertEqual(validate_solution(target, selection, solution), 0)


if __name__ == '__main__':
    unittest.main()
