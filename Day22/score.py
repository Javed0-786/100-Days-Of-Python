from turtle import Turtle


class Score(Turtle):
    def __init__(self, X):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(X, 270)

    def score(self, score):
        self.clear()
        self.write(f"Score: {score}", align="center",
                   font=("Corier", 24, "normal"))
