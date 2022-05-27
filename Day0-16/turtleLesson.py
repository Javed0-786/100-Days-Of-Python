# import turtle
# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.fd(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.align = 'r'
table.field_names = ["Name", "Type"]
table.add_rows([["Pikachu", "Electric"], [
    "Squirtle", "Water"], ["Charmander", "Fire"]])
print(table)
