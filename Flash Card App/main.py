from tkinter import *
import random
import pandas

# --------- CONSTANT -----------------------

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# --------- FUNCTION -----------------------

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/korean_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)   # keeps only one timer active at any moment

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Korean", fill="black")
    canvas.itemconfig(card_word, text=current_card["Korean"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data_to_learn = pandas.DataFrame(to_learn)
    data_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# --------- UI SETUP -----------------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Button
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)


next_card()

window.mainloop()