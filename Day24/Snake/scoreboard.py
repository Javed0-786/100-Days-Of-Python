from turtle import Turtle
ALINGMENT = "center"
FONT = ("Corier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.fetch_high_score()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALINGMENT,
                   font=FONT)

    # def end_game(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER! ", align=ALINGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.store_high_score()
        self.score = 0
        self.update_scoreboard()

    def store_high_score(self):
        with open("score.txt", "w") as file:
            file.write(f"{self.high_score}")

    def fetch_high_score(self):
        with open("score.txt") as file:
            return int(file.read())
