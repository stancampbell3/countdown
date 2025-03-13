from itertools import permutations

from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer

# Assume the wordnet data has been downloaded as in:
# import nltk
# nltk.download('wordnet')
# nltk.download('omw-1.4')

def contains_vowels(letters):
    for letter in letters:
        if letter.upper() in 'AEIOUYW':
            return True
    return False


class SusieDent:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()

    def find_word_forms(self, test_word):
        test_word = test_word.lower()
        forms = set()

        # Check different parts of speech
        for pos in ['n', 'v', 'a', 'r']:
            lemmas = wn.lemmas(self.lemmatizer.lemmatize(test_word, pos=pos))
            for lemma in lemmas:
                forms.add(lemma.name())

        return forms

    def is_valid_english_word(self, word):
        test_word = word.lower()

        if len(test_word) == 1 and (test_word == 'a' or test_word == 'i'):
            return True

        if not contains_vowels(test_word):
            return False

        # heuristic for proper names, beginning with capital letter, needs work
        # covers all caps acronyms, but not all proper names
        if word == "I":
            return False
        if word[0].isupper() and len(word) > 1:
            return False

        # check if word has at least one word form in wordnet
        if len(self.find_word_forms(test_word)) > 0:
            return True
        else:
            return False

    def scoring(self, team1_word, team2_word):
        len_word1 = len(team1_word)
        len_word2 = len(team2_word)
        if len_word1 == 9:
            points1 = 18
        else:
            points1 = len_word1

        if len_word2 == 9:
            points2 = 18
        else:
            points2 = len_word2

        valid1 = self.is_valid_english_word(team1_word)
        valid2 = self.is_valid_english_word(team2_word)
        if not valid1:
            points1 = 0
        if not valid2:
            points2 = 0
        return [points1, points2]

    def could_we_have_done_better(self, letters, target_words):
            letters = ''.join(letters).lower()
            target_word_lengths = [len(word) for word in target_words]
            max_target_length = max(target_word_lengths, default=0)

            # Generate all possible subsets of the given letters
            for i in range(1, len(letters) + 1):
                for perm in permutations(letters, i):
                    word = ''.join(perm)
                    if self.is_valid_english_word(word) and len(word) > max_target_length:
                        return [word]

            return []