from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class ScoreBoard(Turtle):
    """Handles displaying and updating the game score."""

    def __init__(self):
        """Set up the scoreboard with an initial score of zero."""
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        """Update the score display on the screen."""
        self.clear()
        self.write(
            f"Score: {self.score}",
            align=ALIGNMENT,
            font=(FONT)
        )

    def increase_score(self):
        """Increase the score by one and refresh the display."""
        self.score += 1
        self.update_score()

    def game_over(self):
        """Display the Game Over message."""
        self.goto(0, 0)
        self.write(
            "GAME OVER",
            align=ALIGNMENT,
            font=(FONT)
        )
