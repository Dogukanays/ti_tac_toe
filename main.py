import random

spots = {num: "" for num in range(1, 10)}
current_score = {"USER": 0, "COMPUTER": 0}
chars = {"X": None, "O": None}


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


def select_player():
    user_choice = None
    selection_complete = False
    while not selection_complete:
        user_choice = input("Select your player, 'X' or 'O' : ").upper()
        if user_choice not in chars:
            print("This is not a valid choice, please try again")
        else:
            chars[user_choice] = "USER"
            selection_complete = True
    for char in chars:
        if char != user_choice:
            chars[char] = "COMPUTER"


def user_move(char):
    available_spots = [spot for spot in spots if spots[spot] == ""]
    spot_to_fill = None
    selection_complete = False
    while not selection_complete:
        spot_to_fill = input(f"What is your move, (type number among {available_spots}): ")
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


def gameboard_full():
    for spot in spots:
        if spots[spot] == "":
            return False
    return True


def is_trio(lst):
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


def is_game_ended():
    columns = [[spots[num], spots[num + 3], spots[num + 6]] for num in [1, 2, 3]]
    rows = [[spots[num], spots[num + 1], spots[num + 2]] for num in [1, 4, 7]]
    diagonal1 = [spots[1], spots[5], spots[9]]
    diagonal2 = [spots[3], spots[5], spots[7]]
    for item in is_trio(columns), is_trio(rows), is_trio(diagonal1), is_trio(diagonal2):
        if item:
            return item
    else:
        return False


def is_another_round():
    if input("Do you want another round? Type 'Y' or 'N' ").upper() == "N":
        declare_result()
        return False
    else:
        return True


def scoreboard(player):
    print(f"\nThis round has ended, the {player} has won!\n")
    current_score[player] += 1
    return print(f"Current score : {current_score}\n")


def declare_result():
    print("\nThen the game has ended!")
    if current_score["USER"] > current_score["COMPUTER"]:
        print("Congratulations, you have won!")
    elif current_score["USER"] < current_score["COMPUTER"]:
        print("You lost!")
    else:
        print("It's a tie!")


select_player()
game_ended = False
while not game_ended:
    if not gameboard_full():

        winner = is_game_ended()
        if winner:
            create_gameboard()
            spots = {num: "" for num in range(1, 10)}  # refresh gameboard
            scoreboard(chars[winner])
            if not is_another_round():
                game_ended = True
                break

        if chars["X"] == "USER":
            create_gameboard()
            user_move("X")
            if not gameboard_full():
                computer_move("O")

        else:
            if not gameboard_full():
                computer_move("X")
                create_gameboard()
                user_move("O")

    else:

        print(f"\nThis round has ended with a tie!\nCurrent score: {current_score}\n")
        if is_another_round():
            spots = {num: "" for num in range(1, 10)}  # refresh gameboard
        else:
            game_ended = True
