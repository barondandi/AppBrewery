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
TURNS_EASY = 10
TURNS_HARD = 5
LOWER_NUMBER = 1
HIGHER_NUMBER = 100
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
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {LOWER_NUMBER} and {HIGHER_NUMBER}.")

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
            print(f"You have {TURNS_EASY} attempts remaining to guess the number.")
            continue_choosing_difficulty = False
            return TURNS_EASY
        elif difficulty == "hard":
            print(f"You have {TURNS_HARD} attempts remaining to guess the number.")
            continue_choosing_difficulty = False
            return TURNS_HARD
        else:
            print("Did not understand your choice. I need to ask again")

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
initialize_screen()
answer = random_number(LOWER_NUMBER, HIGHER_NUMBER)
print(f"Pssst, the correct answer is {answer}")
turns = choose_difficulty()
while CONTINUE_PLAYING:
    #Input guess
    guess = make_guess()
    #Decrease the number of turns
    turns -= 1
    #Check the answer and act accordingly
    check_guess(guess, answer)

'''SOLUTION
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")
  
#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS
  
def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 
  
  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    
    #Let the user guess a number.
    guess = int(input("Make a guess: "))
    
    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")
  
  
game()
'''