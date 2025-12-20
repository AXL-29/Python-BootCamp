import random
from turtle import Turtle


class Food(Turtle):
    """Represents the food that the snake can eat."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.9, 0.9)  # Slightly smaller than a snake segment
        self.penup()
        self.refresh_food()

    def refresh_food(self):
        """Move the food to a random position on the screen."""
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)
