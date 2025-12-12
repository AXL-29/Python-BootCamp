import turtle
from turtle import Turtle, Screen
import random

# tuple - is an ordered, immutable collection of items
# Key Features of a Tuple:
# Ordered                       - Items have a fixed position.
# Immutable                     - You cannot change, add, or remove items after creation.
# Allows duplicates             - Just like lists, tuples can have repeated elements.
# Can store mixed data types    - e.g., integer, strings, floats, objects.

# Syntax: A tuple is created using parentheses ():
my_tuple = (1,2,3)

# You can also create a tuple without a parentheses (tuple packing):
my_second_tuple = 1, 2, 3

# Single-item Tuple - a tuple with one element needs a comma:
my_third_tuple = (5, )  # tuple
not_a_tuple = (5)   # just an integer

# Use a Tuple when:
    # The data should not change.
    # You want the collection to be safe from accidental modification.
    # You need faster performance (tuples are slightly faster than lists).
    # You want to use it as a key in a dictionary (only immutable types allowed).


# Create turtle and screen objects
drawer = Turtle()
screen = Screen()

# List of colors to use for each polygon
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rgb_color = (r, g, b)

    return rgb_color

turns = [0, 90, 180, 270]

drawer.pensize(15)
drawer.speed("fastest")


for _ in range(300):
    drawer.color(random_color())
    drawer.forward(30)
    drawer.setheading(random.choice(turns))


screen.exitonclick()

