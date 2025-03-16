import unittest
from core.words_db import WordsDb

class TestWordsDb(unittest.TestCase):

    def setUp(self):
        self.db = WordsDb(':memory:')
        self.generate_test_data_mode = False # Set to True to generate test data

    def test_insert_nine_letter_word(self):
        self.db.insert_nine_letter_word('abcdefghij')
        words = self.db.get_nine_letter_words()
        self.assertIn(('abcdefghij',), words)

    def test_insert_valid_word(self):
        self.db.insert_valid_word('cat')
        words = self.db.get_valid_words()
        self.assertIn(('cat',), words)

    def test_get_nine_letter_words(self):
        self.db.insert_nine_letter_word('abcdefghij')
        words = self.db.get_nine_letter_words()
        self.assertEqual(len(words), 1)
        self.assertEqual(words[0], ('abcdefghij',))

    def test_get_valid_words(self):
        self.db.insert_valid_word('cat')
        self.db.insert_valid_word('dog')
        words = self.db.get_valid_words()
        self.assertEqual(len(words), 2)
        self.assertIn(('cat',), words)
        self.assertIn(('dog',), words)

    def test_get_valid_words_by_length(self):
        self.db.insert_valid_word('cat')
        self.db.insert_valid_word('dog')
        self.db.insert_valid_word('elephant')
        words = self.db.get_valid_words(length=3)
        self.assertEqual(len(words), 2)
        self.assertIn(('cat',), words)
        self.assertIn(('dog',), words)

    def test_generate_test_data(self):
        if self.generate_test_data_mode:
            csv_path = '../data'
            self.db.save_words_to_csv(csv_path)
            # check that the files exist
            import os
            self.assertTrue(os.path.exists(f"{csv_path}/nine_letter_words.csv"))
            self.assertTrue(os.path.exists(f"{csv_path}/valid_words.csv"))

if __name__ == '__main__':
    unittest.main()