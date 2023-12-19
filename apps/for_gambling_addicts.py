import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import font
import random
from pygame import mixer

mixer.init()

def hotlaugh():
    mixer.init()
    mixer.music.load("content/goodboy.mp3")
    mixer.music.play()

userxp = 50
waifus = ["a","b","c","d","e","f","g"]

user_choice = " "
while userxp < 100 and userxp > 0:
    
    root = tk.Tk()
    root.geometry("800x450")
    frame = Frame(root, width=800, height=450)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)
    
    img = ImageTk.PhotoImage(Image.open("content/casino.jpg"))
    label = Label(frame, image=img)
    label.pack()


    def rules():
        f = open("content/rules.txt", "r")
        print(f.read())

    def begin():
        photos = ["Anime_waifus/a.jpg", "Anime_waifus/b.jpg", "Anime_waifus/c.jpg","Anime_waifus/d.jpg","Anime_waifus/e.jpg","Anime_waifus/f.jpg","Anime_waifus/g.jpg"]  # List of image file paths

        new_window = Toplevel(root)
        new_window.title("Photo Gallery")
        new_window.geometry("130x950")

        frame = Frame(new_window)
        frame.pack(fill="both", expand=True)

        for photo_path in photos:
            img = ImageTk.PhotoImage(Image.open(photo_path))
            label = Label(frame, image=img)
            label.image = img  # Keep a reference to the image
            label.pack()

            def waifu_a():
                global user_choice
                user_choice = "a"
                new_window.destroy()
                new_window2.destroy()
                Question = Button(root,text="You sure?",command=outcome)
                Question.pack()

            def waifu_b():
                global user_choice
                user_choice = "b"
                new_window.destroy()
                new_window2.destroy()
                Question = Button(root,text="You sure?",command=outcome)
                Question.pack()
            def waifu_c():
                global user_choice
                user_choice = "c"
                new_window.destroy()
                new_window2.destroy()
                Question = Button(root,text="You sure?",command=outcome)
                Question.pack()
            def waifu_d():
                global user_choice
                user_choice = "d"
                new_window.destroy()
                new_window2.destroy()
                Question = Button(root,text="You sure?",command=outcome)
                Question.pack()
            def waifu_e():
                global user_choice
                user_choice = "e"
                new_window.destroy()
                new_window2.destroy()
                Question = Button(root,text="You sure?",command=outcome)
                Question.pack()
            def waifu_f():
                global user_choice
                user_choice = "f"
                new_window.destroy()
                new_window2.destroy()
                Question = Button(root,text="You sure?",command=outcome)
                Question.pack()
            def waifu_g():
                global user_choice
                user_choice = "g"
                new_window.destroy()
                new_window2.destroy()
                Question = Button(root,text="You sure?",command=outcome)
                Question.pack()


        new_window2 = Toplevel(root)
        new_window2.title("Photo Gallery")
        new_window2.geometry("1x200")

        a = Button(new_window2,text="a",command=waifu_a)
        a.pack()
        b = Button(new_window2,text="b",command=waifu_b)
        b.pack()
        c = Button(new_window2,text="c",command=waifu_c)
        c.pack()
        d = Button(new_window2,text="d",command=waifu_d)
        d.pack()
        e = Button(new_window2,text="e",command=waifu_e)
        e.pack()
        f = Button(new_window2,text="f",command=waifu_f)
        f.pack()
        g = Button(new_window2,text="g",command=waifu_g)
        g.pack()

    Rules = Button(text="rules",command=rules)
    Rules.pack()

    Begin = Button(text="Choose a waifu",command=begin)
    Begin.pack()

    def outcome():
        global userxp
        end_outcome = random.choice(waifus)
        if end_outcome == user_choice:
            def hotguy():
                hotlaugh()
                window = Toplevel(root)
                frame = Frame(window, width=1200, height=875)
                frame.pack()
                frame.place(anchor='center', relx=0.5, rely=0.5)
                
                img = ImageTk.PhotoImage(Image.open("content/hot.jpg"))
                label = Label(frame, image=img)
                label.image = img
                label.pack()
                if userxp >= 100:
                    print("Congratulations! You have won the special prize!")


            for _ in range(100):
                hotguy()
            

            userxp += 10
            a = 100-userxp
            print("you won 10 exp {} till you win the special price".format(a))

        else:
            def laugh():
                window = Toplevel(root)
                frame = Frame(window, width=1200, height=875)
                frame.pack()
                frame.place(anchor='center', relx=0.5, rely=0.5)
                
                mixer.music.load("content/laugh.mp3")
                mixer.music.play()
                
                img = ImageTk.PhotoImage(Image.open("content/laughing.jpg"))
                label = Label(frame, image=img)
                label.image = img
                label.pack()

            for _ in range(100):
                laugh()

            userxp -= 10
            print(userxp)
            print("the right answer was " + end_outcome)
            if userxp == 0:
                for y in range(1000):
                    laugh()

    root.mainloop()



