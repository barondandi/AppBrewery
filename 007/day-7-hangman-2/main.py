#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
# To initialize an empty list I use typecasting with list
display = list("")
# A more simple way of doing this is:
# display = []
# ERROR: range does not include the last number so there is no need to substract it
# for n in range(0, (len(chosen_word) - 1)):
# Should be
for n in range(0, len(chosen_word)):
# Or more simple:
# for n in range(len(chosen_word)):
    display.append("_")
# print(display)

guess = input("Guess a letter: ").lower()

#2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for n in range(0, (len(chosen_word) - 1)):
    letter = chosen_word[n]
    if letter == guess:
        display[n] = letter

#3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)