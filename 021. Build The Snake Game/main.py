from turtle import Turtle, Screen
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


starting_position = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for coordinates in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(coordinates)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)

    for seg_num in range(len(segments) - 1, 0, -1):
        x = segments[seg_num - 1]. xcor()
        y = segments[seg_num - 1]. ycor()
        segments[seg_num].goto(x, y)
    segments[0].forward(20)
    segments[0].left(90)

screen.exitonclick()