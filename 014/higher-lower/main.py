############### The Higher Lower Game #####################

# http://www.higherlowergame.com/
# What gets Googled more?
# A frustratingly addictive game of higher or lower using Google searches.
# The data is based on global monthly searches in 2017.

# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

#Variables
import random
from art import logo, vs
from game_data import data
from replit import clear
TURNS_EASY = 10
TURNS_HARD = 5
LOWER_NUMBER = 1
HIGHER_NUMBER = len(data)
# print(HIGHER_NUMBER)
CONTINUE_PLAYING = True
#I get the error when clearing the screen "TERM environment variable not set."
#SOLUTION: https://stackoverflow.com/questions/52895902/term-environemt-varaible-not-set-error-python
import os
os.environ.get('TERM', '')

#Functions
def initialize_screen():
    """Clears the screen and types the logo and limits"""
    # Initialize screen
    # Include an ASCII art logo.
    clear()
    print(logo)
    print(f"Compare A:")
#    print(f"I'm thinking of a number between {LOWER_NUMBER} and {HIGHER_NUMBER}.")
    print(vs)
    print(f"Against B:")

def random_number(l_number, h_number):
    """Returns a random number within the specified range"""
    # With the previous line I see the description of the function when I use it
    r_number = random.randrange(start=l_number, stop=h_number, step=1)
    return r_number


def make_guess():
    #Input guess and make sure it's an integer in range. Returns the chosen number
    continue_making_guess = True
    while continue_making_guess:
        chosen_number = int(input("Make a guess: "))
        if (chosen_number <= HIGHER_NUMBER) and (chosen_number >= LOWER_NUMBER):
            continue_making_guess = False
            return chosen_number
        else:
            print(f"Did not understand your choice. I need an integer between {LOWER_NUMBER} and {HIGHER_NUMBER}.")

def check_guess(i_guess, i_answer):
    '''Check guess versus answer and print a message accordingly. If win or out of turns sets CONTINUE_PLAYING to False'''
    global CONTINUE_PLAYING
    if i_guess == i_answer:
        print(f"You got it! The answer was {answer}.")
        CONTINUE_PLAYING = False
    elif i_guess > i_answer:
        print("Too high.")
        if turns > 0:
            print(f"Guess again.\nYou have {turns} attempts remaining to guess the number.")
        else:
            print("You've run out of guesses, you lose.")
            CONTINUE_PLAYING = False
    elif i_guess < i_answer:
        print("Too low")
        if turns > 0:
            print(f"Guess again.\nYou have {turns} attempts remaining to guess the number.")
        else:
            print("You've run out of guesses, you lose.")
            CONTINUE_PLAYING = False


#main
# Start selecting 2 random numbers
choice_a = random_number(LOWER_NUMBER, HIGHER_NUMBER)
print(f"Choice A is {choice_a}")
choice_b = random_number(LOWER_NUMBER, HIGHER_NUMBER)
print(f"Choice b is {choice_b}")
# Make sure that the second choice is different to the first one and if not change it
while choice_b == choice_a:
    choice_b = random_number(LOWER_NUMBER, HIGHER_NUMBER)
    print(f"The new choice b is {choice_b}")

initialize_screen()

while CONTINUE_PLAYING:
    #Input guess
    guess = make_guess()
    #Decrease the number of turns
    turns -= 1
    #Check the answer and act accordingly
    check_guess(guess, answer)
