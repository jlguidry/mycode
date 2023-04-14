#!/usr/bin/env python3

"""Mini Project #1: If-Logic"""

#Rock Paper Scissors

#Import modules
import random

import crayons

def main():
    """Pylint really wanted a docstring here"""

#Useless nonsense for my amusement
    answer = input(crayons.yellow("\nHi! My name is Py. Do you want to play Rock Paper Scissors?\n")).lower()

    if answer in ["yes", "ye", "y"]:
        print(crayons.yellow("\nYay!\n"))
    elif answer in ["no", "n"]:
        print(crayons.red("\nI'm not letting you leave until you play. :)\n"))
    else:
        print(crayons.cyan("\nI didn't understand your response.\nSo... We'll play anyway! :P\n"))

#Acutual initial game input
    player_choice = input(crayons.yellow("Rock Paper Scissors, What's your choice?\n\n>>>")).title()

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

#Let's see who our winner is

#couldn't use "\n" in an f string)

    print("\n")
    print(f"{crayons.red(player_choice)} vs {crayons.cyan(computer_choice)}")
    print("\n")

    if player_choice == computer_choice:
        print(crayons.blue("It's Tie!"))
    elif (player_choice == "Rock" and computer_choice == "Paper"):
        print(crayons.blue("Paper covers Rock. I win!"))
    elif (player_choice == "Rock" and computer_choice == "Scissors"):
        print(crayons.blue("Rock breaks Scissors. You win!"))
    elif (player_choice == "Paper" and computer_choice == "Rock"):
        print(crayons.blue("Paper covers Rock. You win!"))
    elif (player_choice == "Paper" and computer_choice == "Scissors"):
        print(crayons.blue("Scissors cuts Paper. I win!"))
    elif (player_choice == "Scissors" and computer_choice == "Rock"):
        print(crayons.blue("Rock breaks Scissors. I win!"))
    elif (player_choice == "Scissors" and computer_choice == "Paper"):
        print(crayons.blue("Scissors cuts Paper. You win!"))
    elif player_choice in ["Lizard", "Spock"]:
        print(crayons.green("Nice try, but that's cheating. I win"))
    else:
        print(crayons.red("I didn't understand you, so I win!!"))
    print("\n")    

if __name__ == "__main__":
    main()
