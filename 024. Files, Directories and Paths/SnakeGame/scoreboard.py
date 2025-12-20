from turtle import Turtle

FONT = ("Courier", 14, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    """Shows and updates the current score and high score."""

    def __init__(self):
        """Initialize the scoreboard and load the high score from file."""
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        """Display the current score and high score."""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Add 1 to the current score and update the display."""
        self.score += 1
        self.update_score()

    def reset(self):
        """Reset the score and update the high score if the current score is higher."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()
