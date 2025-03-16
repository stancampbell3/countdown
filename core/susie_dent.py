from itertools import permutations

from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer


# Assume the wordnet data has been downloaded as in:
# import nltk
# nltk.download('wordnet')
# nltk.download('omw-1.4')


class SusieDent:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.debug_mode = True

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
            if self.debug_mode:
                print(f"Word '{word} is a valid single-letter word. 'i' and 'a' are valid.")
            return True

        if word[0].isupper():
            if self.debug_mode:
                print(f"Word '{word}' starts with an uppercase letter, indicating it may be a proper noun.")
            return False

        if not self.contains_vowels(test_word):
            if self.debug_mode:
                print(f"Word '{word}' does not contain any vowels.")
            return False

        if word == "I":
            if self.debug_mode:
                print("Word 'I' is a valid English word, but it is a proper noun")
            return False

        return True # assume words presented are valid unless proven otherwise (kludge)

    def scoring(self, team1_word, team2_word):
        team1_word = team1_word.lower()
        team2_word = team2_word.lower()
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

    def could_we_have_done_any_better(self, letters, target_words):
        letters = ''.join(letters).lower()

        target_word_lengths = [len(word) for word in target_words]
        max_target_length = max(target_word_lengths, default=0)

        # Generate all possible subsets of the given letters, starting with the longest
        # and stopping when a valid word is found or when the length of the subset is
        # less than the longest target word
        for i in range(len(letters), max_target_length, -1):
            for perm in permutations(letters, i):
                word = ''.join(perm)
                if (len(word) > max_target_length
                        and self.contains_vowels(word)
                        and self.is_valid_english_word(word)):
                    return [word]

        return []

    def contains_vowels(self, letters):
        for letter in letters:
            if letter.upper() in 'AEIOUYW':
                return True
        return False
