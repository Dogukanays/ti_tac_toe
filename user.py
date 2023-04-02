from gameboard import GameBoard


class User(GameBoard):

    def __init__(self, char):
        self.char = char
        super().__init__()

    def move(self):
        available_spots = [spot for spot in self.spots if self.spots[spot] == ""]
        while True:
            spot_to_fill = input(f"\nWhat is your move{available_spots}?: ")
            if spot_to_fill.isdigit():
                spot_to_fill = int(spot_to_fill)
            if spot_to_fill not in self.spots:
                print("This is not a valid choice, please follow the instructions.\n")
            else:
                if spot_to_fill not in available_spots:
                    print("This spot has already been filled, please try again.")
                else:
                    break
        self.spots[spot_to_fill] = self.char
