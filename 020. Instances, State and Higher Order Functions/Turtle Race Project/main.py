import random
from turtle import Turtle, Screen
import time

# -------------------- Screen Setup --------------------
screen = Screen()
screen.setup(width=600, height=400)
screen.title("Turtle Race 🐢")

# Prompt user for a bet
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color: "
)

if user_bet:
    user_bet = user_bet.lower()

# -------------------- Turtle Setup --------------------
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

def coordinates(new_turtle, x, y):
    """Move a turtle to a specific (x, y) position without drawing."""
    new_turtle.penup()
    new_turtle.goto(x, y)

# Starting position and spacing
start_y = -125
gap = 50
start_x = -230

for i, color in enumerate(colors):
    t = Turtle("turtle")
    t.color(color)
    t.shape("turtle")
    coordinates(t, start_x, start_y + i * gap)
    turtles.append(t)

# -------------------- Finish Line --------------------
finish_line = Turtle()
finish_line.hideturtle()
finish_line.penup()

# Start finish line slightly below the first turtle
finish_start_y = start_y - 20
finish_line.goto(230, finish_start_y)
finish_line.pendown()
finish_line.left(90)

# Total height to cover all turtles dynamically
num_turtles = len(turtles)
line_height = gap * (num_turtles - 1) + 40  # 40 = padding above & below
finish_line.forward(line_height)

# Label the finish line at the top
finish_line.penup()
finish_line.goto(235, finish_start_y + line_height - 20)
finish_line.write("Finish", align="left", font=("Arial", 12, "bold"))

# -------------------- Countdown --------------------
for i in range(3, 0, -1):
    screen.title(f"Turtle Race starts in {i}...")
    time.sleep(1)
screen.title("Go! 🏁")

# -------------------- Race Logic --------------------
is_race_on = bool(user_bet)

winner_display = Turtle()
winner_display.hideturtle()
winner_display.penup()

while is_race_on:
    for turtle in turtles:
        distance = random.randint(0, 5)
        turtle.forward(distance)

        # Check if a turtle has crossed the finish line
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                result_text = f"You've won! The {winning_color} turtle is the winner 🏆"
            else:
                result_text = f"You've lost! The {winning_color} turtle is the winner ❌"

            # Display the result on screen
            winner_display.goto(-200, 170)
            winner_display.write(result_text, font=("Arial", 16, "bold"))

# -------------------- Exit --------------------
screen.exitonclick()
