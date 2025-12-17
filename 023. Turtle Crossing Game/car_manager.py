from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()
        self.penup()
        self.car_starting_position()
        

    def create_car(self):
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(1, 2)
        self.setheading(180)

    def car_movement(self):
        self.forward(STARTING_MOVE_DISTANCE)
    
    def car_starting_position(self):
        self.goto(x=300, y=random.randint(-280, 280))    
        