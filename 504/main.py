from random import choice
from tkinter import *

import pandas

# ----------------------------------- Constants ----------------------------------- #
BACKGROUND_COLOR = "#B1DDa1"
CURRENT_CARD = {}
to_learn = {}
# ----------------------------------- change Setup ----------------------------------- #

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/504.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="record")


def flip():
    canvas.itemconfig(front_image_canvas, image=back_image)
    canvas.itemconfig(language_canvas, text="Persian")
    global CURRENT_CARD
    text = CURRENT_CARD["persian"]
    canvas.itemconfig(word_canvas, text=' '.join(text.split()[::-1]))


def next_card():
    canvas.itemconfig(front_image_canvas, image=front_image)
    canvas.itemconfig(language_canvas, text="English")
    global CURRENT_CARD
    CURRENT_CARD = choice(to_learn)
    canvas.itemconfig(language_canvas, text="English")
    canvas.itemconfig(word_canvas, text=CURRENT_CARD["english"])
    window.after(3000, flip)


def right():
    to_learn.remove(CURRENT_CARD)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ----------------------------------- UI Setup ----------------------------------- #
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("504 Flash cards")

# row 1
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
front_image_canvas = canvas.create_image(400, 263, image=front_image)
language_canvas = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_canvas = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=1, column=1, columnspan=2)

# row 2
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bd=0, command=right)
right_button.grid(row=2, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bd=0, command=next_card)
wrong_button.grid(row=2, column=2)

next_card()

window.mainloop()
