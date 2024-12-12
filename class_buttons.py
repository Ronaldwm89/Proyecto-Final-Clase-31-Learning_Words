from tkinter import Button


class Botones(Button):
    def __init__(self, img, cols, rows, hks, name):
        super().__init__()
        self.config(image=img, highlightthickness=hks, command=name)
        self.grid(column=cols, row=rows)
