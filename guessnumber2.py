#!/usr/bin/env python
import random
def main():

    """Start a number guessing game between apple, banana, cherry"""

    print("Guess the fruit!")
    mylist = ["apple", "banana", "cherry"]

    x = (random.choice(mylist))
    guess = None

    while x != guess:
        guess = str(input("Pick a fruit between apple, banana and cherry: "))
        if x == guess:
            print("You genius!")
        else:
            print("Try again")

main()
