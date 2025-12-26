from tkinter import *
from typing import Optional

# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer: Optional[str] = None


# TIMER RESET
def reset_timer():
    """Stop the timer and reset UI and state."""
    global reps, timer

    if timer is not  None:
        window.after_cancel(timer)
        timer = None

    reps = 0

    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checked_label.config(text="")


# TIMER MECHANISM
def start_timer():
    """Start the Pomodoro timer based on repetition count."""
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# COUNTDOWN MECHANISM
def count_down(count):
    """Update the countdown timer every second."""
    global timer

    minutes = count // 60
    seconds = count % 60

    canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        update_checkmarks()


def update_checkmarks():
    """Update checkmarks after each completed work session."""
    marks = "✓" * (reps // 2)
    checked_label.config(text=marks)


# UI SETUP
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas (tomato image + timer text)
canvas = Canvas(width=300, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(150, 112, image=tomato_img)
timer_text = canvas.create_text(
    150, 130,
    text="00:00",
    fill="white",
    font=(FONT_NAME, 30, "bold")
)
canvas.grid(row=1, column=1)

# Title label
title_label = Label(
    text="Timer",
    fg=GREEN,
    bg=YELLOW,
    font=(FONT_NAME, 30, "bold")
)
title_label.grid(row=0, column=1)

# Buttons
start_button = Button(
    text="Start",
    command=start_timer,
    bg=YELLOW,
    borderwidth=0,
    padx=10,
    pady=5,
    font=(FONT_NAME, 20, "bold")
)
start_button.grid(row=2, column=0)

reset_button = Button(
    text="Reset",
    command=reset_timer,
    bg=YELLOW,
    borderwidth=0,
    padx=10,
    pady=5,
    font = (FONT_NAME, 20, "bold")

)
reset_button.grid(row=2, column=2)

# Checkmarks
checked_label = Label(
    fg=GREEN,
    bg=YELLOW,
    font=(FONT_NAME, 15, "bold")
)
checked_label.grid(row=3, column=1)

window.mainloop()
