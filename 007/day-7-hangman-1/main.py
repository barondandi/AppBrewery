#Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

#1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = word_list[random.randint(0, (len(word_list)) - 1)]
# There is a more simple way to write this:
# chosen_word = random.choice(word_list)
# print(chosen_word)

#2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess_unformatted = input("Guess a letter: ")
guess = guess_unformatted.lower()
# print(guess)

#3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in range(0, (len(chosen_word) - 1)):
# There is a more simple way to write this:
# for letter in chosen_word
    if chosen_word[letter].lower() == guess:
# This is the way of setting it lowe case
        print("Right")
    else:
        print("Wrong")

''' SOLUTION
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
'''