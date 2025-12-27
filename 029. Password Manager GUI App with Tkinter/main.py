from tkinter import *
from tkinter import messagebox

# PASSWORD GENERATOR

# SAVE PASSWORD
def save_data():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()

    # Dialog Box - is a small window that communicates with the user and usually requires and action (OK, Cancel, Yes/No)
    if website == "" or password == "":
        # The program waits until the user clicks a button -> this is called modal.
        messagebox.showwarning(
            title="Oops",
            message="Please don't leave any fields empty."
        )

    else:
        is_ok = messagebox.askokcancel(
                title= website,
                message = f"""These are the details entered:

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

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# columnspan - is an option used with the grid() geometry manager to tell a 
# widget to stretch across multiple columns instead of staying just one.

# Labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0, sticky="e")

username_label = Label(text="Email/Username: ")
username_label.grid(row=2, column=0, sticky="e")

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0, sticky="e")

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
gen_pass_btn = Button(text="Generator Password", padx=0, pady=0)
gen_pass_btn.grid(row=3, column=2, sticky="e")

add_btn = Button(text="Add", command=save_data, width=34, padx=0, pady=0)
add_btn.grid(row=4, column=1, columnspan=2, sticky="e")

window.mainloop()