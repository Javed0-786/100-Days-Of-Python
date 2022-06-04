from tkinter import *
from tkinter import messagebox
import pyperclip
import string
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatePassword():
    alphabet_string = string.ascii_letters
    alphabet_list = list(alphabet_string)

    alphabet_list = alphabet_list + \
        [str(num) for num in list(range(0, 10))] + \
        ["!", "@", "#", "%", "&", "*", "_", "/", "-", "+"]

    pswd = ""
    for i in range(0, 12):
        j = random.randint(0, 70)
        pswd = pswd + alphabet_list[j]
    entry3.insert(END, string=pswd)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def addPassword():
    website = entry1.get()
    email = entry2.get()
    password = entry3.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error Occured",
                            message="Fields can't be empty")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")

            entry1.delete(0, len(website))
            entry3.delete(0, len(password))
            pyperclip.copy(password)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
# window.minsize(width=140, height=140)
window.config(padx=50, pady=50)
image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)


label_1 = Label(text="Website:")
label_1.grid(row=1, column=0)

entry1 = Entry(width=35)
entry1.grid(row=1, column=1, columnspan=2)

label_2 = Label(text="Email/Username:")
label_2.grid(row=2, column=0)

entry2 = Entry(width=35, )
entry2.grid(row=2, column=1, columnspan=2)
entry2.insert(index=0, string="javedalam@gmail.com")


label_3 = Label(text="Password:")
label_3.grid(row=3, column=0)

entry3 = Entry(width=17)
entry3.grid(row=3, column=1)


button_1 = Button(text="Generate Password", command=generatePassword)
button_1.grid(row=3, column=2)

button_2 = Button(text="Add", width=36, command=addPassword)
button_2.grid(row=4, column=1, columnspan=2)

window.mainloop()
