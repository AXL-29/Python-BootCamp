"""A simple Tkinter GUI that converts miles to kilometers using user input."""

from tkinter import *

FONT = ("Courier", 14, "normal")
MILES_TO_KM = 1.609


def calculate_kilometers():
    """Converts miles entered by the user into kilometers and updates the result label."""
    miles = float(miles_entry.get())
    kilometers = miles * MILES_TO_KM
    result_label.config(text=f"{kilometers:.2f}")


# Window setup
window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

# Widgets
miles_entry = Entry()
miles_entry.insert(0, "0")

miles_label = Label(text="Miles", font=FONT)
equals_label = Label(text="is equal to:", font=FONT)
result_label = Label(text="0", font=FONT)
km_label = Label(text="Km", font=FONT)

calculate_button = Button(text="Calculate", command=calculate_kilometers)

# Layout
miles_entry.grid(row=0, column=1)
miles_label.grid(row=0, column=2)

equals_label.grid(row=1, column=0)
result_label.grid(row=1, column=1)
km_label.grid(row=1, column=2)

calculate_button.grid(row=2, column=1)

window.mainloop()
