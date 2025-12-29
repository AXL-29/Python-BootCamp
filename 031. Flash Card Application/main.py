from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

def flash_card():
    data = pandas.read_csv("./data/french_words.csv")
    word_dict = {row.French:row.English for (index, row) in data.iterrows()}

    french_word, english_word = random.choice(list(word_dict.items()))

    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=french_word)

# UI Setup:
window = Tk()

window.title("Flash Card Application")
window.config(bg=BACKGROUND_COLOR, 
              padx=50, pady=50)

canvas = Canvas(width=800, 
                height=526, 
                highlightthickness=0, 
                bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=front_img)

title_text = canvas.create_text(400, 150, 
                              font=("Arial", 40, "italic"),
                              text="Title",
                              fill="black")

word_text = canvas.create_text(400, 263, 
                              font=("Arial", 60, "bold"),
                              text="Word",
                              fill="black")
canvas.grid(row=0, column=0, columnspan=2)

wrong_button = PhotoImage(file="./images/wrong.png")
right_button = PhotoImage(file="./images/right.png")

wrong = Button(
        command=flash_card,
        image=wrong_button,
        highlightthickness=0,
        borderwidth=0,
        takefocus=False,
        activebackground=BACKGROUND_COLOR
        ).grid(row=1, column=0, padx=50)

right = Button(
        command=flash_card,
        image=right_button,
        highlightthickness=0,
        borderwidth=0,
        takefocus=False,
        activebackground=BACKGROUND_COLOR
        ).grid(row=1, column=1, padx=50)



window.mainloop()