import imageio
import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import speech_recognition as sr 
from tkinter.font import Font
from time import sleep
import threading

def open_program1():
    root = tk.Tk()
    root.title("HALT STOP")

    my_font = Font(
        family="css/baby-shower-time/BabyShowerTime",
        size=13,
        weight="bold")

    image = Image.open("pictures/goofylawliet.jpeg")
    photo = ImageTk.PhotoImage(image)

    label1 = tk.Label(root, image=photo)
    label1.pack()

    label2 = tk.Label(root, text="dieses code ist noch unvollständig und wegen des zeitdrucks werde ich es später updaten! Geniess dieses Prototyp",font=my_font)
    label2.pack()

    button1 = tk.Button(root, text="OKAY DANKE FÜR DEN UNVERTIGEN CODE LOSER", command=root.destroy)
    button1.pack()


    root.mainloop()

def start_audio_processing():
    thread = threading.Thread(target=process_audio)
    thread.daemon = True  # Allow the program to exit when the main thread exits
    thread.start()

def imageupdater(imagepath, labeltext):
    image = Image.open(imagepath)
    photo = ImageTk.PhotoImage(image)
    label1.configure(image=photo)
    label1.image = photo

    label2.configure(text=labeltext)

greetings = [
    "Hello",
    "Hi",
    "Hey",
    "Good morning",
    "Good afternoon",
    "Good evening",
    "Hi there",
    "Greetings",
    "Salutations",
    "Howdy",
    "What's up",
    "Yo",
    "Hiya",
    "Hi there",
    "Nice to meet you",
    "Welcome",
    "How's it going",
    "Bonjour",
    "Hola",
    "Ciao",
    "Namaste",
    "Guten Tag",
    "Salam",
    "Shalom",
    "Konnichiwa",
    "Hallo",
    "Aloha",
    "Sup",
    "Hi friend",
    "Hello there",
    "Top of the morning to you",
    "Good to see you",
    "How do you do",
    "Hi folks",
    "Greetings and salutations",
    "Pleased to meet you",
    "Hello world"
]

goodbyes = [
    "Goodbye",
    "Farewell",
    "Adieu",
    "Adios",
    "Cheerio",
    "See you later",
    "See you soon",
    "Take care",
    "Until next time",
    "So long",
    "Bye",
    "Bye-bye",
    "Ciao",
    "Later",
    "Catch you later",
    "Toodles",
    "Sayonara",
    "Auf Wiedersehen",
    "Hasta luego",
    "Peace out",
    "Bye for now",
    "Take it easy",
    "Goodnight",
    "Have a great day",
    "Have a good one",
    "Have a good day",
    "Take care of yourself",
    "Goodbye for now",
    "Stay safe",
    "See you around",
    "Until we meet again",
    "Adios amigos",
    "Until then",
    "Keep in touch",
    "Godspeed",
    "Bon voyage",
    "Peace and love",
    "Until next time",
    "May the force be with you",
    "Happy trails"
]

open_program1()
#Variables
imagepath = "pictures/lawliet2.png"
labeltext = "Hi, I'm Lawliet, your personal assistant."

def process_audio():
    global imagepath, labeltext, greetings, goodbyes
    
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("ich höre:")
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("du sagtest:", text)
            if text in greetings:
                imageupdater("pictures/lawliet3.jpeg", "bye bye ^-^")

            elif text in goodbyes:
                imageupdater("pictures/lawliet3.jpeg", "bye bye ^-^")
                sleep(3)
                subprocess.call("taskkill /IM python.exe /F", shell=True)
            elif text == "open commands":
                
                f = open("commands.txt", "r")
                f = f.read()

                root = tk.Tk()
                root.title("rules")

                my_font = Font(
                    family="css/baby-shower-time/BabyShowerTime",
                    size=8,
                    weight="bold")

                label2 = tk.Label(root, text=f,font=my_font)
                label2.pack()

                root.mainloop()

            elif text == "apps":
                subprocess.run(["python", "apps/apps.py"])
            elif text == "game":
                subprocess.run(["python", "apps/games/games.py"])
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
            imageupdater("pictures/lawliet4.jpeg", "coudn't understand audio ;(")

        except sr.RequestError as e:
            print(f"Error with the API request; {e}")

root = tk.Tk()
root.title("Lawliet")

my_font = Font(
    family="css/baby-shower-time/BabyShowerTime",
    size=13,
    weight="bold")

image = Image.open(imagepath)
photo = ImageTk.PhotoImage(image)

label1 = tk.Label(root, image=photo)
label1.pack()

label2 = tk.Label(root, text=labeltext,font=my_font)
label2.pack()

start_audio_processing()

root.mainloop()






