import random
from collections import defaultdict
from nltk.corpus import words
import csv
from core.susie_dent import SusieDent

# Ensure the words corpus is downloaded
# Uncomment the following line if you haven't downloaded the words corpus yet
# import nltk
# nltk.download('words')

class ConundrumRound:
    def __init__(self):
        self.word_list = [word for word in words.words() if len(word) == 9 and word.isalpha()]
        self.partitioned_words = self.partition_words_by_letters(self.word_list)
        self.valid_keys = [key for key, some_words in self.partitioned_words.items() if len(some_words) > 1]

    def partition_words_by_letters(self, word_list):
        susie = SusieDent()
        partitions = defaultdict(list)
        for word in word_list:
            key = ''.join(sorted(word))
            if susie.is_valid_english_word(word) and len(key) == 9:
                partitions[key].append(word)
        return partitions

    def generate_conundrum(self):

        if not self.valid_keys:
            raise ValueError("No valid conundrums found.")

        key = random.choice(self.valid_keys)
        solution_word = random.choice(self.partitioned_words[key]).upper()
        other_choices = self.partitioned_words[key].copy()
        conundrum_word = random.choice(other_choices).upper()
        return conundrum_word, solution_word

    def dump_word_list_to_csv(self, file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Word'])
            for word in self.word_list:
                writer.writerow([word])

    def dump_valid_keys_to_csv(self, file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Key'])
            for key in self.valid_keys:
                writer.writerow([key])