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
    mode = input("Please select your game mode. Type 's' for single-player, 'm' for multiplayer: ").lower()
    return mode


# needed if game mode is single-player
def player_selection():
    choice = None
    selection_complete = False
    while not selection_complete:
        choice = input("Select your player, 'X' or 'O' : ").upper()
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
        spot_to_fill = input(f"What is your move{available_spots}: ")
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


def check_trio(lst):
    if type(lst[0]) == list:
        # if that list represents a row or a column
        for item in lst:
            if item[0] != "" and item.count(item[0]) == len(item):
                return item[0]
        return False
    else:
        # for diagonals
        if lst[0] != "" and lst.count(lst[0]) == len(lst):
            return lst[0]
        else:
            return False


def check_winner():
    columns = [[spots[num], spots[num + 3], spots[num + 6]] for num in [1, 2, 3]]
    rows = [[spots[num], spots[num + 1], spots[num + 2]] for num in [1, 4, 7]]
    diagonal1 = [spots[1], spots[5], spots[9]]
    diagonal2 = [spots[3], spots[5], spots[7]]
    for item in (check_trio(columns), check_trio(rows), check_trio(diagonal1), check_trio(diagonal2)):
        if item:
            return item
    else:
        return False


def round_end():
    if not gameboard_full():
        winner = check_winner()
        if winner:
            chars[winner][0] += 1
            declare_current_score(winner)
            return True

        else:
            return False

    else:
        print(f"\nThis round has ended with a tie!\nCurrent score ➡️ 'X': {chars['X'][0]} - 'O': {chars['O'][0]}\n")
        return True


def another_round():
    if input("Do you want another round (yes/no)? ").lower() == "no":
        return False
    else:
        return True


def declare_current_score(char):
    print(f"\nThis round has ended, the player '{char}' has won!\n")
    print(f"Current score ➡️ 'X': {chars['X'][0]} - 'O': {chars['O'][0]}")


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

game_is_on = True
while game_is_on:
    if game_mode == "m":
        create_gameboard()
        move("X")
        create_gameboard()
        move("O")
    else:
        if chars["X"][1] == "user":
            create_gameboard()
            move("X")
            if not gameboard_full():
                computer_move("O")

        else:
            if not gameboard_full():
                computer_move("X")
                create_gameboard()
                move("O")

    if round_end():
        spots = {num: "" for num in range(1, 10)}
        if not another_round():
            declare_final_result()
            game_is_on = False
