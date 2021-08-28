import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Added debugging using a loop (not yet covered)
input_error = True
while input_error == True:
    player_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if player_selection >= 0 and player_selection <= 2:
        input_error = False
    else:
        print("ERROR with the selection. Please type '0', '1' or '2'.")

# Using the previous sequence to create a list
options = [rock, paper, scissors]
# print(options)
print(options[player_selection])

computer_selection = random.randint(0, 2)
print(f"Computer chose:\n{options[computer_selection]}")

# Now let's go for the winner
# One way is to create a 3 x 3 matrix with the possible combinations
# First index is player's choice, second index is computer choice
# "0" is a tie, "1" is player win and "2" is computer win.
result = [[0, 2, 1], [1, 0, 2], [2, 1, 0]]
# print(result)

if result[player_selection][computer_selection] == 0:
    print("It's a tie.")
elif result[player_selection][computer_selection] == 1:
    print("You win.")
else:
    print("You lose.")

''' SOLUTION
import random

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end
'''