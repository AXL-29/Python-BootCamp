from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SPAWN_CHANCE = 10  # controls random spawn, static at all levels

class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.goto(300, random.randint(-260, 280))
        new_car.setheading(180)
        self.cars.append(new_car)

    def spawn_car(self):
        """Random spawn, same at all levels"""
        if random.randint(1, SPAWN_CHANCE) == 1:
            self.create_car()

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)
            if car.xcor() < -320:
                car.hideturtle()
                self.cars.remove(car)

    def level_up(self):
        """Only speed increases"""
        self.car_speed += MOVE_INCREMENT
