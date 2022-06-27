#!/usr/bin/env python

import random

def main():
    """Start a noble gas element guessing game."""
    print("Guess the element!")

    noblegas= [
        "helium",
        "neon",
        "argon",
        "krypton",
        "xenon",
        "radon",
        "oganesson"
        ]

    x = random.choice(noblegas)
    guess = None
    i = 0
    while x != guess:

        guess = str(input("What noble gas am I thinking of? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            i = i +1
            print("You guess correctly on your {}-times".format(i))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))
            i = i +1

main()