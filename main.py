from tkinter import *
from class_buttons import Botones
import pandas
import random

random_word = {}

try:
    data = pandas.read_csv(r"data\words_to_learn.csv")
    
except FileNotFoundError:
    data = pandas.read_csv(r"data\data_words.csv")
    
finally:
    df_dict = data.to_dict(orient="records")
    

def word_random():
    global random_word
    random_word = random.choice(df_dict)
    english_word = random_word["English"].title() 
    spanish_word = random_word["Español"].title()

    canvas_bg.itemconfig(canvas_img_front, image=img_front)
    canvas_bg.itemconfig(language, text="English", fill="black")
    canvas_bg.itemconfig(words, text=english_word, fill="black")
    
    def change_card():
        
        canvas_bg.itemconfig(canvas_img_front, image=img_back)
        canvas_bg.itemconfig(language, text="Español", fill="white")
        canvas_bg.itemconfig(words, text=spanish_word, fill="white")
    
        root.after_cancel(pausa)
    
    pausa = root.after(3000, change_card)

def word_learn():
    
    df_dict.remove(random_word)#Elimina la palabra aprendida
    df_update = pandas.DataFrame(df_dict)#crea un dataframe desde el diccionario actualizado
    df_update.to_csv(r"data\words_to_learn.csv", index=False)#crea el archivo csv y elimina la columna del index
    
    word_random()
       


    #df_dict.remove()

    #with open(r"words_to_learn.csv", "w") as data_learning:
        #words_learned = data_learning.write()
    



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
img_front = PhotoImage(file=r"images\card_front.png")
img_back = PhotoImage(file=r"images\card_back.png")

#Creacion del canvas, textos, images and configurations
canvas_bg = Canvas(width=800, height=526, highlightthickness=0, bg=BG_COLOR)
canvas_img_front = canvas_bg.create_image(400,263, image=img_front)
language = canvas_bg.create_text(400,150, text="", font=FONT_LOW)
words = canvas_bg.create_text(400,263, text="", font=FONT_UP)
canvas_bg.grid(column=0, row=0, columnspan=2)


#Botones Creados desde la class_buttons
wrong_button = Botones(wrong_img, 0,1,0, word_random)
right_button = Botones(right_img, 1,1,0, word_learn)

word_random()

root.mainloop()



'''
try:
            with open(r"passwords.json", "r") as data:
         
                #leyendo los archivos viejos
                data_new = json.load(data)
         
               
        except (FileNotFoundError, json.JSONDecodeError): 
             data_new = {}
        
        #actualizando los datos vacios con nuevos
        data_new.update(new_data)
        
        with open(r"passwords.json", "w") as data:
            #agregando la nueva info a la vieja funciona como un write
            json.dump(data_new, data, indent=4)
'''