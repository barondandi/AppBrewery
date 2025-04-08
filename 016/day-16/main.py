# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
#
# my_screen = Screen()
# print("my_screen resolution", my_screen.canvheight, "x", my_screen.canvwidth)
# #my_screen.bgcolor("orange")
#
# print(timmy.position())
# timmy.forward(100)
# print(timmy.position())
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)
print(table.align)
table.align = "l"
print(table)
print(table.align)
