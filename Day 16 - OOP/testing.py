# from turtle import Turtle, Screen
# import prettytable

# test = Turtle()

# print(test)

# test.shape("turtle")
# test.color(1,0,0)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table)