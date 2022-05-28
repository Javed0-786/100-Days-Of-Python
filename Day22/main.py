from turtle import Turtle, Screen
from player import Player
from ball import Ball
import time
X1 = 380

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Game")
screen.tracer(0)
game_is_on = True


player1 = Player(X1)
player2 = Player(-X1)
ball = Ball()
ball.partition()

screen.listen()
screen.onkey(fun=player1.move_up, key="Up")
screen.onkey(fun=player1.move_down, key="Down")
screen.onkey(fun=player2.move_up, key="w")
screen.onkey(fun=player2.move_down, key="s")


while True:
    time.sleep(0.03)
    ball.ball_move()
    ball.detect_collision(player1.blocks, player2.blocks)
    screen.update()

screen.exitonclick()
