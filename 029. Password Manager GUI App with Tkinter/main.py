from tkinter import *
from tkinter import messagebox
import random
import pyperclip

#CONSTANT DATA

# Characters used for password generation
LETTERS = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

SYMBOLS = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_",
    "=", "+", "[", "]", "{", "}", ";", ":", "'", '"', ",", ".",
    "<", ">", "/", "?", "|", "\\", "~", "`"
]

# PASSWORD GENERATOR

def password_generator():
    """Generate a random password and display it in the password entry field."""
    password_entry.delete(0, END)

    password_letters = [random.choice(LETTERS) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(SYMBOLS) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(NUMBERS) for _ in range(random.randint(2, 4))]

    # Combine and shuffle all characters
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    # Convert list into string
    generated_password = "".join(password_list)

    password_entry.insert(0, generated_password)

    # Copy the password.
    pyperclip.copy(generated_password)

# SAVE PASSWORD

def save_data():
    """Validate input, confirm details, and save password data to file."""
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()

    # Validate required fields
    if website == "" or password == "":
        messagebox.showwarning(
            title="Oops",
            message="Please don't leave any fields empty."
        )
        return

    # Confirm details before saving
    is_ok = messagebox.askokcancel(
        title=website,
        message=f"""These are the details entered:

Email: {email}
Password: {password}

Is it okay to save?
"""
    )

    if is_ok:
        with open("data.txt", "a") as data:
            data.write(f"{website} | {email} | {password}\n")

        website_entry.delete(0, END)
        password_entry.delete(0, END)

# UI SETUP

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
Label(text="Website:").grid(row=1, column=0, sticky="e")
Label(text="Email/Username:").grid(row=2, column=0, sticky="e")
Label(text="Password:").grid(row=3, column=0, sticky="e")

# Entries
website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="e")

username_entry = Entry(width=40)
username_entry.insert(0, "gimpaojade4@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2, sticky="e")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="e")

# Buttons
Button(
    text="Generate Password",
    command=password_generator
).grid(row=3, column=2, sticky="e")

Button(
    text="Add",
    width=34,
    command=save_data
).grid(row=4, column=1, columnspan=2, sticky="e")

window.mainloop()
