from game import Game
from gameboard import GameBoard
from user import User
from computer import Computer

game = Game()
game.game_mode_selection()

if game.mode == "single":
    char_choice = game.player_selection()
    user = User(char_choice)
    computer = Computer()
    computer.difficulty_selection()
else:
    user_1 = User("X")
    user_2 = User("O")

gameboard = GameBoard()

while True:

    if game.mode == "multiplayer":
        if not gameboard.round_end():
            gameboard.create()
            user_1.move()
        else:
            if not gameboard.another_round():
                game.declare_final_score()
                breaka

        if not gameboard.round_end():
            gameboard.create()
            user_2.move()

        else:
            if not gameboard.another_round():
                game.declare_final_score()
                break
            else:
                continue

    else:
        if user.char == "X":

            if not gameboard.round_end():
                gameboard.create()
                user.move()
            else:
                if not gameboard.another_round():
                    game.declare_final_score()
                    break
                else:
                    continue

            if not gameboard.round_end():
                computer.move()
            else:
                if not gameboard.another_round():
                    game.declare_final_score()
                    break
        else:
            if not gameboard.round_end():
                computer.move()
                if not gameboard.is_full():
                    gameboard.create()
            else:
                if not gameboard.another_round():
                    game.declare_final_score()
                    break
                else:
                    continue

            if not gameboard.round_end():
                user.move()
            else:
                if not gameboard.another_round():
                    game.declare_final_score()
                    break
