import unittest
from core.conundrum_round import ConundrumRound
from core.susie_dent import SusieDent


class TestConundrumRound(unittest.TestCase):

    def setUp(self):
        self.conundrum_round = ConundrumRound()
        # let's get an instance of SusieDent to use to check the validity of words
        self.susie = SusieDent()

    def test_generate_conundrum(self):
        conundrum, solution = self.conundrum_round.generate_conundrum()
        print(f"Conundrum: {conundrum}, Solution: {solution}")
        self.assertEqual(len(conundrum), 9)
        self.assertEqual(len(solution), 9)
        self.assertNotEqual(conundrum, solution)
        self.assertTrue(solution.isalpha())
        self.assertTrue(conundrum.isalpha())
        self.assertCountEqual(conundrum, solution)
        # both should be valid English words
        self.assertTrue(self.susie.is_valid_english_word(conundrum))
        self.assertTrue(self.susie.is_valid_english_word(solution))

    def test_partition_words_by_letters(self):
        partitioned = self.conundrum_round.partition_words_by_letters(self.conundrum_round.word_list)
        self.assertTrue(isinstance(partitioned, dict))
        self.assertTrue(all(isinstance(k, str) for k in partitioned.keys()))
        self.assertTrue(all(isinstance(v, list) for v in partitioned.values()))
        self.assertTrue(all(len(v) > 0 for v in partitioned.values()))
        # Check if all words in the partitioned dictionary are valid English words
        for words in partitioned.values():
            for word in words:
                self.assertTrue(self.susie.is_valid_english_word(word))

    def test_partitioned_words(self):
        partitioned = self.conundrum_round.partitioned_words
        self.assertTrue(isinstance(partitioned, dict))
        self.assertTrue(all(isinstance(k, str) for k in partitioned.keys()))
        self.assertTrue(all(isinstance(v, list) for v in partitioned.values()))
        self.assertTrue(all(len(v) > 0 for v in partitioned.values()))

    def test_dump_word_list_to_csv(self):
        import os
        test_file_path = 'test_word_list.csv'
        self.conundrum_round.dump_word_list_to_csv(test_file_path)
        self.assertTrue(os.path.exists(test_file_path))

        # Check if the file is not empty
        with open(test_file_path, 'r') as file:
            content = file.read()
            self.assertTrue(len(content) > 0)

        # Clean up the test file
        os.remove(test_file_path)

    def test_dump_partitioned_words_to_csv(self):
        import os
        import csv
        test_file_path = 'test_partitioned_words.csv'
        with open(test_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            for key, words in self.conundrum_round.partitioned_words.items():
                writer.writerow([key] + words)

        self.assertTrue(os.path.exists(test_file_path))

        # Check if the file is not empty
        with open(test_file_path, 'r') as file:
            content = file.read()
            self.assertTrue(len(content) > 0)

        # Clean up the test file
        os.remove(test_file_path)

    def test_dump_valid_keys_to_csv(self):
        import os
        test_file_path = 'test_valid_keys.csv'
        self.conundrum_round.dump_valid_keys_to_csv(test_file_path)
        self.assertTrue(os.path.exists(test_file_path))

        # Check if the file is not empty
        with open(test_file_path, 'r') as file:
            content = file.read()
            self.assertTrue(len(content) > 0)

        # Clean up the test file
        # os.remove(test_file_path)

if __name__ == '__main__':
    unittest.main()