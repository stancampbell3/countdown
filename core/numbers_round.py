import random


class NumbersRound:
    def __init__(self):
        self.large_numbers = [25, 50, 75, 100]
        self.small_numbers = list(range(1, 11)) * 2  # Small numbers range from 1 to 10, with duplicates

    def get_number_selections(self, num_large, num_small):
        if not (0 <= num_large <= 4):
            raise ValueError("The number of large numbers must be between 0 and 4.")
        if not (2 <= num_small <= 6):
            raise ValueError("The number of small numbers must be between 2 and 6.")
        if num_large + num_small != 6:
            raise ValueError("The total number of numbers must be 6.")

        selected_large = random.sample(self.large_numbers, num_large)
        selected_small = random.sample(self.small_numbers, num_small)
        self.numbers = selected_large + selected_small
        random.shuffle(self.numbers)
        return self.numbers

    def find_target_number(self):
        self.target_number = random.randint(101, 999)
        return self.target_number
