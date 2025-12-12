import random
import turtle
from turtle import Turtle, Screen
# import colorgram
#
# colors = colorgram.extract('hirst_painting.png', 50)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     rgb_colors.append((r, g, b))

color_list = [(230, 156, 93), (252, 236, 90), (50, 86, 167), (234, 85, 46), (142, 74, 51),
              (255, 99, 132), (54, 162, 235), (255, 206, 86), (75, 192, 192),
              (153, 102, 255), (255, 159, 64)]

t = Turtle()
screen = Screen()

# Turtle setup
t.shape("arrow")
t.color("black")
turtle.colormode(255)   # allow RGB values 0–255
t.speed("fast")         # draw as fast as possible
t.penup()               # no drawing while moving
t.hideturtle()          # hide turtle icon

# Move turtle to starting corner (bottom-left)
t.setheading(225)
t.forward(300)
t.setheading(0)

# Draw 10 rows × 10 columns of dots
for row in range(10):
    for col in range(10):
        t.dot(20, random.choice(color_list))  # draw a colorful dot
        t.forward(50) # space between dots

    # Move up to the next row
    t.setheading(90)
    t.forward(50)

    # Move back to start of the row (left side)
    t.setheading(180)
    t.forward(500)

    # Face right again for the next row
    t.setheading(0)
screen.exitonclick()