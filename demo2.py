from tkinter import *
from PIL import Image, ImageTk

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')

        img = Image.open('recipy_images/12.png')

        imgTk = ImageTk.PhotoImage(image=img)

        self.lb = Label(self.root, image=imgTk)
        self.lb.pack()

        self.root.mainloop()


obj = Main()