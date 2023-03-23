import random

spots = {num: "" for num in range(1, 10)}
chars = {
    "X": [0, "user"],
    "O": [0, "user"]
}


def create_gameboard():
    gameboard = ""
    for spot in spots:
        if (spot - 1) % 3 == 0 or (spot - 1) % 3 == 1:  # is last spot of the row?
            if spots[spot] == "":
                gameboard += " _ |"
            else:
                gameboard += f" {spots[spot]} |"
        else:
            if spots[spot] == "":
                gameboard += " _ \n"
            else:
                gameboard += f" {spots[spot]} \n"
    return print(gameboard)


def game_mode_selection():
    mode = None
    selection_complete = False
    while not selection_complete:
        mode = input("Please select your game mode. Type 's' for single-player, 'm' for multiplayer: ").lower()
        if mode != "s" and mode != "m":
            print("This is not a valid choice, please follow the instructions.\n")
        else:
            selection_complete = True
    return mode


# needed if game mode is single-player
def player_selection():
    choice = None
    selection_complete = False
    while not selection_complete:
        choice = input("\nSelect your player, 'X' or 'O' : ").upper()
        if choice not in chars:
            print("This is not a valid choice, please try again")
        else:
            selection_complete = True
    for char in chars:
        if char != choice:
            chars[char][1] = "computer"


def gameboard_full():
    for spot in spots:
        if spots[spot] == "":
            return False
    return True


def move(char):
    available_spots = [spot for spot in spots if spots[spot] == ""]
    spot_to_fill = None
    selection_complete = False
    while not selection_complete:
        spot_to_fill = input(f"\nWhat is your move{available_spots}?: ")
        if spot_to_fill.isdigit():
            spot_to_fill = int(spot_to_fill)
        if spot_to_fill not in spots:
            print("This is not a valid choice, please follow the instructions.\n")
        else:
            if spot_to_fill not in available_spots:
                print("This spot has already been filled, please try again.")
            else:
                selection_complete = True
    spots[spot_to_fill] = char


def computer_move(char):
    available_spots = [spot for spot in spots if spots[spot] == ""]
    spot_to_fill = random.choice(available_spots)
    spots[spot_to_fill] = char


def triads():
    columns = [[spots[num], spots[num + 3], spots[num + 6]] for num in [1, 2, 3]]
    rows = [[spots[num], spots[num + 1], spots[num + 2]] for num in [1, 4, 7]]
    diagonals = [[spots[1], spots[5], spots[9]], [spots[3], spots[5], spots[7]]]
    return columns + rows + diagonals


def is_winner():
    for triad in triads():
        if triad.count("X") == 3 or triad.count("O") == 3:
            winner = triad[0]
            chars[winner][0] += 1
            declare_current_score(winner)
            return True


def round_end():
    global spots
    if not gameboard_full():
        if is_winner():
            spots = {num: "" for num in range(1, 10)}
            return True
        else:
            return False

    else:
        create_gameboard()
        if is_winner():
            spots = {num: "" for num in range(1, 10)}
            return True
        else:
            spots = {num: "" for num in range(1, 10)}
            print(f"\nThis round has ended with a tie!\nCurrent score ➡️ 'X': {chars['X'][0]} - 'O': {chars['O'][0]}\n")
            return True


def another_round():
    if input("Do you want another round (yes/no)? ").lower() == "no":
        return False
    else:
        return True


def declare_current_score(char):
    print(f"\nThis round has ended, the player '{char}' has won!\n")
    create_gameboard()
    print(f"Current score ➡️ 'X': {chars['X'][0]} - 'O': {chars['O'][0]}\n")


def declare_final_result():
    print("\nThen the game has ended!")
    if chars["X"][0] > chars["O"][0]:
        print("Player 'X' has won")
    elif chars["X"][0] < chars["O"][0]:
        print("Player 'O' has won")
    else:
        print("It's a tie!")


game_mode = game_mode_selection()
if game_mode == "s":
    player_selection()

while True:
    # First Path: Multiplayer mode
    if game_mode == "m":
        if not round_end():
            create_gameboard()
            move("X")
        else:
            if not another_round():
                declare_final_result()
                break
            else:
                continue

        if not round_end():
            create_gameboard()
            move("O")
        else:
            if not another_round():
                declare_final_result()
                break
            else:
                continue
    else:
        # Second Path: Single-player mode with player "X"
        if chars["X"][1] == "user":

            if not round_end():
                create_gameboard()
                move("X")
            else:
                if not another_round():
                    declare_final_result()
                    break
                else:
                    continue

            if not round_end():
                computer_move("O")
            else:
                if not another_round():
                    declare_final_result()
                    break
        # Third Path: Single-player mode with player "O"
        else:
            if not round_end():
                computer_move("X")
                if not gameboard_full():
                    create_gameboard()
            else:
                if not another_round():
                    declare_final_result()
                    break
                else:
                    continue

            if not round_end():
                move("O")
            else:
                if not another_round():
                    declare_final_result()
                    break
