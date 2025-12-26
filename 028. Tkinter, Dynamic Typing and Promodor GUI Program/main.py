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
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Long Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Short Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
        count_down(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# Event-Driven - a programming style where the flow of the program is controlled by events, not by a fixed step-by-step order.
# Simple definition - event-driven programming means your program waits for something to happen(an event) and then responds with code.

# after() - is a method that lets you schedule code to run, after a certain amount of time - without freezing the GUI.

def count_down(count):
    count_min = count // 60
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

# Tkinter Canvas Widget - is a drawing area where you can draw shapes, display images
# and create simple graphics or animations inside a Tkinter window.

canvas = Canvas(width=300, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(150, 112, image=img)
timer_text = canvas.create_text(150, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"), )
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
title_label.grid(row=0, column=1)

start_button = Button(text="Start", command=start_timer, bg=YELLOW, borderwidth=0, highlightthickness=0, padx=10, pady=5)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=YELLOW, borderwidth=0, highlightthickness=0, padx=10, pady=5)
reset_button.grid(row=2, column=2)

checked_label = Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
checked_label.grid(row=3, column=1)

window.mainloop()