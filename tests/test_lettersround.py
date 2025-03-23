import unittest
from core.letters_round import LettersRound


class TestLettersRound(unittest.TestCase):

    def setUp(self):
        self.a_round = LettersRound()

    def test_select_letters_valid(self):
        letters = self.a_round.select_letters(3, 6)
        self.assertEqual(len(letters), 9)
        self.assertEqual(sum(1 for letter in letters if letter in 'AEIOU'), 3)
        self.assertEqual(sum(1 for letter in letters if letter not in 'AEIOU'), 6)

    def test_select_letters_invalid_total(self):
        with self.assertRaises(ValueError):
            self.a_round.select_letters(2, 6)

    def test_select_letters_invalid_vowels(self):
        with self.assertRaises(ValueError):
            self.a_round.select_letters(2, 7)

    def test_select_letters_invalid_consonants(self):
        with self.assertRaises(ValueError):
            self.a_round.select_letters(3, 7)

    def test_score_round_valid_words(self):
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        choices = {
            'team1': 'CAB',
            'team2': 'BEAD'
        }
        scores = self.a_round.score_round(choices, letters)
        self.assertEqual(scores['team1'], 3)
        self.assertEqual(scores['team2'], 4)

    def test_score_round_invalid_word(self):
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        choices = {
            'team1': 'JJJJ',
            'team2': 'BEAD'
        }
        scores = self.a_round.score_round(choices, letters)
        self.assertEqual(0, scores['team1'])
        self.assertEqual(4, scores['team2'])


if __name__ == '__main__':
    unittest.main()
