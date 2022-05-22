import turtle as t
import time

screen = t.Screen()

tim = t.Turtle()
color = ["red", "green", "yellow", "purple", "black", "orange", "blue", "pink"]
angle = 120
k = 3
for i in color:
    for j in range(k):
        tim.color(i)
        tim.fd(100)
        tim.left(angle)

    k += 1
    angle = 180-((k-2) * 180)/k


screen.exitonclick()
