import unittest
from core.susie_dent import SusieDent


class TestSusieDent(unittest.TestCase):

    def setUp(self):
        self.susie_dent = SusieDent()

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
        self.assertEqual(self.susie_dent.scoring('mouse', 'cat'), [5, 3])

    def test_scoring_2(self):
        self.assertEqual(self.susie_dent.scoring('123', 'cat'), [0, 3])

    def test_scoring_3(self):
        self.assertEqual(self.susie_dent.scoring('mouse', '123'), [5, 0])

    def test_scoring_4(self):
        self.assertEqual(self.susie_dent.scoring('123', '456'), [0, 0])

    def test_scoring_5(self):
        self.assertEqual(self.susie_dent.scoring('astronaut', 'beautiful'), [18, 18])

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
