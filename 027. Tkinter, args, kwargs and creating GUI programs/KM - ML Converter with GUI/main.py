# Layout Manager:
    # 1. Pack Layout Manager - is the simplest and most beginner-friendly way to place widgets in Tkinter
        # It automatically arranges widget relative to each other, instead of using coordinates.
        # How pack Works:
            # When you use pack(), Tkinter decides where to place the widgets based on:
                # Which side of the window it belongs to
                # The order you pack widgets

    # 2. Place Layout Manager - position widgets by specifying exact coordinates or relative positions within a container.
        # How place Works
        # Absolute positioning
            # x, y -> exact pixel coordinates

        # Relative positioning
            # relx, rely -> relative position (0.0 to 1.0)
            # relwidth, relheight -> relative size

    # 3. Grid Layout Manager - the grid layout manager places widgets in a table-like structure using rows and columns
        # similar to an Excel sheet or HTML table.

        # How grid Works
        # You tell Tkinter:
            # which row
            # which column
        # Tkinter then places the widget in that cell.

# Adding Padding - padding is the extra space around the widgets so your GUI doesn't look cramped.
# Padding with pack() & grid()
    # padx and pady
    # padx - horizontal space (left & right)
    # pady - vertical space (top & bottom)


from tkinter import *

def button_clicked():
    new_text  = my_input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(row=1, column=1)

# Button
button1 = Button(text="Click Me", command=button_clicked)
button1.grid(row=2, column=2)

# Button
button2 = Button(text="Click Me", command=button_clicked)
button2.grid(row=1, column=3)

# Entry
my_input = Entry()
my_input.grid(row=3, column=4)

window.mainloop()
