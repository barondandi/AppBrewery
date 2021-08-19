''' VERSION 1
#1. Create a greeting for your program.
print("Welcome to Band Name Generator v1.0")
#2. Ask the user for the city that they grew up in.
print("In which city did you grow up?")
city = input()
#3. Ask the user for the name of a pet.
print("Can you give me the name of a pet?")
pet = input()
#4. Combine the name of their city and pet and show them their band name.
band_name = city + " " + pet
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/
print("Your band name could be " + band_name)
'''

print("┏━━┓━━━━━━━━━━━━┏┓━━━━━━━━━━━━━━━━━━━━━━━━━┏━━━┓━━━━━━━━━━━━━━━━━━━━━┏┓━━━━━━━━━━━━━━━━┏━━━┓━━┏━━━┓")
print("┃┏┓┃━━━━━━━━━━━━┃┃━━━━━━━━━━━━━━━━━━━━━━━━━┃┏━┓┃━━━━━━━━━━━━━━━━━━━━┏┛┗┓━━━━━━━━━━━━━━━┃┏━┓┃━━┃┏━┓┃")
print("┃┗┛┗┓┏━━┓━┏━┓━┏━┛┃━━━━┏━┓━┏━━┓━┏┓┏┓┏━━┓━━━━┃┃━┗┛┏━━┓┏━┓━┏━━┓┏━┓┏━━┓━┗┓┏┛┏━━┓┏━┓━━━━┏┓┏┓┗┛┏┛┃━━┃┃━┃┃")
print("┃┏━┓┃┗━┓┃━┃┏┓┓┃┏┓┃━━━━┃┏┓┓┗━┓┃━┃┗┛┃┃┏┓┃━━━━┃┃┏━┓┃┏┓┃┃┏┓┓┃┏┓┃┃┏┛┗━┓┃━━┃┃━┃┏┓┃┃┏┛━━━━┃┗┛┃┏━┛┏┛━━┃┃━┃┃")
print("┃┗━┛┃┃┗┛┗┓┃┃┃┃┃┗┛┃━━━━┃┃┃┃┃┗┛┗┓┃┃┃┃┃┃━┫━━━━┃┗┻━┃┃┃━┫┃┃┃┃┃┃━┫┃┃━┃┗┛┗┓━┃┗┓┃┗┛┃┃┃━━━━━┗┓┏┛┃┃┗━┓┏┓┃┗━┛┃")
print("┗━━━┛┗━━━┛┗┛┗┛┗━━┛━━━━┗┛┗┛┗━━━┛┗┻┻┛┗━━┛━━━━┗━━━┛┗━━┛┗┛┗┛┗━━┛┗┛━┗━━━┛━┗━┛┗━━┛┗┛━━━━━━┗┛━┗━━━┛┗┛┗━━━┛")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
city = input("In which city did you grow up?\n")
pet = input("Can you give me the name of a pet?\n")
band_name = city + " " + pet
print("Your band name could be " + band_name)


''' SOLUTION
print("Welcome to the Band Name Generator.")
street = input("What's name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet)
'''