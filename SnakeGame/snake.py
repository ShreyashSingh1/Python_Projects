from turtle import Turtle
MOVE_DISTANCE = 20
"""Right = 0 left = 180 up = 90 down = 270"""


class Snake:
    def __init__(self):
        self.segments = []
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        # snake creation
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in self.starting_positions:
            self.add_seg(position)

    def move(self):
        for seg_no in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_no - 1].xcor()
            new_y = self.segments[seg_no - 1].ycor()
            self.segments[seg_no].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_seg(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("White")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_seg(self.segments[-1].position())
        # Return the turtle’s current location (x,y) i.e tuple of its Coordinates (as a Vec2D vector).

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def reset(self):
        for _ in self.segments:
            _.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
