from turtle import Turtle, Screen
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def create_block(self):
        block = Turtle("square")
        block.color("white")
        block.penup()
        block_x = self.segments[len(self.segments)-1].xcor()
        block_y = self.segments[len(self.segments)-1].ycor()
        block.goto(block_x, block_y)
        self.segments.append(block)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    def check_collision(self):
        check_x = self.head.xcor()
        check_y = self.head.ycor()

        if check_x >= 300 or check_x <= -300 or check_y >= 310 or check_y <= -300:
            return True

        else:
            return False

    def check_self_collission(self):
        for segment_number in range(1, len(self.segments)):
            if self.head.distance(self.segments[segment_number]) < 10:
                return True

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
