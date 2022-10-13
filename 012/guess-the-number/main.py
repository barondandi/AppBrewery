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
choose_difficulty = True
continue_playing = True
#I get the error when clearing the screen "TERM environment variable not set."
#SOLUTION: https://stackoverflow.com/questions/52895902/term-environemt-varaible-not-set-error-python
import os
os.environ.get('TERM', '')

#Functions
def random_number(l_number, h_number):
    """Returns a random number within the specified range"""
    # With the previous line I see the description of the function when I use it
    r_number = random.randrange(start=l_number, stop=h_number, step=1)
    return r_number

#Initialize screen
# Include an ASCII art logo.
clear()
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random_number(lower_number, higher_number)
print(f"Pssst, the correct answer is {answer}")

while choose_difficulty:
    difficulty = (input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()
    if difficulty == "easy":
        turns = turns_easy
        print(f"You have {turns} attempts remaining to guess the number.")
        choose_difficulty = False
    elif difficulty == "hard":
        turns = turns_hard
        print(f"You have {turns} attempts remaining to guess the number.")
        choose_difficulty = False
    else:
        print("Did not understand your choice. I need to ask again")

while continue_playing and (turns > 0):
    #Input guess and making sure it's an integer in range
    make_guess = true
    while make_guess:
        guess = int(input("Make a guess: "))
        if (make_guess <= higher_number) and (make_guess >= lower_number):
            make_guess = False
        else:
            print(f"Did not understand your choice. I need an integer between {lower_number} an {higher_number}.")
    #Decrease the number of turns
    turns -= 1
    #Check the answer and act accordingly
    if guess == answer:
        print("You win!")
        continue_playing = False
    elif guess > answer:
        print(f"Too high.\nGuess again.\nYou have {turns} attempts remaining to guess the number.")
    elif guess < answer:
        print(f"Too low.\nGuess again.\nYou have {turns} attempts remaining to guess the number.")
