import unittest
from lettersround import LettersRound

class TestLettersRound(unittest.TestCase):

    def test_select_letters(self):
        a_round = LettersRound()
        letters = a_round.select_letters(3, 6)
        self.assertEqual(len(letters), 9)
        self.assertEqual(sum(1 for letter in letters if letter in 'AEIOU'), 3)
        self.assertEqual(sum(1 for letter in letters if letter not in 'AEIOU'), 6)

    def test_invalid_letter_selection(self):
        a_round = LettersRound()
        with self.assertRaises(ValueError):
            a_round.select_letters(2, 7)
        with self.assertRaises(ValueError):
            a_round.select_letters(6, 3)
        with self.assertRaises(ValueError):
            a_round.select_letters(4, 4)

    def test_submit_words(self):
        a_round = LettersRound()
        a_round.submit_words('mouse', 'cat')
        self.assertEqual(a_round.team1_word, 'mouse')
        self.assertEqual(a_round.team2_word, 'cat')

    def test_score_a_round(self):
        a_round = LettersRound()
        a_round.select_letters(3, 6)
        a_round.submit_words('mouse', 'cat')
        team1_score, team2_score = a_round.score_round()
        self.assertIsInstance(team1_score, int)
        self.assertIsInstance(team2_score, int)

if __name__ == '__main__':
    unittest.main()