from tkinter import *

root = Tk()
root.minsize(width=300, height=150)
root.title("Unit Convertor")
root.config(padx=10, pady=10)
input = Entry(width=10)
input.insert(END, string="0")
# input.config(padx=10, pady=20)
input.grid(row=0, column=1)


def calculation():
    result = 1.609 * int(input.get())
    label_3.config(text=round(result, 2))


label_1 = Label(text="Miles", font=("arial", 10, "bold"))
label_1.grid(row=0, column=2)
label_1.config(padx=20)


label_2 = Label(text="is equal to", font=("arial", 10, "bold"))
label_2.grid(row=1, column=0)
label_2.config(padx=20)

label_3 = Label(text='0', font=("arial", 10, "bold"))
label_3.grid(row=1, column=1)
label_3.config(padx=20, pady=20)

label_4 = Label(text="Km", font=("arial", 10, "bold"))
label_4.grid(row=1, column=2)
label_4.config(padx=20, pady=20)

# convert = calculation()

button = Button(text="Convert", command=calculation)
button.grid(row=2, column=1)

root.mainloop()
