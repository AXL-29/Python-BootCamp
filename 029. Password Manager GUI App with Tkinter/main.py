from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# columnspan - is an option used with the grid() geometry manager to tell a 
# widget to stretch across multiple columns instead of staying just one.

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0, sticky="e")

website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2, sticky="e")


username_label = Label(text="Email/Username: ")
username_label.grid(row=2, column=0, sticky="e")

username_entry = Entry(width=40)
username_entry.grid(row=2, column=1, columnspan=2, sticky="e")

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0, sticky="e")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="e")

gen_pass_btn = Button(text="Generator Password", padx=0, pady=0)
gen_pass_btn.grid(row=3, column=2, sticky="e")

add_btn = Button(text="Add", width=34, padx=0, pady=0)
add_btn.grid(row=4, column=1, columnspan=2, sticky="e")

window.mainloop()