from snake import Snake
from turtle import Screen, Turtle
from food import Food
from scoreboard import Scoreboard
import time
import os


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
score = 0

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.create_block()
        # score += 1
        # os.system("cls")
        # print(f"Score = {score}")
        scoreboard.increase_score()

    if snake.check_collision() or snake.check_self_collission():
        # scoreboard.end_game()
        snake.reset()
        scoreboard.reset()


screen.exitonclick()
