# Turtle Challenge 2: Draw a Dashed Line

from turtle import Turtle, Screen

jade = Turtle()

for _ in range(20):
    jade.forward(10)
    jade.penup()
    jade.forward(10)
    jade.pendown()


screen = Screen()
screen.exitonclick()
