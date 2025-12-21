import turtle

# Set up screen and turtle
screen = turtle.Screen()

# Add the shape
img = "blank_states_img.gif"  # Use correct relative or absolute path
screen.addshape(img)
turtle.shape(img)

# Wait for a click to close the window
turtle.mainloop()