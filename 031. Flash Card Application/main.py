from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# UI Setup:
windows = Tk()

windows.title("Flash Card Application")
windows.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
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
        image=wrong_button,
        highlightthickness=0,
        borderwidth=0
        ).grid(row=1, column=0, padx=50, pady=50)

right = Button(
        image=right_button,
        highlightthickness=0,
        borderwidth=0
        ).grid(row=1, column=1, padx=50, pady=50)

windows.mainloop()