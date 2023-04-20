from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    let_list = [choice(letters) for _ in range(randint(8, 10))]
    sym_list = [choice(symbols) for _ in range(randint(2, 4))]
    num_list = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = let_list + sym_list + num_list

    shuffle(password_list)

    password = "".join(password_list)
    password_e.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_e.get()
    username = username_e.get()
    password = password_e.get()

    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Don't leave any field empty.")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)

        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
        finally:
            website_e.delete(0, END)
            password_e.delete(0, END)


# ----------------------------- SEARCH ----------------------------------#
def find_password():
    website = website_e.get()
    if len(website) == 0:
        messagebox.showerror(title="Error", message="Don't leave this section empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror(title="No file error", message="No Data File Found")
        else:
            try:
                user = data[website]["username"]
                password = data[website]["password"]
            except KeyError:
                messagebox.showerror(title="No website error", message="No details for the website exists")
            else:
                messagebox.showinfo(title=website, message=f"Username: {user}\n Password: {password}")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
# window.minsize(height=200, width=200)
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=190)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=lock)
canvas.grid(column=1, row=0)

# Labels
website_l = Label(text="Website:")
website_l.grid(column=0, row=1)
username_l = Label(text="Email/Username:")
username_l.grid(column=0, row=2)
password_l = Label(text="Password:")
password_l.grid(column=0, row=3)

# Entries
website_e = Entry()
website_e.grid(column=1, row=1, columnspan=2, sticky="EW")
website_e.focus()
username_e = Entry()
username_e.grid(column=1, row=2, columnspan=2, sticky="EW")
username_e.insert(END, "yonatank50@gmail.com")
password_e = Entry()
password_e.grid(column=1, row=3, sticky="EW")

# Buttons
generate_b = Button(text="Generate Password", command=generate_password)
generate_b.grid(column=2, row=3, sticky="EW")
add_b = Button(text="Add", width=36, command=save)
add_b.grid(column=1, row=4, columnspan=2, sticky="EW")
search_b = Button(text="Search", width=13, command=find_password)
search_b.grid(column=2, row=1, sticky="EW")

window.mainloop()
