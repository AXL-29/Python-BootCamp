from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    """Controls the snake movement, growth, and reset behavior."""

    def __init__(self):
        self.segments = []              # List of snake body segments
        self.create_snake()
        self.head = self.segments[0]    # Reference to the snake's head

    def create_snake(self):
        """Create the initial snake body."""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, segment_position):
        """Add a new segment to the snake."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(segment_position)
        self.segments.append(new_segment)

    def extend_segment(self):
        """Extend the snake by adding a segment at the tail."""
        self.add_segment(self.segments[-1].position())

    def reset(self):
        """Remove the current snake and recreate it."""
        for segment in self.segments:
            segment.goto(1000, 1000)  # Move segments off-screen

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        """Move the snake forward."""
        # Move each segment to the position of the one in front
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(
                self.segments[i - 1].xcor(),
                self.segments[i - 1].ycor()
            )
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Change direction to up."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change direction to down."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change direction to left."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change direction to right."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
