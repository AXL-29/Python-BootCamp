from turtle import Turtle, Screen

# Set up the game screen
screen = Screen()
screen.setup(width=500, height=400)

# Prompt the user to place a bet on which turtle will win
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color: "
)

# Available turtle colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Store all turtle objects
turtles = []

def coordinates(turtle, x, y):
    """Move a turtle to a specific (x, y) position without drawing."""
    turtle.penup()
    turtle.goto(x, y)

# Starting position and spacing for turtles
start_y = -125
gap = 50
start_x = -230

# Create turtles, assign colors, and align them evenly on the Y-axis
for i, color in enumerate(colors):
    t = Turtle("turtle")
    t.color(color)
    coordinates(t, start_x, start_y + i * gap)
    turtles.append(t)

# Exit the program when the screen is clicked
screen.exitonclick()
