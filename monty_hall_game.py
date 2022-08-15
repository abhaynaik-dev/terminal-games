#! /usr/bin/env python3
# Monty hall simulator
# Let's make a deal

import random

prizes = ["goat", "car", "goat"]
door_range = "(1-" + str(len(prizes)) + ")"


def choose_door(message):
    chosen_door = input(message)
    if not chosen_door.strip().isdigit():
        return choose_door("Please provide int to choose doors between " + door_range + ">")
    elif not 0 < int(chosen_door) < 4:
        return choose_door("Please choose doors between " + door_range + ">")
    else:
        return int(chosen_door) - 1


def lets_play():
    random.shuffle(prizes)  # This will shuffle the prizes behind doors
    host_door_choice = -1
    # Find out which door to open first
    user_door_choice = choose_door("Choose doors between " + door_range + ">")

    # This will randomly open a door which has a goat behind the door
    while True:
        host_door_choice = random.randint(0, len(prizes) - 1)
        if host_door_choice != user_door_choice and \
                prizes[host_door_choice] != "car":
            break
    print("Before I show you the prize,\n"
          "Let me show you door number ", host_door_choice + 1)
    print("Door number ", host_door_choice + 1, " has ... a `", prizes[host_door_choice], "`")

    # Ask user if he wants to change the choice
    user_door_choice = \
        choose_door("\nThis is your last chance! Do you want to SWITCH? \nChoose doors between " + door_range + ">")
    while user_door_choice == host_door_choice:
        user_door_choice = \
            choose_door("This door is already opened! \nChoose again between " + door_range + ">")

    # Declaring the prize
    print("` You get ... a", prizes[user_door_choice], "`")

    play_again = input("\nDo you want to play again? [yes/no]")
    if play_again.lower() == "yes":
        lets_play()
    else:
        quit()


if __name__ == '__main__':
    lets_play()
