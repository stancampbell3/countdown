import wn

class SusieDent:
    def __init__(self):
        self.en_wordnet = wn.Wordnet('oewn:2024')

    def is_valid_english_word(self, word):
        test_word = word.lower()

        if len(test_word) == 1 and (test_word == 'a' or test_word == 'i'):
            return True

        synsets = self.en_wordnet.synsets(test_word)
        if not synsets:
            return False

        # heuristic for proper names, beginning with capital letter, needs work
        # covers all caps acronyms, but not all proper names
        if word == "I":
            return False
        if word[0].isupper() and len(word) > 1:
            return False

        return True

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