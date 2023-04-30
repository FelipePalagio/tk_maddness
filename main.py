from tkinter import *
from threading import *

jan = Tk()
jan.geometry("500x400")
jan.config(background="white")
jan.title("Git_fucked")


def hex_to_rgb(hex):
    rgb = []
    for i in (0, 2, 4):
        decimal = int(hex[i:i + 2], 16)
        rgb.append(decimal)

    return tuple(rgb)


def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


print(rgb_to_hex(100, 0, 0))


def backstreet_blues():
    r = 0
    g = 0
    b = 0
    while True:
        r += 1
        #g += 1
        #b += 1
        col= rgb_to_hex(r, g, b)
        print(col)
        jan.config(background=col)
        time.sleep(0.1)


threader = Thread(target=backstreet_blues, daemon=True)
threader.start()

jan.mainloop()
