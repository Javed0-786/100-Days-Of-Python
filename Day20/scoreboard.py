from turtle import Turtle
ALINGMENT = "center"
FONT = ("Corier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALINGMENT,
                   font=FONT)

    def end_game(self):
        self.goto(0, 0)
        self.write(f"GAME OVER! ", align=ALINGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
