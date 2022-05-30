from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
# YCOR = [-240, -210, -180, -150, -120, -90, -
# 60, -30, 0, 30, 60, 90, 120, 150, 180, 210, 240]


class CarManager():

    def __init__(self):
        self.my_cars = []
        self.car_speed = 10
        self.cars_numbers = 6

    def new_car(self):
        chance = random.randint(1, self.cars_numbers)
        if chance == 1:
            car = Turtle()
            car.hideturtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(1, 2.5, 1)
            car.showturtle()
            y = random.randint(-250, 250)
            x = 280
            car.goto(x, y)
            self.my_cars.append(car)

    def move(self):
        for car in self.my_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        if self.car_speed % 3 == 0:
            self.cars_numbers -= 1
