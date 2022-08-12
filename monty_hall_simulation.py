#! /usr/bin/env python3
# Monty hall simulator, to prove the winning probability
# Let's make a deal

import random
import matplotlib.pyplot as plt
import numpy as np


# function to reveal the door that does not contain the prize
def get_non_prize_door(host, num_doors, player_choice):
    i = 1
    while i == host or i == player_choice:
        i = (i + 1) % num_doors

    return i


# function to switch the other unopened door
def switch_function(shown_door, num_doors, player_choice):
    i = 1
    while i == shown_door or i == player_choice:
        i = (i + 1) % num_doors

    return i


# function to simulate the game
def monty_hall_game(switch, num_tests):
    win_switch_cnt = 0
    win_no_switch_cnt = 0
    lose_switch_cnt = 0
    lose_no_switch_cnt = 0

    doors = [0, 1, 2]
    num_doors = len(doors)

    # Loop through player can play a game
    for i in range(0, num_tests):
        door_with_prize = random.randint(0, num_doors - 1)
        host = door_with_prize
        player_choice = random.randint(0, num_doors - 1)
        original_player_choice = player_choice
        show_door = get_non_prize_door(host, num_doors, player_choice)  # This will give the door with goat behind

        # User consent to switch to other unopened door
        if switch:
            player_choice = switch_function(show_door, num_doors, player_choice)

        # This will help to count the probability of winning
        if player_choice == door_with_prize and switch == False:
            # Players wins without switching
            win_no_switch_cnt += 1
        elif player_choice == door_with_prize and switch == True:
            # Players wins with switching
            win_switch_cnt += 1
        elif player_choice != door_with_prize and switch == False:
            # Players lost without switching
            lose_no_switch_cnt += 1
        elif player_choice != door_with_prize and switch == True:
            # Players lost with switching
            lose_switch_cnt += 1
        else:
            print("[-] SOMETHING IS WRONG")
    return win_no_switch_cnt, win_switch_cnt, lose_no_switch_cnt, lose_switch_cnt, num_tests


if __name__ == '__main__':
    # Let's play the game
    # x = monty_hall_game(True, 10000)

    # Create data visualization with winning percentage from always switching
    num_tests = []
    win_percentage = []
    switch = True
    y = -1
    z = -1
    for i in range(1, 2001):
        num_tests.append(i)
        y = monty_hall_game(switch, i)
        win_percentage.append((y[1] / y[4]) * 100)

    print("Win with switching percentage of test playing", y[4], ' game is:', y[1] / y[4] * 100, "%")
    print("Lose with switching percentage of test playing", y[4], ' game is:', y[3] / y[4] * 100, "%")
    print("Win without switching percentage of test playing", y[4], ' game is:', y[0] / y[4] * 100, "%")
    print("Lose without switching percentage of test playing", y[4], ' game is:', y[2] / y[4] * 100, "%")

    win_percentage = np.array([y[1] / y[4] * 100, y[3] / y[4] * 100])
    labels = ["Win Percentage", "Lose Percentage"]
    plt.pie(win_percentage, labels=labels, autopct='%1.2f%%')
    plt.title("Monty hall challenge with SWITCH")
    plt.show()
