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

state1 = "Delaware"
state2 = "Pennsylvania"

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# We define the order by the offset from the beginning
print(states_of_america[0])
# Last item of the list is -1 as there is not such a thing as -0
print(states_of_america[-1])

states_of_america[1] = "Pencilvania"
print(states_of_america)
states_of_america.append("Angelaland")
print(states_of_america)

print(len(states_of_america))

num_of_states = len(states_of_america)
# This gives an error:
# print(states_of_america[num_of_states])
# This is the right way to do do it as the first index of the list is 0
print(states_of_america[num_of_states - 1])

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

print(dirty_dozen[0])
print(dirty_dozen[1])

print(dirty_dozen[1][2])
print(dirty_dozen[1][3])