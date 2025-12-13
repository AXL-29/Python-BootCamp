from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forwards():
    turtle.forward(10)

def move_backwards():
    turtle.backward(10)

def move_counter_clockwise():
    turtle.left(10)

def move_clockwise():
    turtle.right(10)

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

# Functions as Inputs - means passing a function into another function as an argument
# instead of passing data like 'number' or 'strings'.

# def function_name1(something):
    # Do this with something
    # Then do this
    # Finally do this

# def function_name2():
    # Do this

# Then we can pass function_name2 to function_name1
# function_name1(function_name2)

screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()