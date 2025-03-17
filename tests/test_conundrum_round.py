import unittest
from core.conundrum_round import ConundrumRound
from core.susie_dent import SusieDent


class TestConundrumRound(unittest.TestCase):

    def setUp(self):
        self.conundrum_round = ConundrumRound()
        # let's get an instance of SusieDent to use to check the validity of words
        self.susie = SusieDent()
        self.debug_mode = True

    def test_generate_conundrum(self):
        conundrum, solution = self.conundrum_round.generate_conundrum()
        if self.debug_mode:
            print(f"Conundrum: {conundrum}, Solution: {solution}")
        self.assertEqual(len(conundrum), 9)
        self.assertEqual(len(solution), 9)
        self.assertNotEqual(conundrum, solution)
        self.assertTrue(solution.isalpha())
        self.assertTrue(conundrum.isalpha())
        self.assertCountEqual(conundrum, solution)
        self.assertTrue(self.susie.is_valid_english_word(solution))

    def test_validate_solution(self):
        conundrum, solution = self.conundrum_round.generate_conundrum()
        is_valid = self.conundrum_round.validate_solution(conundrum, solution)
        if self.debug_mode:
            print(f"Validating Conundrum: {conundrum}, Solution: {solution}, Is Valid: {is_valid}")
        self.assertTrue(is_valid)

        # Test with an invalid solution
        invalid_solution = "invalidword"
        is_valid_invalid = self.conundrum_round.validate_solution(conundrum, invalid_solution)
        if self.debug_mode:
            print(f"Validating Conundrum: {conundrum}, Invalid Solution: {invalid_solution}, Is Valid: {is_valid_invalid}")
        self.assertFalse(is_valid_invalid)

if __name__ == '__main__':
    unittest.main()