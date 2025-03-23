import unittest

from core.letters_round import LettersRound
from core.susie_dent import SusieDent


class TestSusieDent(unittest.TestCase):

    def setUp(self):
        self.susie_dent = SusieDent()
        self.a_round = None  # Placeholder for LettersRound, if needed

    def test_is_valid_english_word(self):
        self.assertTrue(self.susie_dent.is_valid_english_word('mouse'))

    def test_proper_noun(self):
        self.assertFalse(self.susie_dent.is_valid_english_word('London'))

    def test_abbreviation(self):
        self.assertFalse(self.susie_dent.is_valid_english_word('UK'))

    def test_invalid_word(self):
        self.assertFalse(self.susie_dent.is_valid_english_word('swarzchbewgoooberOOooomelsh'))

    def test_single_letter(self):
        self.assertTrue(self.susie_dent.is_valid_english_word('a'))

    def test_plurals1(self):
        self.assertTrue(self.susie_dent.is_valid_english_word('cats'))

    def test_plurals2(self):
        self.assertTrue(self.susie_dent.is_valid_english_word('mice'))

    def test_scoring_1(self):
        letters = ['m', 'o', 'u', 's', 'e', 'c', 'a', 't']
        choices = {
            'team1': 'CAB',
            'team2': 'BEAD'
        }
        self.a_round = LettersRound()
        self.a_round.vowels = 4
        self.a_round.consonants = 5

        scores = self.a_round.score_round(choices, letters)
        self.assertEqual(scores['team1'], 3)
        self.assertEqual(scores['team2'], 4)

    def test_scoring_2(self):
        choices = {'player1': '123', 'player2': 'cat'}
        letters = ['c', 'a', 't']
        scores = self.

    def test_scoring_3(self):
        choices = {'player1': 'mouse', 'player2': '123'}
        letters = ['m', 'o', 'u', 's', 'e']
        self.assertEqual(self.susie_dent.scoring(choices, letters), {'player1': 5, 'player2': 0})

    def test_scoring_4(self):
        choices = {'player1': '123', 'player2': '456'}
        letters = []
        self.assertEqual(self.susie_dent.scoring(choices, letters), {'player1': 0, 'player2': 0})

    def test_scoring_5(self):
        choices = {'player1': 'astronaut', 'player2': 'beautiful'}
        letters = ['a', 's', 't', 'r', 'o', 'n', 'u', 't', 'b', 'e', 'a', 'u', 't', 'i', 'f', 'u', 'l']
        self.assertEqual(self.susie_dent.scoring(choices, letters), {'player1': 18, 'player2': 18})

    def test_could_we_have_done_any_better(self):
        letters = ['m', 'o', 'u', 's', 'e', 'c', 'a', 't']
        longest_words = self.susie_dent.could_we_have_done_any_better(letters, ['mouse', 'cat'])
        print(longest_words)
        self.assertTrue('mucosae' in longest_words)

    def test_get_valid_english_words(self):
        valid_words = self.susie_dent.get_valid_english_words()
        self.assertTrue(isinstance(valid_words, list))
        self.assertTrue(len(valid_words) > 0)
        self.assertTrue(all(isinstance(word, str) for word in valid_words))

if __name__ == '__main__':
    unittest.main()
