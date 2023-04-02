class Game:
    chars = {
        "X": [0, "user"],
        "O": [0, "user"]
    }

    def __init__(self):
        self.mode = None

    def game_mode_selection(self):
        while True:
            choice = input("Select your game mode(single/multiplayer): ").lower()
            if choice != "single" and choice != "multiplayer":
                print("This is not a valid choice, please follow the instructions.\n")
            else:
                break
        self.mode = choice

    # needed if game mode is single-player
    def player_selection(self):
        while True:
            choice = input("Select your player(X/O): ").upper()
            if choice not in self.chars:
                print("This is not a valid choice, please follow the instructions.")
            else:
                break
        for char in self.chars:
            if char != choice:
                self.chars[char][1] = "computer"

        return choice

    def declare_current_score(self, char):
        print(f"\nThis round has ended, the player '{char}' has won!\n")
        # create_gameboard()
        print(f"Current score ➡️ 'X': {self.chars['X'][0]} - 'O': {self.chars['O'][0]}\n")

    def declare_final_score(self):
        print("\nThen the game has ended!")
        if self.chars["X"][0] > self.chars["O"][0]:
            print("Player 'X' has won")
        elif self.chars["X"][0] < self.chars["O"][0]:
            print("Player 'O' has won")
        else:
            print("It's a tie!")
