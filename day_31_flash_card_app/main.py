
from tkinter import *
import pandas
from random import choice

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
# ---------------------------- DATA ------------------------------- #
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    full_data = pandas.read_csv("data/spanish_to_english.csv")
    to_learn = full_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# ---------------------------- PICK A WORD ------------------------------- #

def next_word():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(language_l, text="Spanish", fill="black")
    canvas.itemconfig(word_l, text=current_card["Spanish"], fill="black")

    flip_timer = window.after(3000, flip)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_word()

def flip():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(language_l, text="English", fill="white")
    canvas.itemconfig(word_l, text=current_card["English"], fill="white")



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)


# On Card
language_l = canvas.create_text(400, 150, text="", font=LANG_FONT)
word_l = canvas.create_text(400, 263, text="", font=WORD_FONT)

# Buttons
correct_image = PhotoImage(file="images/right.png",)
wrong_image = PhotoImage(file="images/wrong.png")

correct_b = Button(image=correct_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
correct_b.grid(column=1, row=1)

wrong_b = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_word)
wrong_b.grid(column=0, row=1)

next_word()

window.mainloop()
