from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.quiz = quiz
        self.score = Label(text=f"Score: {self.quiz.score}", font=(
            "arial", 15, "normal"), bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(
            150, 125, text="Some Question Text", font=("arial", 20, "italic"), fill=THEME_COLOR, width=300)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.true = Button(
            image=true_image, highlightthickness=0, command=self.return_true)
        self.true.grid(row=2, column=0, padx=20, pady=20, )
        self.false = Button(image=false_image,
                            highlightthickness=0, command=self.return_false)
        self.false.grid(row=2, column=1, padx=20, pady=20, )
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(
                self.question, text="You have attempted all the questions.\nThankyou")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def return_true(self):
        is_right = self.quiz.check_answer("True")
        self.delay(is_right)

    def return_false(self):
        is_wrong = self.quiz.check_answer("False")
        self.delay(is_wrong)

    def delay(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
