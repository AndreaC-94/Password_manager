from tkinter import *
from tkinter import messagebox
from passowrdData import *
import random as rd
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def check_pass_symbols(password):
    if password[0] in ['.', '-']:  # password[0] != "." and password[0] != "-":
        return True
    return False


def generate():
    password_entry.delete(0, END)
    password = []
    password.extend([rd.choice(LETTERS[:25]) for _ in range(rd.randint(4, 5))])
    password.extend([rd.choice(LETTERS[25:]) for _ in range(rd.randint(4, 5))])
    password.extend([rd.choice(NUMBERS) for _ in range(rd.randint(2, 4))])
    password.extend([rd.choice(SYMBOLS) for _ in range(rd.randint(2, 4))])

    checking = True
    while checking:
        rd.shuffle(password)
        checking = check_pass_symbols(password)

    password = "".join(password)
    pyperclip.copy(password)
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Please don't leave any empty field!")
        if len(website) == 0:
            website_entry.focus()
        elif len(username) == 0:
            username_entry.focus()
        else:
            password_entry.focus()

    elif check_pass_symbols(password):
        messagebox.showinfo(title="Password Error", message="Your password cannot begin with \".\" or \"-\"\n"
                                                            "Pick a different password please")
        password_entry.delete(0, END)
        password_entry.focus()
    elif len(password) < 8:
        messagebox.showinfo(title="Password too short", message="Your password must have a length of at least 8\n\n"
                                                                "Please pick a different password")
        password_entry.focus()
    else:
        ok_to_save = messagebox.askyesno(title="Data check",
                                         message=f"There are the details entered:\n\nWebsite: {website}\nUsername: "
                                                 f"{username}\nPassword: \"{password}\"\nIs it ok to save?")

        if ok_to_save:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {username} | {password}\n")  # Separator -> " | "
                website_entry.delete(0, END)
                # username_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()
                pyperclip.copy(password)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
# window.geometry("200x200")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
website_label.grid(row=1, column=0)
username_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=51)
username_entry = Entry(width=51)
password_entry = Entry(width=32)
website_entry.grid(row=1, column=1, columnspan=2)
username_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)
website_entry.focus()
username_entry.insert(0, "andreacolucci1994@gmail.com")

# Buttons
password_button = Button(text="Generate Password", width=14, command=generate)
add_button = Button(text="Add", width=43, command=save)
password_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
