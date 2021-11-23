from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUI:
    def __init__(self, quiz_text: QuizBrain):
        self.quiz = quiz_text
        self.window = Tk()
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.title("Quizzler")

        self.score_label = Label(text=f"Score:\t0", bg=THEME_COLOR)
        self.score_label.grid(row=1, column=2, padx=20, pady=20)

        self.canvas = Canvas(width=500, height=250, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(250,
                                                125,
                                                width=480,
                                                text="Some Question Text",
                                                fill=THEME_COLOR,
                                                font=("Arial", 15, "italic"),
                                                )

        self.canvas.grid(row=2, column=1, columnspan=3)

        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=self.true_img, highlightthickness=0, bg=THEME_COLOR, command=self.is_True)
        self.true_button.grid(row=3, column=1, padx=20, pady=20)

        self.false_button = Button(image=self.false_img, highlightthickness=0, bg=THEME_COLOR, command=self.is_False)
        self.false_button.grid(row=3, column=3, padx=20, pady=20)

        self.show_question()

        self.window.mainloop()

    def show_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score:\t{self.quiz.score}")
            self.canvas.itemconfig(self.question, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question, text="You've reached to the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def is_True(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def is_False(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.show_question)
