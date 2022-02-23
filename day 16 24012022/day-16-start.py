# from turtle import Turtle,Screen
#
# timmy = Turtle()
#
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.forward(100)
#
# print(timmy)
#
# my_screen = Screen()
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("name",["Hoang","Kt3","Quat Quat","Shinta"])
table.add_column("age",["23","23","23","23"])
print(table)