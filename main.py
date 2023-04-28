from tkinter import *
from threading import *
jan = Tk()
jan.geometry("500x400")
jan.config(background="yellow")
jan.title("Git_fucked")
colourids = ["black","white","red","green"]

def backstreet_blues():
    while True:
        for i in colourids:
            jan.config(background=i)



threader = Thread(target=backstreet_blues,daemon=True)
threader.start()

jan.mainloop()
