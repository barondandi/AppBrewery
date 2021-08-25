import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

print(my_module.pi)

# Generates a random float between 0 an 1.0 -1 is NOT included-
random_float = random.random()
print(random_float)
# To generate a random float between 0 and 5
print (random_float * 5)

love_score = random.randint(1, 100)
print(f"Your Love Score is {love_score}.")