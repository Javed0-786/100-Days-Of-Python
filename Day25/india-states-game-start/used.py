import turtle
import pandas

screen = turtle.Screen()
image = "map.gif"
screen.addshape(image)
pen = turtle.Turtle(shape=image)
pen.shapesize(0.5, 1)
# pen.hideturtle()
pen.penup()


# states = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh',
#           'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']


# x_cordiantes = []
# y_cordiantes = []
# # print(states)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#     x_cordiantes.append(x)
#     y_cordiantes.append(y)


turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
screen.mainloop()
data = {
    "states": states,
    "x": x_cordiantes,
    "y": y_cordiantes
}
df = pandas.DataFrame(data)
df.to_csv("data.csv")
