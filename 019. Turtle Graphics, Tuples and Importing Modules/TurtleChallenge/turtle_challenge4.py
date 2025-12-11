# Turtle Challenge 4: Draw a random walk
from turtle import Turtle, Screen
import random

# Create turtle and screen objects
drawer = Turtle()
screen = Screen()

# List of colors to use for each polygon
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "cyan", "magenta", "brown"]
turns = [0, 90, 180, 270]

drawer.pensize(15)
drawer.speed("fastest")


for _ in range(300):
    drawer.color(random.choice(colors))
    drawer.forward(30)
    drawer.setheading(random.choice(turns))


screen.exitonclick()
