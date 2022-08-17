from turtle import Turtle
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0), (-60,0)]

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):

        for sq_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[sq_num - 1].xcor()
            new_y = self.segments[sq_num - 1].ycor()
            self.segments[sq_num].goto(new_x, new_y)
        self.head.forward(10)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.head.forward(1)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.head.forward(1)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.head.forward(1)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.head.forward(1)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.color("gold")
        self.segments.append(new_segment)

    def extend(self):
        for _ in range(0,2):
            self.add_segment(self.segments[-1].pos())

    def is_collision(self):
        for segment in self.segments:
            if self.head.distance(segment) < 0:
                return True

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
            seg.clear()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]