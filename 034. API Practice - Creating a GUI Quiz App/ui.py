from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.score = 0
        self.window = Tk()
        self.canvas = Canvas()
        self.window.title("Quizzler!")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.score}", 
                                 fg="white", 
                                 bg=THEME_COLOR, 
                                 highlightthickness=0).grid(
                                    row=0,
                                    column=1)
        
        self.canvas.create_rectangle(width=300)
        self.window.mainloop()