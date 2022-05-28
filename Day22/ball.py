from turtle import Turtle
from score import Score

player1_score = Score(-100)
player2_score = Score(100)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.moveX = 10
        self.moveY = 10
        self.score1 = 0
        self.score2 = 0

    def ball_move(self):
        new_x = self.xcor() + self.moveX
        new_y = self.ycor() + self.moveY
        self.goto(new_x, new_y)

    def partition(self):
        pen = Turtle()
        pen.color("white")
        pen.hideturtle()
        pen.penup()
        pen.goto(0, 300)
        pen.right(90)
        pen.pensize(5)
        for i in range(30):
            pen.pendown()
            pen.forward(10)
            pen.penup()
            pen.forward(10)

    def detect_collision(self, paddle1, paddle2):
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()

        for block in paddle1:
            if self.distance(block) <= 20:
                self.bounce_x()

        for block in paddle2:
            if self.distance(block) <= 30:
                self.bounce_x()

        if self.xcor() > 380:
            self.position_reset()
            self.bounce_x()
            self.score2 += 1
            player2_score.score(self.score1)

        if self.xcor() < -380:
            self.position_reset()
            self.bounce_x()
            self.score1 += 1
            player1_score.score(self.score2)

    def bounce_y(self):
        self.moveY *= -1

    def bounce_x(self):
        self.moveX *= -1

    def position_reset(self):
        self.goto(0, 0)
