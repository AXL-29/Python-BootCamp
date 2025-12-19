from turtle import Turtle

STARTING_POSITION = [(20, 0), (0, 0), (-20, 0)]
DISTANCE_MOVEMENT = 20

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_segments = []
        self.snake()
        self.head = self.snake_segments[0]

    def snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.snake_segments.append(new_segment)

    def move(self):
        for i in range(len(self.snake_segments) -1, 0, -1):
            self.snake_segments[i].goto(
                self.snake_segments[i - 1].xcor(),
                self.snake_segments[i - 1].ycor()
            )
        self.head.forward(DISTANCE_MOVEMENT)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

