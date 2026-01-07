"""
Flash Card Application

Displays French words as flashcards, automatically flips to English after a delay,
and permanently removes learned words so progress persists across app restarts.
"""

from tkinter import *
import pandas
import random

# CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"
FLIP_DELAY_MS = 3000

# DATA LOADING

# Load ONLY remaining words; create progress file on first run
try:
    to_learn = pandas.read_csv("./data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    original_data.to_csv("./data/words_to_learn.csv", index=False)
    to_learn = original_data.to_dict(orient="records")

current_card = {}
flip_timer = None

# FUNCTIONS
def next_card():
    """Selects a new French word, resets the card to front, and starts the flip timer."""
    global current_card, flip_timer

    # Cancel existing flip timer
    if flip_timer:
        window.after_cancel(flip_timer)

    # All words learned
    if not to_learn:
        canvas.itemconfig(canvas_image, image=front_img)
        canvas.itemconfig(title_text, text="🎉 Done!", fill="black")
        canvas.itemconfig(word_text, text="All words learned", fill="black")
        return

    # Pick a random remaining card
    current_card = random.choice(to_learn)

    # Show front of the card
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")

    # Schedule automatic flip
    flip_timer = window.after(FLIP_DELAY_MS, flip_card)


def flip_card():
    """Flips the card to show the English translation."""
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


def is_known():
    """Removes the current card from learning list and saves progress permanently."""
    if current_card in to_learn:
        to_learn.remove(current_card)

    # Save updated learning list
    pandas.DataFrame(to_learn).to_csv(
        "./data/words_to_learn.csv",
        index=False
    )

    next_card()

# UI SETUP
window = Tk()
window.title("Flash Card Application")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Load images (keep references)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
wrong_button = PhotoImage(file="./images/wrong.png")
right_button = PhotoImage(file="./images/right.png")

# Canvas
canvas = Canvas(
    width=800,
    height=526,
    highlightthickness=0,
    bg=BACKGROUND_COLOR
)
canvas_image = canvas.create_image(400, 263, image=front_img)

title_text = canvas.create_text(
    400, 150,
    font=("Arial", 40, "italic"),
    fill="black"
)

word_text = canvas.create_text(
    400, 263,
    font=("Arial", 60, "bold"),
    fill="black"
)

canvas.grid(row=0, column=0, columnspan=2)

# Buttons
Button(
    image=wrong_button,
    command=next_card,
    highlightthickness=0,
    borderwidth=0,
    takefocus=False,
    activebackground=BACKGROUND_COLOR
).grid(row=1, column=0, padx=50)

Button(
    image=right_button,
    command=is_known,
    highlightthickness=0,
    borderwidth=0,
    takefocus=False,
    activebackground=BACKGROUND_COLOR
).grid(row=1, column=1, padx=50)

# START APP
next_card()
window.mainloop()
