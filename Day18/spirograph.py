import turtle as t
import random
screen = t.Screen()

tim = t.Turtle()
tim.speed(0.5)
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# color = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue',
#          'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray']


for i in range(72):
    tim.color(random_color())
    tim.circle(100)
    tim.left(5)


screen.exitonclick()
