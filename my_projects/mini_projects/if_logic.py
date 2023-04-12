#!/usr/bin/env python3

"""Mini Project #1: If-Logic"""

#Rock Paper Scissors

#Random module?
import random

player_choice = input("Rock Paper Scissors, What's your choice?")

choices = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(choices)

print(f"{player_choice} vs {computer_choice}\n")



