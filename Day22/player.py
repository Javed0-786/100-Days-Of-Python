from turtle import Turtle
# import time

# POSITIONS = [(-480, 0), (-480, -20), (-480, -40)]


class Player:
    def __init__(self, x):

        self.blocks = []
        self.x = x
        self.positions = [(self.x, 0), (self.x, -20),
                          (self.x, -40), (self.x, -60)]
        self.form_player()

    def form_player(self):
        for position in self.positions:
            block = Turtle("square")
            block.penup()
            block.color("white")
            block.setheading(90)
            block.goto(position)
            self.blocks.append(block)

    def move_up(self):
        for segment in self.blocks:
            segment.forward(40)

    def move_down(self):
        for segment in self.blocks:
            segment.forward(-40)
