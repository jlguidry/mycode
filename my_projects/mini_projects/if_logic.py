#!/usr/bin/env python3

"""Mini Project #1: If-Logic"""

#Rock Paper Scissors

#Random module?
import random

def(ques1):
    if ques1 == 'yes' or 'y':
        print('Rock, Paper, Scissors?')
    
    elif ques1 == 'no' or 'n':
        print("I\'m not letting you leave until you play :) ")
    else:
        print("You can only answer yes or no")
        return None
    return ques1
    
ques1 = input("\nHi! My name is Py. Do you want to play Rock Paper Scissors? yes/no \n")

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
    print("Rock smashes Scissors. You win!")
elif (player_choice == "Paper" and computer_choice == "Rock"):
    print("Paper covers Rock. You win!")
elif (player_choice == "Paper" and computer_choice == "Scissors"):
    print("Scissors cuts Paper. I win!")
elif (player_choice == "Scissors" and computer_choice == "Rock"):
    print("Rock smashes Scissors. I win!")
elif (player_choice == "Scissors" and computer_choice == "Paper"):
    print("Scissors cuts Paper. You win!")
else:
    print("I didn\'t understand you")



