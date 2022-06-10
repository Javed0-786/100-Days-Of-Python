import numpy
from tkinter import *


# All the oparations like calculation and all


# Graphics User Interface
window = Tk()
window.geometry('400x700')
window.title("Calculator")
window.config(padx=50, pady=50)
canvas = Canvas(width=300, height=100, bg="green")
canvas.grid(row=0, column=0, columnspan=4)

image_1 = PhotoImage(file="images/1.png")
button_1 = Button(image=image_1)
button_1.grid(row=1, column=0)

image_2 = PhotoImage(file="images/2.png")
button_2 = Button(image=image_2)
button_2.grid(row=1, column=1)

image_3 = PhotoImage(file="images/3.png")
button_3 = Button(image=image_3)
button_3.grid(row=1, column=2)

image_4 = PhotoImage(file="images/4.png")
button_4 = Button(image=image_4)
button_4.grid(row=2, column=0)

image_5 = PhotoImage(file="images/5.png")
button_5 = Button(image=image_5)
button_5.grid(row=2, column=1)

image_6 = PhotoImage(file="images/6.png")
button_6 = Button(image=image_6)
button_6.grid(row=2, column=2)

image_7 = PhotoImage(file="images/7.png")
button_7 = Button(image=image_7)
button_7.grid(row=3, column=0)

image_8 = PhotoImage(file="images/8.png")
button_8 = Button(image=image_8)
button_8.grid(row=3, column=1)

image_9 = PhotoImage(file="images/9.png")
button_9 = Button(image=image_9)
button_9.grid(row=3, column=2)

image_0 = PhotoImage(file="images/0.png")
button_0 = Button(image=image_0)
button_0.grid(row=4, column=0)

window.mainloop()
