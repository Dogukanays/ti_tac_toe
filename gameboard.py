from game import Game


class GameBoard(Game):

    spots = {num: "" for num in range(1, 10)}

    def __init__(self):
        super().__init__()

    def create(self):
        gameboard = ""
        for spot in self.spots:
            if (spot - 1) % 3 == 0 or (spot - 1) % 3 == 1:  # is last spot of the row?
                if self.spots[spot] == "":
                    gameboard += " _ |"
                else:
                    gameboard += f" {self.spots[spot]} |"
            else:
                if self.spots[spot] == "":
                    gameboard += " _ \n"
                else:
                    gameboard += f" {self.spots[spot]} \n"
        # if self.round_end():
        #     pass
        else:
            return print(gameboard)

    def is_full(self):
        for spot in self.spots:
            if self.spots[spot] == "":
                return False
        return True

    def triads(self):

        columns = [{num: self.spots[num], num + 3: self.spots[num + 3], num + 6: self.spots[num + 6]} for num in
                   [1, 2, 3]]
        rows = [{num: self.spots[num], num + 1: self.spots[num + 1], num + 2: self.spots[num + 2]} for num in [1, 4, 7]]
        diagonals = [{1: self.spots[1], 5: self.spots[5], 9: self.spots[9]},
                     {3: self.spots[3], 5: self.spots[5], 7: self.spots[7]}]
        return {"columns": columns, "rows": rows, "diagonals": diagonals}

    def is_winner(self):
        all_triads = self.triads()
        for triad_kind in all_triads:
            for single_triad in all_triads[triad_kind]:
                char_found = []
                for spot in single_triad:
                    if single_triad[spot] != "":
                        char_found.append(single_triad[spot])
                if char_found.count("X") == 3 or char_found.count("O") == 3:
                    winner = single_triad[spot]
                    self.chars[winner][0] += 1
                    self.declare_current_score(winner)
                    return True

    def round_end(self):

        if not self.is_full():
            if self.is_winner():
                self.refresh_gameboard()
                return True
            else:
                return False

        else:
            self.create()
            if self.is_winner():
                # wins at last move
                self.refresh_gameboard()
                return True
            else:
                self.refresh_gameboard()
                print(
                    f"\nThis round has ended with a tie!"
                    f"\nCurrent score ➡️ 'X': {self.chars['X'][0]} - 'O': {self.chars['O'][0]}\n")
                return True

    @staticmethod
    def refresh_gameboard():
        GameBoard.spots = {num: "" for num in range(1, 10)}

    @staticmethod
    def another_round():
        while True:
            response = input("Do you want another round (yes/no)? ").lower()
            if response == "no":
                return False
            elif response == "yes":
                return True
            else:
                print("This is not a valid choice, please follow the instructions.\n")
