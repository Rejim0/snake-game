from turtle import Turtle

# Starting positions for the 3 snake segments (head first, then body)
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

# How many pixels the snake moves each step
MOVE_DISTANCE = 20

# Heading degrees for each direction (turtle uses angles)
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        # List that holds all the turtle segments making up the snake
        self.segments = []
        # Build the initial snake using the starting positions
        self.create_snake()
        # The head is always the first segment in the list
        self.head = self.segments[0]

    def create_snake(self):
        # Loop through each starting position and create a segment there
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        # Create a single white square turtle and place it at the given position
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()  # lift pen so it doesn't draw lines when moving
        new_segment.goto(position)
        # Add it to the segments list so we can track it
        self.segments.append(new_segment)

    def extend(self):
        # Add a new segment at the tail's current position
        # It sits on top of the tail for one frame, then move() pulls them apart
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Move each segment (starting from the tail) to where the one in front of it was
        # We go backwards so we don't overwrite positions before copying them
        for seg in range(len(self.segments) - 1, 0, -1):
            x_corr = self.segments[seg - 1].xcor()
            y_corr = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_corr, y_corr)
        # After all segments have shuffled back, move the head forward
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # Only allow turning up if not already going down (can't reverse)
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Only allow turning down if not already going up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # Only allow turning left if not already going right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Only allow turning right if not already going left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
