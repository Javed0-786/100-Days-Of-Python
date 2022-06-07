from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/french_words.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words_permanent.csv")
finally:
    dictionary = data.to_dict(orient="records")

current_card = {}
learnt = []
to_learn = []


# print(data.iterrows())
# dictionary = {dic[0]: dic[1] for (row, dic) in data.iterrows()}
# print(dictionary)


def refresh():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(background, image=front_image)
    current_card = random.choice(dictionary)
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=current_card["French"])
    flip_timer = window.after(3000, flip)


def flip():
    canvas.itemconfig(background, image=back_image)
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=current_card["English"])


def wrong_answer():
    refresh()


def right_answer():
    refresh()
    dictionary.remove(current_card)
    pandas.DataFrame(dictionary).to_csv("data/french_words.csv", index=False)


window = Tk()
window.title("Flash Card App")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip)

canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
background = canvas.create_image(400, 267, image=front_image)
title = canvas.create_text(400, 120, text="Title",
                           font=("arial", 40, "italic"))
word = canvas.create_text(400, 250, text="Wrong", font=(
    "arial", 60, "bold"), fill="red")
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, command=wrong_answer)
wrong.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right = Button(image=right_image, highlightthickness=0, command=right_answer)
right.grid(row=1, column=1)

refresh()
window.mainloop()
