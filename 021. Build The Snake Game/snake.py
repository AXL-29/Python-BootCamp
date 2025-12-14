from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    """Snake composed of multiple Turtle segments."""

    def __init__(self):
        """Initialize the snake with its starting body."""
        self.segments = []
        self.create_snake()

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
