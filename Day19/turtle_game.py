from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")
run = True
colors = ["violet", "indigo", "blue", "green", "yellow", "red"]
turtles = []
k = 0
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, -120+k)
    turtles.append(new_turtle)
    k += 40

while run:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            run = False
            if turtle.pencolor() == user_bet:
                print('Hurrey You Won 😎')

            else:
                print("Alas You Lost the Game 🥺")

        else:
            ran_move = random.randint(0, 10)
            turtle.forward(ran_move)


screen.exitonclick()
