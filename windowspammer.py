import tkinter as tk
import random
import pygame

def windowopener(x, y):
    root = tk.Tk()

    pygame.mixer.init()
    pygame.mixer.music.load('htmlpages/sounds/wrong.mp3')
    pygame.mixer.music.play()

    label1 = tk.Label(root, text="loser")
    label1.pack()
    root.title('Tkinter Window Demo')
    root.geometry(f'300x200+{x}+{y}')
    root.resizable(False, False)
    root.mainloop()  # Enter Tkinter event loop

for i in range(200000):
    x1 = random.randint(50, 700)
    y1 = random.randint(50, 700)
    windowopener(x1, y1)
