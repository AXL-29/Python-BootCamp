# Turtle Challenge 5: Make a Spirograph
import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()

turtle.colormode(255)   # allow RGB colors
t.speed("fastest")      # set speed

def random_color():
    """Generate a random rgb colors and return it"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rgb_color = (r, g, b)

    return rgb_color

# Draw a spirograph (circle tilted by small degrees repeatedly)
for _ in range(72):     # 360 / 5 = 72 circles (rotated 5 degrees each)
    t.color(random_color())
    t.circle(100)       # draw a circle of radius 100
    t.setheading(t.heading() + 5)   # tilt by 5 degrees

screen.exitonclick()