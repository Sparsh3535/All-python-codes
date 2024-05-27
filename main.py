from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
french_word_2 = ""
def change_to_french():
    global french_word_2
    canvas.itemconfig(image, image=front_card_image)
    canvas.itemconfig(french, text="French", fill="black")
    french_word_2 = random.choice(words["French"])
    canvas.itemconfig(french_word, text=french_word_2, fill="black")
    window.after(3000, func=flip_card)
def word_to_remove():
    row_to_remove = words[words.French == french_word_2].index
    words.drop(row_to_remove, inplace=True)
    change_to_french()
def flip_card():
    canvas.itemconfig(image, image=back_card_image)
    canvas.itemconfig(french, text="English", fill="white")
    french_word_row = words[words.French == french_word_2]
    english_word = french_word_row.English.values[0]
    canvas.itemconfig(french_word, text=english_word, fill="white")
    window.after(3000, func=change_to_french)

window = Tk()
window.title("Flash Card Project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, highlightthickness=0)
front_card_image = PhotoImage(file="../flash-card-project-start/images/card_front.png")
back_card_image = PhotoImage(file="../flash-card-project-start/images/card_back.png")
image = canvas.create_image(410, 263, image=front_card_image)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR)

right_image = PhotoImage(file="../flash-card-project-start/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=word_to_remove)
right_button.grid(row=1, column=0)
wrong_image = PhotoImage(file="../flash-card-project-start/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=word_to_remove)
wrong_button.grid(row=1, column=1)

words = pandas.read_csv("data/french_words.csv")
french_list = words["French"].to_list()
english_list = words["English"].to_list()

french = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
french_word = canvas.create_text(400, 263, text=random.choice(french_list), font=("Ariel", 60, "bold"))

change_to_french()

window.mainloop()
