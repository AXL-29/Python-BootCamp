# Procedural Programming - is a programming paradigm (style of coding) that is based on procedures, 
# also called functions, methods, or routines. It focuses on writing step-by-step instructions that 
# tell the computer what to do in a logical sequence.

# Object Oriented Programming - is a style of programming where you structure your code using objects.
# An object represents a real-world thing and contains both data (variables) and behaviors (functions/methods).

# attributes - stores data about each object.
# methods - this performs an action using the object's attributes.
# object - is an actual thing made from class, each object has its own value.
# class - is like a blueprint, it defines what an object will have (attributes) and can do (methods)

from turtle import Turtle, Screen

# object = class()
johny = Turtle()
print(johny)


# object.attributes
my_screen = Screen()
print(my_screen.canvheight)

# object.method()
johny.shape("turtle")
johny.color("DarkBlue")
johny.forward(100)
my_screen.exitonclick()