#!/usr/bin/env python3

"""Mini Project #1: If-Logic"""

#Rock Paper Scissors

#Import modules
import random

def main():
    """Pylint really wanted a docstring here"""

#Useless nonsense for my amusement
    answer = input("\nHi! My name is Py. Do you want to play Rock Paper Scissors?\n").lower()

    if answer in ["yes", "ye", "y"]:
        print("\nYay!\n")
    elif answer in ["no", "n"]:
        print("\nI'm not letting you leave until you play. :)\n")
    else:
        print("\nI didn't understand your response.\nSo... We'll play anyway! :P\n")

#Acutual initial game input
    player_choice = input("Rock Paper Scissors, What's your choice?").title()

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

#Let's see who our winner is
    print(f"\n{player_choice} vs {computer_choice}\n")

    if player_choice == computer_choice:
        print("It's Tie!")
    elif (player_choice == "Rock" and computer_choice == "Paper"):
        print("Paper covers Rock. I win!")
    elif (player_choice == "Rock" and computer_choice == "Scissors"):
        print("Rock breaks Scissors. You win!")
    elif (player_choice == "Paper" and computer_choice == "Rock"):
        print("Paper covers Rock. You win!")
    elif (player_choice == "Paper" and computer_choice == "Scissors"):
        print("Scissors cuts Paper. I win!")
    elif (player_choice == "Scissors" and computer_choice == "Rock"):
        print("Rock breaks Scissors. I win!")
    elif (player_choice == "Scissors" and computer_choice == "Paper"):
        print("Scissors cuts Paper. You win!")
    elif player_choice in ["Lizard", "Spock"]:
        print("Nice try, but that's cheating. I win")
    else:
        print("I didn't understand you, so I win!!")

if __name__ == "__main__":
    main()
