import random
from password_art import logo
from password_words import word_list
from passwords_vars import number_of_words


print(logo)
game_is_finished = False
word_list_len = len(word_list) - 1
# print(word_list_len)
# print(word_list[word_list_len])

# List to check which words have already been used
used_words = []
for index in range(word_list_len):
    used_words.append(False)
# print(used_words)

# Generate random unused words
word_counter = number_of_words
words_chosen = []
while word_counter > 0:
    word_index = random.randint(0, word_list_len)
    if not used_words[word_index]:
        used_words[word_index] = True
        words_chosen.append(word_list[word_index])
        word_counter -= 1

print(words_chosen)

# while not game_is_finished:
