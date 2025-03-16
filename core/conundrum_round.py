import random
from nltk.corpus import words
from core.susie_dent import SusieDent

# Ensure the words corpus is downloaded
# Uncomment the following line if you haven't downloaded the words corpus yet
# import nltk
# nltk.download('words')

class ConundrumRound:
    def __init__(self):
        self.susie = SusieDent()
        self.word_list = [word for word in words.words() if len(word) == 9 and self.susie.is_valid_english_word(word)]

    def generate_conundrum(self):
        solution_word = random.choice(self.word_list)
        conundrum_word = ''.join(random.sample(solution_word, len(solution_word)))
        return conundrum_word, solution_word

