from tkinter import *

root = Tk()
root.title("Button to lable")
root.minsize(200, 300)
my_lable = Label(text="How are you", font=("arial", 24, "bold"))
my_lable.pack()


def button_clicked():
    text_lable = input.get()
    my_lable.config(text=text_lable)


button = Button(text="Click Me", command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()
print(input.get())


root.mainloop()
