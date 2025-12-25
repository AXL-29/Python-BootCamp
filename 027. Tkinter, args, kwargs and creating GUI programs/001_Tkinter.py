# Tkinter is a built-in GUI (Graphical User Interface) library.
#   - It lets you create windows, buttons, text boxes, labels, forms and more
#   - So users can click instead of typing in the terminal.

# Common Tkinter Components(Widgets)
# Widget	Purpose
# Tk()	    Creates the main window
# Label	    Displays text
# Button	Clickable button
# Entry	    Input box
# Text	    Multi-line text
# Canvas	Draw shapes/images

from tkinter import *

window = Tk()
window.title("My GUI Program")
window.minsize(width=400, height=400)

# Label
label = Label(text="I am a Label", font=("Courier", 24, "bold"))
label.pack()

# Button
def button_clicked():
    # label["text"] = "I got clicked"     # Either one of this can use to edit text in label
    label.config(text=user_entry.get())

button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
user_entry = Entry(width=10)
user_entry.pack()


window.mainloop()

