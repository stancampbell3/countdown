import random
import string
from core.susie_dent import SusieDent

class LettersRound:
    def __init__(self):
        self.susie_dent = SusieDent()

    def select_letters(self, num_vowels, num_consonants):
        if num_vowels + num_consonants != 9:
            raise ValueError("The total number of letters must be 9.")
        if not (3 <= num_vowels <= 5):
            raise ValueError("The number of vowels must be between 3 and 5.")
        if not (4 <= num_consonants <= 6):
            raise ValueError("The number of consonants must be between 4 and 6.")

        vowels = 'AEIOU'
        consonants = ''.join(set(string.ascii_uppercase) - set(vowels))

        self.letters = random.choices(vowels, k=num_vowels) + random.choices(consonants, k=num_consonants)
        random.shuffle(self.letters)
        return self.letters

    def score_round(self, team1_word, team2_word, letters):
        if not all(letter in letters for letter in team1_word.upper()):
            team1_score = 0
        else:
            team1_score = self.susie_dent.scoring(team1_word, team2_word)[0]

        if not all(letter in letters for letter in team2_word.upper()):
            team2_score = 0
        else:
            team2_score = self.susie_dent.scoring(team1_word, team2_word)[1]

        return team1_score, team2_score