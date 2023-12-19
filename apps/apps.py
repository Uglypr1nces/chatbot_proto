import tkinter as tk
import subprocess
from PIL import Image, ImageTk  

def open_program1():
    
    subprocess.run(["python", "apps/createpassword.py"])

def open_program2():
    
    subprocess.run(["python", "apps/for_gambling_addicts.py"])

def open_program3():
    
    subprocess.run(["python", "apps/todolist.py"])

def open_program3():
    
    subprocess.run(["python", "apps/todolist.py"])

root = tk.Tk()
root.title("Apps")
root.geometry("400x200")


# Create buttons to open different programs
button1 = tk.Button(root, text="Password Maker", command=open_program1)
button2 = tk.Button(root, text="Casino", command=open_program2)
button3 = tk.Button(root, text="Todo List", command=open_program3)
button4 = tk.Button(root, text="window spammer", command=open_program4)

# Use grid layout manager to arrange the buttons
button1.grid(row=0, column=0, padx=10, pady=10)
button2.grid(row=0, column=1, padx=10, pady=10)
button3.grid(row=0, column=2, padx=10, pady=10)
button4 = tk.Button(root, text="window spammer", command=open_program4)

root.mainloop()

