from turtle import Turtle

FONT = ("Courier", 14, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    """Displays and manages the current score and high score."""

    def __init__(self):
        super().__init__()
        self.score = 0          # Current game score
        self.high_score = 0     # Highest score achieved
        self.update_score()

    def update_score(self):
        """Refresh the score display on the screen."""
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT
        )

    def increase_score(self):
        """Increase score by one and update the display."""
        self.score += 1
        self.update_score()

    def reset(self):
        """Reset score and update high score if needed."""
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
