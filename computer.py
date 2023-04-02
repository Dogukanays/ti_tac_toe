import random
from gameboard import GameBoard


class Computer(GameBoard):

    def __init__(self):
        self.char = None
        self.difficulty = None
        super().__init__()
        for char in self.chars:
            if self.chars[char][1] == "computer":
                self.char = char

    def difficulty_selection(self):
        while True:
            choice = input("Select your difficulty level(easy/normal/hard/expert): ").lower()
            if choice not in ["easy", "normal", "hard", "expert"]:
                print("This is not a valid choice, please follow the instructions.")
            else:
                break
        self.difficulty = choice

    def computer_offensive_strategy(self):
        all_triads = self.triads()
        for triad_kind in all_triads:
            for single_triad in all_triads[triad_kind]:
                char_found = 0
                for spot in single_triad:
                    if single_triad[spot] == self.char:
                        char_found += 1
                if char_found == 2:
                    for spot in single_triad:
                        if single_triad[spot] == "":
                            return spot

    def computer_defensive_strategy(self):
        all_triads = self.triads()
        for triad_kind in all_triads:
            for single_triad in all_triads[triad_kind]:
                char_found = 0
                for spot in single_triad:
                    if single_triad[spot] != self.char and single_triad[spot] != "":
                        char_found += 1
                if char_found == 2:
                    for spot in single_triad:
                        if single_triad[spot] == "":
                            return spot

    def move(self):
        num_for_possibilities = [1, 2, 3, 4]
        num = random.choice(num_for_possibilities)
        if self.difficulty == "easy":
            if num == 1 and self.computer_defensive_strategy():
                self.spots[self.computer_defensive_strategy()] = self.char
            else:
                available_spots = [spot for spot in self.spots if self.spots[spot] == ""]
                spot_to_fill = random.choice(available_spots)
                self.spots[spot_to_fill] = self.char

        elif self.difficulty == "normal":
            if num in [1, 2] and self.computer_offensive_strategy():
                self.spots[self.computer_offensive_strategy()] = self.char

            elif num in [1, 2] and self.computer_defensive_strategy():
                self.spots[self.computer_defensive_strategy()] = self.char

            else:
                available_spots = [spot for spot in self.spots if self.spots[spot] == ""]
                spot_to_fill = random.choice(available_spots)
                self.spots[spot_to_fill] = self.char

        elif self.difficulty == "hard":
            if num in [1, 2, 3] and self.computer_offensive_strategy():
                self.spots[self.computer_offensive_strategy()] = self.char

            elif num in [1, 2, 3] and self.computer_defensive_strategy():
                self.spots[self.computer_defensive_strategy()] = self.char

            else:
                available_spots = [spot for spot in self.spots if self.spots[spot] == ""]
                spot_to_fill = random.choice(available_spots)
                self.spots[spot_to_fill] = self.char
        else:

            if self.computer_offensive_strategy():
                self.spots[self.computer_offensive_strategy()] = self.char

            elif self.computer_defensive_strategy():
                self.spots[self.computer_defensive_strategy()] = self.char

            else:
                available_spots = [spot for spot in self.spots if self.spots[spot] == ""]
                spot_to_fill = random.choice(available_spots)
                self.spots[spot_to_fill] = self.char
