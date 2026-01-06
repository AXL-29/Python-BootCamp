from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.score}",
                                 fg="white",
                                 bg=THEME_COLOR,
                                 highlightthickness=0,
                                 font=("Arial", 12, "normal")
                                 )

        self.score_label.grid(row=0, column=1)

        self.canvas  = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 16, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        true_btn_img = PhotoImage(file="images/true.png")
        false_btn_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_btn_img, highlightthickness=0, borderwidth=0)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_btn_img, highlightthickness=0, borderwidth=0)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()