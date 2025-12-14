from turtle import Turtle, Screen

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_position = [(0, 0), (-20, 0), (-40, 0)]

for coordinates in starting_position:
    turtle = Turtle("square")
    turtle.color("white")
    turtle.goto(coordinates)

screen.exitonclick()