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

import tkinter

window = tkinter.Tk()
window.title("My GUI Program")
window.minsize(width=400, height=400)

# Label
label = tkinter.Label(text="I am a Label", font=("Courier", 24, "bold"))
label.pack(side="bottom")


window.mainloop()

