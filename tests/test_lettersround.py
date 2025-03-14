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
        letters = self.a_round.select_letters(3, 6)
        team1_word = ''.join(letters[:3])
        team2_word = ''.join(letters[3:6])
        team1_score, team2_score = self.a_round.score_round(team1_word, team2_word, letters)
        self.assertGreaterEqual(team1_score, 0)
        self.assertGreaterEqual(team2_score, 0)

    def test_score_round_invalid_word(self):
        letters = self.a_round.select_letters(3, 6)
        team1_word = 'INVALID'
        team2_word = ''.join(letters[3:6])
        team1_score, team2_score = self.a_round.score_round(team1_word, team2_word, letters)
        self.assertEqual(team1_score, 0)
        self.assertGreaterEqual(team2_score, 0)


if __name__ == '__main__':
    unittest.main()
