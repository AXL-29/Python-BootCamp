from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.after_id = None

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Grid configuration (FIX)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)

        # Score label
        self.score_label = Label(
            text="Score: 0",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 12, "normal"),
            anchor="e"
        )
        self.score_label.grid(row=0, column=1, sticky="e")

        # Canvas (FIX border)
        self.canvas = Canvas(
            width=300,
            height=250,
            bg="white",
            highlightthickness=0
        )
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 16, "italic"),
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        # Button images (FIX reference)
        self.true_btn_img = PhotoImage(file="images/true.png")
        self.false_btn_img = PhotoImage(file="images/false.png")

        # Buttons (FIX padding)
        self.true_button = Button(
            image=self.true_btn_img,
            command=self.true_pressed,
            highlightthickness=0,
            borderwidth=0
        )
        self.true_button.grid(row=2, column=0, pady=20)

        self.false_button = Button(
            image=self.false_btn_img,
            command=self.false_pressed,
            highlightthickness=0,
            borderwidth=0
        )
        self.false_button.grid(row=2, column=1, pady=20)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(
                self.question_text,
                text=self.quiz.next_question()
            )
        else:
            self.canvas.itemconfig(
                self.question_text,
                text="You've reached the end of the quiz."
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        self.canvas.config(bg="green" if is_right else "red")

        if self.after_id:
            self.window.after_cancel(self.after_id)

        self.after_id = self.window.after(1000, self.get_next_question)
