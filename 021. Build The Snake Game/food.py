from turtle import Turtle
import random

class Food(Turtle):
    """Represents the food for the snake that appears at random positions."""

    def __init__(self):
        """Create the food as a small green circle and place it randomly."""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Move the food to a new random location on the screen."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
