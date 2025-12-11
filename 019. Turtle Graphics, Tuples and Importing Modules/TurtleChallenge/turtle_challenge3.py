from turtle import Turtle, Screen
import random

# Create turtle and screen objects
drawer = Turtle()
screen = Screen()

# List of colors to use for each polygon
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "cyan", "magenta", "brown"]

# Draw polygons starting from 3 sides up to 10 sides
for sides in range(3, 11):
    drawer.color(random.choice(colors))   # Pick a random color for each shape
    angle = 360 / sides                   # Turning angle for a regular polygon

    # Draw a polygon with 'sides' number of sides
    for _ in range(sides):
        drawer.forward(100)               # Length of each side
        drawer.right(angle)               # Angle turn to complete the polygon

# Close the screen when clicked
screen.exitonclick()
