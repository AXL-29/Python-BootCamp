from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = pandas.read_csv("./data/french_words.csv").to_dict(orient="records")

current_card = {}
flip_timer = None


def next_card():
    global current_card, flip_timer

    # 1️⃣ Cancel existing timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)

    # 2️⃣ Pick a new card
    current_card = random.choice(to_learn)

    # 3️⃣ Reset card to FRONT
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=current_card["French"])

    # 4️⃣ Start new flip timer
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=current_card["English"])

# UI Setup:
window = Tk()
window.title("Flash Card Application")
window.config(bg=BACKGROUND_COLOR, 
              padx=50, pady=50)

front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
wrong_button = PhotoImage(file="./images/wrong.png")
right_button = PhotoImage(file="./images/right.png")

canvas = Canvas(width=800, 
                height=526, 
                highlightthickness=0, 
                bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=front_img)

title_text = canvas.create_text(400, 150, 
                              font=("Arial", 40, "italic"),
                              text="Title",
                              fill="black")

word_text = canvas.create_text(400, 263, 
                              font=("Arial", 60, "bold"),
                              text="Word",
                              fill="black")
canvas.grid(row=0, column=0, columnspan=2)

wrong = Button(
        command=next_card,
        image=wrong_button,
        highlightthickness=0,
        borderwidth=0,
        takefocus=False,
        activebackground=BACKGROUND_COLOR
        ).grid(row=1, column=0, padx=50)

right = Button(
        command=next_card,
        image=right_button,
        highlightthickness=0,
        borderwidth=0,
        takefocus=False,
        activebackground=BACKGROUND_COLOR
        ).grid(row=1, column=1, padx=50)

next_card()
window.mainloop()