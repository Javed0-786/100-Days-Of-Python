from turtle import Turtle, Screen
import pandas
import random


FONT = ("Corier", 11, "normal")
COLOR = ["red", "blue", "black", "violet", "green"]


screen = Screen()
image = "map.gif"

screen.addshape(image)
Turtle(shape=image)
pen = Turtle()
pen.penup()
pen.hideturtle()


data = pandas.read_csv("data.csv")
# print(type(data[data["state"] == user_response]))
states = data["states"].to_list()
states = [state.lower() for state in states]
left = True
# print(data)
print(states)
x_cors = data["x"].tolist()
y_cors = data["y"].tolist()
total_score = len(states)


def update_lists(index):
    states.pop(index)
    x_cors.pop(index)
    y_cors.pop(index)


def lessons():
    new_data = {
        "states": states,
        "x": x_cors,
        "y": y_cors
    }
    file = pandas.DataFrame(new_data)
    file.to_csv("Lessons.csv")


score = 0
while left:
    user_response = screen.textinput(
        f"{score} / {total_score} is correct", "What's another state's name: ")
    state = user_response.lower()
    if state in states:
        index = states.index(state)
        x = x_cors[index]
        y = y_cors[index]
        pen.goto(x, y)
        color = random.choice(COLOR)
        pen.color(color)
        pen.write(user_response, align="center", font=FONT)
        update_lists(index)
        score += 1

    elif state == "exit":
        left = False
        lessons()
        quit()

    if len(states) == 0:
        pen.goto(0, 0)
        pen.write("You Won The Game", align="center",
                  font=("Corier", 24, "normal"))

        left = False


screen.mainloop()
