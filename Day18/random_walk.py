import turtle as t
import random
screen = t.Screen()


tim = t.Turtle()
tim.pensize(10)
tim.speed(9)


color = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue',
         'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray']

for i in range(500):
    angle = random.randint(0, 3) * 90
    ran_color = random.choice(color)
    tim.color(ran_color)
    tim.fd(20)
    tim.setheading(angle)

screen.exitonclick()
