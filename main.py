from tkinter import *
from class_buttons import Botones
import pandas
import random

data = pandas.read_csv(r"data\data_words.csv")

def word_random():
    word_english = random.choice(data["English"])
    word_spanish = data[data.English == word_english]
    
    canvas_bg.delete("word")
    canvas_bg.create_text(400,263, text=word_english, font=FONT_UP, tags="word")

#Constantes Fuentes y Background
BG_COLOR = "#B1DDC6"
FONT_LOW = ("Ariel", 40, "italic")
FONT_UP = ("Ariel", 60, "bold")

#Creacion del root
root = Tk()
root.title("Learning English whit (FlashCards)")
root.config(padx=50, pady=50, bg= BG_COLOR)

#Imagenes de los botones
right_img = PhotoImage(file=r"images\right.png")
wrong_img = PhotoImage(file=r"images\wrong.png")

#Imagenes de BGROUND
img_back = PhotoImage(file=r"images\card_back.png")
img_front = PhotoImage(file=r"images\card_front.png")

#Creacion del canvas, textos, images and configurations
canvas_bg = Canvas(width=800, height=526, highlightthickness=0, bg=BG_COLOR)
canvas_img_front = canvas_bg.create_image(400,263, image=img_front)
#canvas_img_back = canvas_bg.create_image(400,263, image=img_back)
language = canvas_bg.create_text(400,150, text="English", font=FONT_LOW)
canvas_bg.grid(column=0, row=0, columnspan=2)


#Botones Creados desde la class_buttons
wrong_button = Botones(wrong_img, 0,1,0, word_random)
right_button = Botones(right_img, 1,1,0, word_random)



root.mainloop()



