##Python Dictionaries
# Dictionaries in Python are used to store set of data like Key: Value pair
# the syntax of a dictionary in Python is very simple we use {} inside that
# we define {Key: Value}, to separate multiple values we use','

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

#Retrieving items from dictionary
print(programming_dictionary["Bug"])    # this will print the definition of Bug

#Adding items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

#Create an empty dictionary
empty_dictionary = {}

#Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

#Edit and item in a dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
programming_dictionary["Bug"] = "a moth in your computer"
print(programming_dictionary)

#Loop through a dictionary
for entry in programming_dictionary:
    print(f"The key is {entry}; and the value is \"{programming_dictionary[entry]}\".")

#Nesting
capitals = {
    "France" = "Paris",
    "Germany" = "Berlin",
}

#Nesting a list in a dictionary
travel_log = {
    "France" = ["Paris", "Lille", "Dijon"],
}
