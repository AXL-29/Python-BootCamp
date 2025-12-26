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



from tkinter import *

def button_clicked():
    new_text  = my_input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.place(x=0, y=0)

# Button
button = Button(text="Click Me", command=button_clicked)
my_label.place(x=0, y=0)

# Entry
my_input = Entry()
my_label.place(x=0, y=0)


window.mainloop()
