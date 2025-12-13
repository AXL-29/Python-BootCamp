# What is an Object?
    # An 'object' is real thing created from a class.
    # Think of a class as a blueprint, and an object is a real thing built from that blueprint

from turtle import Turtle, Screen

screen = Screen()
turtle1 = Turtle()
turtle2 = Turtle()

# Turtle, Screen                -> class(blueprint)
# turtle1, turtle2, screen      -> objects

# What is an instance
    #  a specific object created from a class

    # 'turtle1' is an instance of Turtle
    # 'turtle2' is another instance of Turtle
    # 'screen' is an instance of Screen

# Object = Instance()

# What is Object State
    # The current values of its attributes (variables)
    # This attributes describes the object

turtle1.color("green")
turtle1.color("blue")

screen.exitonclick()