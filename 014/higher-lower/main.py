############### The Higher Lower Game #####################

# http://www.higherlowergame.com/
# What gets Googled more?
# A frustratingly addictive game of higher or lower using Google searches.
# The data is based on global monthly searches in 2017.

# The Higher Lower Game:

# Include an ASCII art logos.
# 1st time: Randomize 2 entries from the data list. Make sure that they do not overlap.
# 2nd time an followings: replace the 1st entry by the previous 2nd. Randomize 1 entry from the data list. Make sure that it does not overlap.
# Print the 2 choices including the art logos:
# art.logo +
# Compare A: {name}, a {description}, from {country}.
# art.vs
# Against B: {name}, a {description}, from {country}.
# Who has more followers? Type 'A' or 'B':
# Ask the user "Who has more followers? Type 'A' or 'B': "
# Check user's guess against actual answer.
# If the user is right print "You're right! Current score: x.". Ask again replacing the A choice by the previous B, and generating a new random B choice.
# If the user is wrong print "Sorry, that's wrong. Final score: x-1" and exit the program
# Track the number of successful turns.


#Variables
import random
from art import logo, vs
from game_data import data
from replit import clear
TURNS = 1
LOWER_NUMBER = 1
HIGHER_NUMBER = len(data)
# print(HIGHER_NUMBER)
CONTINUE_PLAYING = True
#I get the error when clearing the screen "TERM environment variable not set."
#SOLUTION: https://stackoverflow.com/questions/52895902/term-environemt-varaible-not-set-error-python
import os
os.environ.get('TERM', '')

#Functions
def initialize_screen(a_data, b_data):
    """Clears the screen and types the logo and limits"""
    # Initialize screen
    # Include an ASCII art logo.
    clear()
    print(logo)
    print(f"Compare A: {a_data['name']}, a {a_data['description']}, from {a_data['country']}.")
    print(vs)
    print(f"Against B: {b_data['name']}, a {b_data['description']}, from {b_data['country']}.")

def random_number(l_number, h_number):
    """Returns a random number within the specified range"""
    # With the previous line I see the description of the function when I use it
    r_number = random.randrange(start=l_number, stop=h_number, step=1)
    return r_number


def make_guess():
    #Input guess and make sure it's a'A' or 'B'. Returns the chosen letter
    # Ask the user "Who has more followers? Type 'A' or 'B': "
    continue_making_guess = True
    while continue_making_guess:
        chosen_letter = str(input("Who has more followers? Type 'A' or 'B': "))
        if (chosen_letter.upper() == 'A') or (chosen_letter.upper() == 'B'):
            continue_making_guess = False
            return chosen_letter
        else:
            print("Did not understand your choice. Possible answers are only 'A' or 'B': ")
def check_answer(a_count, b_count):
    #Checks wether the right answer it's a'A' or 'B'. Inputs are the 'follower_count' as integers. Returns the right letter
    if a_count >= b_count:
        right_answer = 'A'
    else:
        right_answer = 'B'
    return right_answer

def check_guess(i_guess, i_answer):
    '''Check guess versus answer and print a message accordingly. A wrong answer sets CONTINUE_PLAYING to False'''
    global CONTINUE_PLAYING
    global turns
    # If the user is right print "You're right! Current score: x.". Ask again replacing the A choice by the previous B, and generating a new random B choice.
    if i_guess == i_answer:
        print(f"You're right! Current score: {turns}.")
        CONTINUE_PLAYING = True
    # If the user is wrong print "Sorry, that's wrong. Final score: x-1" and exit the program
    else:
        print(f"Sorry, that's wrong. Final score: {turns - 1}")
        CONTINUE_PLAYING = False


#main

# 1st time: Randomize 2 entries from the data list. Make sure that they do not overlap.
# Start selecting 2 random numbers
choice_a = random_number(LOWER_NUMBER, HIGHER_NUMBER)
# Now setting the value to 0, 1, 49, 50, 51 to check behaviour
#choice_a = 1
#print(f"Choice A is {choice_a}")
choice_b = random_number(LOWER_NUMBER, HIGHER_NUMBER)
#print(f"Choice b is {choice_b}")
# Make sure that the second choice is different to the first one and if not change it
while choice_b == choice_a:
    choice_b = random_number(LOWER_NUMBER, HIGHER_NUMBER)
#   print(f"The new choice b is {choice_b}")

data_a = data[choice_a - 1]
#print(data_a)
#print(data_a['name'])
data_b = data[choice_b - 1]
initialize_screen(data_a, data_b)

while CONTINUE_PLAYING:
    #Input guess
    guess = make_guess()
    #Calculate the right answer
    answer = check_answer(data_a['follower_count'], data_b['follower_count'])
    print(f"The right answer is {answer}.")
    # Check user's guess against actual answer.
    clear()
    print(logo)
    check_guess(guess, answer)
    # Track the number of successful turns.
    turns += 1

