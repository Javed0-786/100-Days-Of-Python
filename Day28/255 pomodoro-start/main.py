from tkinter import *
from tkinter import messagebox
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
check_mark = ""
delay = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global check_mark
    global reps
    check_mark = ""
    reps = 1
    window.after_cancel(delay)
    label_2.config(text=check_mark)
    label_1.config(text="Timer")
    canvas.itemconfig(timer_text, text=f"25:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    global check_mark

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 1 and reps < 8:
        label_1.config(text="Work", fg=GREEN)
        countdown(work_sec)

    elif reps % 2 == 0 and reps < 8:
        label_1.config(text="Break", fg=PINK)
        countdown(short_break_sec)

    elif reps == 8:
        label_1.config(text="Break", fg=RED)
        countdown(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(total_sec):
    count = math.floor(total_sec / 60)
    sec = total_sec % 60
    global check_mark
    global reps
    global delay
    if count < 10 or sec < 10:
        if count < 10 and sec > 9:
            canvas.itemconfig(timer_text, text=f"0{count}:{sec}")

        elif count > 9 and sec < 10:
            canvas.itemconfig(timer_text, text=f"{count}:0{sec}")

        else:
            canvas.itemconfig(timer_text, text=f"0{count}:0{sec}")

    else:
        canvas.itemconfig(timer_text, text=f"{count}:{sec}")

    if sec == 0:
        sec = 60
        count -= 1

    if count >= 0:
        delay = window.after(1000, countdown, total_sec - 1)
    else:
        reps += 1
        start_timer()
        if reps % 2 == 0:
            check_mark += "🗸"
            label_2.config(text=check_mark)
            messagebox.showinfo("Reminder", "Please Take Break")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=30, pady=30, bg=YELLOW)
label_1 = Label(text="Timer", font=(
    FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
label_1.grid(row=0, column=1)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text=f"00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


button_1 = Button(text="Start", command=start_timer, width=10)
button_1.grid(row=2, column=0)

button_2 = Button(text="Reset", command=reset_timer, width=10)
button_2.grid(row=2, column=2)

label_2 = Label(font=(
    FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
label_2.grid(row=3, column=1)


window.mainloop()
