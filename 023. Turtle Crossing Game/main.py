import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # create cars randomly
    car_manager.spawn_car()

    # move all cars
    car_manager.move_cars()

    # detect collision
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # player reaches finish line
    if player.ycor() > 280:
        player.reset_position()
        car_manager.level_up()
        scoreboard.increase_level()
screen.exitonclick()
