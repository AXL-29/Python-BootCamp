from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

# Heading constants
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Snake composed of multiple Turtle segments."""

    def __init__(self):
        """Initialize the snake with its starting body."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create the initial snake body from predefined positions."""
        for position in STARTING_POSITION:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        """Move the snake forward by one step."""
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(
                self.segments[i - 1].xcor(),
                self.segments[i - 1].ycor()
            )
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """Change the snake's head direction to up."""
        if self.head.setheading() != DOWN:
            self.head.setheading(UP)

    def up(self):
        """Change the snake's head direction to up, if not moving down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change the snake's head direction to down, if not moving up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change the snake's head direction to left, if not moving right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change the snake's head direction to right, if not moving left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

