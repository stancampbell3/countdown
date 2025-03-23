import random
from core.susie_dent import SusieDent


class LettersRound:
    def __init__(self):
        self.susie_dent = SusieDent()
        self.vowels = 'A' * 15 + 'E' * 21 + 'I' * 13 + 'O' * 13 + 'U' * 5
        self.consonants = (
                'B' * 2 + 'C' * 3 + 'D' * 6 + 'F' * 2 + 'G' * 3 + 'H' * 2 +
                'J' * 1 + 'K' * 1 + 'L' * 5 + 'M' * 4 + 'N' * 8 + 'P' * 4 +
                'Q' * 1 + 'R' * 9 + 'S' * 9 + 'T' * 9 + 'V' * 1 + 'W' * 1 +
                'X' * 1 + 'Y' * 1 + 'Z' * 1
        )

    def select_letters(self, num_vowels, num_consonants):
        if num_vowels + num_consonants != 9:
            raise ValueError("The total number of letters must be 9.")
        if not (3 <= num_vowels <= 5):
            raise ValueError("The number of vowels must be between 3 and 5.")
        if not (4 <= num_consonants <= 6):
            raise ValueError("The number of consonants must be between 4 and 6.")

        letters = random.choices(self.vowels, k=num_vowels) + random.choices(self.consonants, k=num_consonants)
        random.shuffle(letters)
        return letters

    def score_round(self, choices, letters):
        scores = {}
        for player_id, word in choices.items():
            scores[player_id] = self.susie_dent.scoring({player_id: word})[player_id]
        return scores
