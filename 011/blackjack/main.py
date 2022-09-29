############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Variables
import random
from art import logo
from replit import clear
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
continue_playing = True
#I get the error when clearing the screen "TERM environment variable not set."
#SOLUTION: https://stackoverflow.com/questions/52895902/term-environemt-varaible-not-set-error-python
import os
os.environ.get('TERM', '')

#Functions
def deal_card():
    """Returns a random card from the deck"""
    # With the previous line I see the description of the function when I use it
    return random.choice(cards)

def calculate_score(input_cards):
    """Takes a list of cards and return the score calculated from the card"""
    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if len(input_cards) == 2 and sum(input_cards) == 21:
        return 0 #A Blackjack is returned as a 0
    # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    elif sum(input_cards) > 21:
        for i in range(len(input_cards)):
            if input_cards[i] == 11: #Checking if I have got an Ace. DEBUG: Does it for all the Aces in the hand (shorted out in the second if)
                input_cards[i] = 1
                if sum(input_cards) == 21:
                    return 21 #Faster than returning the sum
        return sum(input_cards)
    else:
        return sum(input_cards)

def compare(input_user_score, input_computer_score):
    """Compares user_score and computer_score and returns the outcome as a text string"""
    #If the computer and user both have the same score, then it's a draw
    if input_user_score == input_computer_score:
        return "It's a draw"
    #If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins."""
    elif input_user_score == 0:
        return "User blackjack. You win 😃"
    #If none of the above, then the player with the highest score wins."""
    elif input_user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

while continue_playing:
    #Variables
    continue_current_game = True
    continue_dealing = True
    computer_dealing = True

    print(logo)
    #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    #user_cards = []
    #computer_cards = []
    user_cards = []
    computer_cards = []

    #print(deal_card())
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #print(f"User cards: {user_cards}. Computer cards: {computer_cards}")

    #Hint 6: Create a function called calculate_score() that takes a List of cards as input
    #and returns the score.
    #Look up the sum() function to help you do this.


    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    #print(f"Computer cards: {computer_cards}, computer score: {computer_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if computer_score == 0:
        print("Computer blackjack. You lose 😤")
        continue_current_game = False
    elif user_score == 0:
        print("User blackjack. You win 😃")
        continue_current_game = False
    elif user_score > 21:
        print("You went over. You lose 😤")
        continue_current_game = False

    #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
    #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    while continue_current_game and continue_dealing:
        another_card = (input("Type 'y' to get another card, type 'n' to pass: ")).lower()
        if another_card == "y":
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")
            if user_score > 21:
                print("You went over. You lose 😤")
                continue_current_game = False
        else:
            continue_dealing = False

    #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while continue_current_game and computer_dealing:
        if computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
            if computer_score > 21:
                print(f"Your final hand: {user_cards}, final score: {user_score}")
                print(f"Computer's final hand: {computer_cards}, computer final score: {computer_score}")
                print("Computer went over. You win 😃")
                continue_current_game = False
            elif computer_score == 0:
                print(f"Your final hand: {user_cards}, final score: {user_score}")
                print(f"Computer's final hand: {computer_cards}, computer final score: {computer_score}")
                print("Computer blackjack. You lose 😤")
                continue_current_game = False
        else:
            computer_dealing = False

    #Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
    if continue_current_game:
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, computer final score: {computer_score}")
        print(compare(user_score, computer_score))
        continue_current_game = False

    #Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
    restart_game = (input("Type 'y' if you want to restart the game. Any other key to exit: ")).lower()
    if restart_game == "y":
        clear()
    else:
        continue_playing = False

