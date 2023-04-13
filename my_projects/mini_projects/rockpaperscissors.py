# -*- coding: utf-8 -*-
#!/usr/bin/env python3

#"""Mini Project #1: If-Logic"""

#Rock Paper Scissors

#Random module?

import random

answer = input("Hi! My name is Py. Do you want to play Rock Paper Scissors?\n")

if answer in ["yes", "ye", "y"]:
    print("Yay!") 
elif answer in ["no", "n"]:
    print("I\'m not letting you leave until you play :) ")
else:
     print("I didn't understand that, so we'll play anyway :P")

#initial input
player_choice = input("Rock Paper Scissors, What's your choice?").title()
    

choices = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(choices)

print(f"\n{player_choice} vs {computer_choice}\n")

if(player_choice == computer_choice):
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
else:
    print("I didn't understand you, so I win!!")
