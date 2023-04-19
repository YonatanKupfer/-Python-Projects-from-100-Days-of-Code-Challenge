from tkinter import *
from quiz_brain import QuizBrain

# constants
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    
    # initialize the quiz interface
    def __init__(self, quiz_bank: QuizBrain):
        self.quiz = quiz_bank
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150,
                                                125,
                                                width=280,
                                                text="Some question",
                                                fill=THEME_COLOR,
                                                font=FONT
                                                )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Score label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        correct_image = PhotoImage(file="images/true.png")
        wrong_image = PhotoImage(file="images/false.png")

        # Buttons
        self.true_b = Button(image=correct_image, bg=THEME_COLOR, highlightthickness=0, command=self.guess_true)
        self.true_b.grid(column=0, row=2)
        self.false_b = Button(image=wrong_image, bg=THEME_COLOR, highlightthickness=0, command=self.guess_false)
        self.false_b.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()
    
    # get the next question
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz.")
            self.true_b.config(state="disabled")
            self.false_b.config(state="disabled")
    
    # check if the user's answer is correct
    def guess_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def guess_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)
    
    # give feedback to the user
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)


