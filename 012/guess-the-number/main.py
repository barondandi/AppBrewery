############### Number Guessing Game #####################

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

#Variables
import random
from art import logo
from replit import clear
turns_easy = 10
turns_hard = 5
lower_number = 1
higher_number = 100
continue_playing = True
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
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_number} and {higher_number}.")

def random_number(l_number, h_number):
    """Returns a random number within the specified range"""
    # With the previous line I see the description of the function when I use it
    r_number = random.randrange(start=l_number, stop=h_number, step=1)
    return r_number

def choose_difficulty():
    '''Asks for a difficulty and returns the number of turns based on the chosen difficulty'''
    continue_choosing_difficulty = True
    while continue_choosing_difficulty:
        difficulty = (input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()
        if difficulty == "easy":
            print(f"You have {turns_easy} attempts remaining to guess the number.")
            continue_choosing_difficulty = False
            return turns_easy
        elif difficulty == "hard":
            print(f"You have {turns_hard} attempts remaining to guess the number.")
            continue_choosing_difficulty = False
            return turns_hard
        else:
            print("Did not understand your choice. I need to ask again")

def make_guess():
    #Input guess and make sure it's an integer in range. Returns the chosen number
    continue_making_guess = True
    while continue_making_guess:
        chosen_number = int(input("Make a guess: "))
        if (chosen_number <= higher_number) and (chosen_number >= lower_number):
            continue_making_guess = False
            return chosen_number
        else:
            print(f"Did not understand your choice. I need an integer between {lower_number} and {higher_number}.")

def check_guess(i_guess, i_answer):
    global continue_playing
    if i_guess == i_answer:
        print(f"You got it! The answer was {answer}.")
        continue_playing = False
    elif i_guess > i_answer:
        print("Too high.")
        if turns > 0:
            print(f"Guess again.\nYou have {turns} attempts remaining to guess the number.")
        else:
            print("You've run out of guesses, you lose.")
            continue_playing = False
    elif i_guess < i_answer:
        print("Too low")
        if turns > 0:
            print(f"Guess again.\nYou have {turns} attempts remaining to guess the number.")
        else:
            print("You've run out of guesses, you lose.")
            continue_playing = False


#main
initialize_screen()
answer = random_number(lower_number, higher_number)
print(f"Pssst, the correct answer is {answer}")
turns = choose_difficulty()
while continue_playing:
    #Input guess
    guess = make_guess()
    #Decrease the number of turns
    turns -= 1
    #Check the answer and act accordingly
    check_guess(guess, answer)

