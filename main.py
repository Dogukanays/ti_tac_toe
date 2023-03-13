import random

spots = {num: "" for num in range(1, 10)}
current_score = {"USER": 0, "COMPUTER": 0}


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
    player_options = ["X", "O"]
    user_choice = None
    computer_player = None
    selection_complete = False
    while not selection_complete:
        user_choice = input("Select your user_player, 'X' or 'O' : ").upper()
        if user_choice not in player_options:
            print("This is not a valid choice, please try again")
        else:
            selection_complete = True
    for char in player_options:
        if char != user_choice:
            computer_player = char
    return user_choice, computer_player


players = select_player()
user = players[0]
computer = players[1]


def user_move(char):
    available_spots = [spot for spot in spots if spots[spot] == ""]
    spot_to_fill = None
    selection_complete = False
    while not selection_complete:
        spot_to_fill = int(input(f"What is your move, (type number among {available_spots}): "))
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


def scoreboard(char):
    print(f"\nThis round has ended, the {char} has won!\n")
    for player in current_score:
        if player == char:
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


game_ended = False
while not game_ended:
    if not gameboard_full():
        create_gameboard()
        user_move(user)
        if not gameboard_full():
            computer_move(computer)
        winner = is_game_ended()
        if winner:
            create_gameboard()
            spots = {num: "" for num in range(1, 10)}  # refresh gameboard
            if winner == user:
                scoreboard("USER")
            else:
                scoreboard("COMPUTER")
            if input("Do you want another round? Type 'Y' or 'N' ").upper() == "N":
                game_ended = True
                declare_result()

    else:
        spots = {num: "" for num in range(1, 10)}  # refresh gameboard
