from tkinter import Button


class Botones(Button):
    def __init__(self, img, cols, rows, hks):
        super().__init__()
        self.config(image=img, highlightthickness=hks)
        self.grid(column=cols, row=rows)