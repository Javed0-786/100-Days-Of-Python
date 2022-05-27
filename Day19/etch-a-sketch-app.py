import turtle as t


class Control:
    def __init__(self, turtle):
        self.turtle = turtle

    def move_fd(self):
        self.turtle.fd(10)

    def move_bd(self):
        self.turtle.fd(-10)

    def turn_left(self):
        self.turtle.left(90)

    def turn_right(self):
        self.turtle.right(90)

    def pen_up(self):
        self.turtle.penup()

    def pen_down(self):
        self.turtle.pendown()


tim = t.Turtle()
control = Control(tim)

screen = t.Screen()


screen.listen()
screen.onkeypress(fun=control.move_fd, key='w')
screen.onkeypress(fun=control.move_bd, key='s')
screen.onkey(fun=control.turn_left, key='a')
screen.onkey(fun=control.turn_left, key='d')
screen.onkey(fun=control.pen_up, key='space')
screen.onkey(fun=control.pen_down, key='j')

screen.exitonclick()
