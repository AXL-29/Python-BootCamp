import turtle
import pandas as pd

# --- Setup screen ---
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=800, height=800)

# Load the map image
img = "blank_states_img.gif"
try:
    screen.addshape(img)
    turtle.shape(img)
except turtle.TurtleGraphicsError:
    print(f"Error: '{img}' not found. Please place it in the same directory.")
    turtle.bye()
    exit()

# Create a turtle for writing text
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

# Load CSV data
try:
    data = pd.read_csv("50_states.csv")
except FileNotFoundError:
    print("Error: '50_states.csv' not found. Please place it in the same directory.")
    turtle.bye()
    exit()

all_states = data.state.to_list()
guessed_states = []

# --- Game loop ---
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name? (Type 'Exit' to quit)"
    )

    if not answer_state:
        continue  # If user clicks cancel or enters nothing, ask again

    answer_state = answer_state.strip().title()

    if answer_state == "Exit":
        # Save missing states to a file
        missing_states = [state for state in all_states if state not in guessed_states]
        pd.DataFrame(missing_states).to_csv("states_to_learn.csv", index=False)
        print("Game ended. Missing states saved to 'states_to_learn.csv'.")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        x = int(state_data.x.iloc[0])
        y = int(state_data.y.iloc[0])
        pen.goto(x, y)
        pen.write(answer_state, align="center", font=("Courier", 12, "normal"))

# Keep window open until clicked
screen.mainloop()