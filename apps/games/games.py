import tkinter as tk
import subprocess

def open_program1():
    subprocess.Popen(["createpassword.py"])

def open_program2():
    subprocess.Popen(["for_gambling_addicts.py"])

def open_program3():
    subprocess.Popen(["todolist.exe"])

root = tk.Tk()

button1 = tk.Button(root, text="Open Program 1", command=open_program1)
button1.pack()

button2 = tk.Button(root, text="Open Program 2", command=open_program2)
button2.pack()

button3 = tk.Button(root, text="Open Program 3", command=open_program3)
button3.pack()

root.mainloop()
