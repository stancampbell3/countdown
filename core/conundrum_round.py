import random
from collections import defaultdict
from nltk.corpus import words
import csv

# Ensure the words corpus is downloaded
# Uncomment the following line if you haven't downloaded the words corpus yet
# import nltk
# nltk.download('words')

class ConundrumRound:
    def __init__(self):
        self.word_list = [word for word in words.words() if len(word) == 9 and word.isalpha()]
        self.partitioned_words = self.partition_words_by_letters(self.word_list)

    def partition_words_by_letters(self, word_list):
        partitions = defaultdict(list)
        for word in word_list:
            key = ''.join(sorted(word))
            partitions[key].append(word)
        return partitions

    def generate_conundrum(self):
        valid_keys = [key for key, words in self.partitioned_words.items() if len(words) > 1]
        if not valid_keys:
            raise ValueError("No valid conundrums found.")

        key = random.choice(valid_keys)
        solution_word = random.choice(self.partitioned_words[key]).upper()
        conundrum_word = ''.join(random.sample(solution_word, len(solution_word)))
        return conundrum_word, solution_word

    def dump_word_list_to_csv(self, file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Word'])
            for word in self.word_list:
                writer.writerow([word])
# Example usage
# conundrum_round = ConundrumRound()
# conundrum, solution = conundrum_round.generate_conundrum()
# print(f"Conundrum: {conundrum}, Solution: {solution}")