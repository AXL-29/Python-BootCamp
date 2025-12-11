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