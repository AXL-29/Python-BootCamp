from turtle import Turtle

FONT = ("Courier", 14, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=270)
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=("Courier", 24, "bold"))