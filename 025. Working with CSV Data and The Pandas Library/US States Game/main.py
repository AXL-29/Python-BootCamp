import turtle

# Set up screen and turtle
screen = turtle.Screen()
screen.setup(800, 800)

# Add the shape
img = "blank_states_img.gif"  # Use correct relative or absolute path
screen.addshape(img)
turtle.shape(img)

answer_state = screen.textinput(title="Guess the state",
                                prompt="What's another state's name?")