#!/usr/bin/env python3

"""working with if, elif, else, and while"""

round = 0
answer = " "


while round < 3 and answer.lower() != "brian":
    round = round + 1
    print("Finish the movie title, 'Monty Python\'s Life of ____'")
    answer = input("Your guess--> ")

    if answer.title() == 'Brian':
        print("Correct!!!")
    elif answer == 'shrubbery':
        print("!You gave the SUPER SECRET answer!")
    elif round==3:
        print("Sorry, the answer was Brian.")
    else:
        print("Nope, try again...")


