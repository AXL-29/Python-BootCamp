# Turtle Challenge 1: Draw a Square.
from turtle import Turtle, Screen

jade = Turtle()
jade.shape("arrow")

for _ in range(4):
    jade.forward(100)
    jade.right(90)

screen = Screen()
screen.exitonclick()


# Notes: To refactor a variable name in one-go use (Shift + F6) then rename.

# Basic Import:

# Import a whole module - you bring in the entire module, and use its functions with the module name.
# syntax: import module_name

# Import specific functions or classes - this lets you skip writing the module name.
# syntax: from module_name import class_name, function_name

# Import everything from a module (not recommended) - avoids this in real projects because it can overwrite names accidentally.
# syntax: from module_name import *

# Import a module with an alias - useful if the module name is long.
# syntax: import module_name as alias_name
