from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

# Tkinter Canvas Widget - is a drawing area where you can draw shapes, display images
# and create simple graphics or animations inside a Tkinter window.

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"), )
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title_label.grid(row=0, column=1)

start_button = Button(text="Start", bg=YELLOW, borderwidth=0, highlightthickness=0, padx=10, pady=5)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=YELLOW, borderwidth=0, highlightthickness=0, padx=10, pady=5)
reset_button.grid(row=2, column=2)

checked_label = Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
checked_label.grid(row=3, column=1)

window.mainloop()