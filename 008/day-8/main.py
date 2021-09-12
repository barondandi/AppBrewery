# Simple Function
def greet():
    print("This is")
    print("a simple")
    print("function")
greet()

#Function that allows for input
def greet_with_name(name):
    print(f"Hello {name}.")
    print(f"How do you do {name}?")
greet_with_name("Victor")

#Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}.")
    print(f"How is the weather in {location}?")
greet_with("Victor", "Madrid")
# To change the parameters order
greet_with(location = "Madrid", name = "Victor")