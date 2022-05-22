# from turtle import Turtle, Screen
import turtle as t
screen = t.Screen()


tim = t.Turtle()

four = 20
while (four):
    four -= 1
    tim.pendown()
    tim.fd(10)
    tim.penup()
    tim.fd(10)


screen.exitonclick()
