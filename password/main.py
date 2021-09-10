import random
from password_art import logo
from password_words import word_list
# from password_words_test_20 import word_list
from password_vars import number_of_words


print(logo)
game_is_finished = False
word_list_len = len(word_list) - 1
print(f"Dictionary has {word_list_len} words.")
# print(word_list[word_list_len])

# List to check which words have already been used
used_words = []
for index in range(word_list_len):
    used_words.append(False)
used_words_counter = len(used_words)
# print(used_words)
# print(len(used_words))
# print(type(used_words[word_list_len - 1]))

# Loop to keep on generating words unless told otherwise
while not game_is_finished:
    # Generate random unused words
    word_counter = number_of_words
    words_chosen = []
    while word_counter > 0 and used_words_counter > 0:
        word_index = random.randint(0, word_list_len - 1)
        if not used_words[word_index]:
            used_words[word_index] = True
            words_chosen.append(word_list[word_index])
            word_counter -= 1
            used_words_counter -= 1
    if used_words_counter < 1:
        print("Sorry, all words have been already used!")
        game_is_finished = True
    else:
        print(words_chosen)
    print('Press "ENTER" to continue. Any other letter plus "ENTER" to exit')
    if input() != "":
        game_is_finished = True
