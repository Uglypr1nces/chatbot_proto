from tkinter import *
from tkinter.font import Font
import datetime

#thsese variables will be used later on

a = " "
b = " "
c = " "

root = Tk()
root.geometry("500x300")
root.title("to do list")

my_font = Font(
    family="Terminal",
    size=20,
    weight="bold")

my_frame = Frame(root)
my_frame.pack(pady=10)

my_list = Listbox(my_frame,
    font=my_font,
    width=25,
    height=5,
    bg="systemButtonFace",
    bd=0,
    fg="#464646",
    highlightthickness=0,
    selectbackground="#a6a6a6",
    activestyle="none"
    )
my_list.pack(side=LEFT, fill=BOTH)

class ThingToDo:
    def __init__(self, date, end, importance):
        self.date = date
        self.end = end
        self.importance = importance

stuff = ["example"]

for item in stuff:
    my_list.insert(END, item)

myscrollbar = Scrollbar(my_frame)
myscrollbar.pack(side=RIGHT, fill=BOTH)

my_list.config(yscrollcommand=myscrollbar.set)
myscrollbar.config(command=my_list.yview)

my_entry = Entry(root, font=("Helvetica", 24))
my_entry.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

def delete_item():
    my_list.delete(ANCHOR)

def details():
    try:
        print(a)
        print(b)
        print(c)
        finaldetails_window = Toplevel(root)
        finaldetails_window.title("Details")
        finaldetails_window.geometry("400x200")

        details_frame = LabelFrame(finaldetails_window, text=f"Details for {selected_item}")
        details_frame.pack(pady=10)

    except:
        selected_item = my_list.get(ANCHOR)
        details_window = Toplevel(root)
        details_window.title("Details")
        details_window.geometry("400x200")

        details_frame = LabelFrame(details_window, text=f"Details for {selected_item}")
        details_frame.pack(pady=10)

        question1 = "wann wollen sie es machen(dd,mm,yyyy)?"
        question2 = "wie wichtig ist es(sehr,mittel,weniger)?"

        my_label = Label(details_frame, text=f"{question1}")
        my_label.pack()

        label_test = Label(details_frame, text="this is just a test")
        label_test.pack()

        my_entry1 = Entry(details_frame, font=("Helvetica", 24))
        my_entry1.pack(pady=20)

        def next_step():
            end_line = my_entry1.get()
            label_test.config(text=end_line)
            my_label.config(text=question2)  # Updated label text for the second question
            my_entry1.delete(0, "end")

        def end():
            importance = my_entry1.get()
            end_line = label_test.cget("text")
            selected_item_obj = ThingToDo(datetime.datetime.now(), end_line, importance)
            details_window.destroy()
            a = selected_item_obj.date
            b = selected_item_obj.end
            c = selected_item_obj.importance
            d = " "
            print(a)
            print(b)
            print(c)

        ok_button = Button(details_frame, text="ok", command=next_step)
        ok_button.pack()

        end_button = Button(details_frame, text="fertig?", command=end)
        end_button.pack()

def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

def cross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#dedede")
    my_list.selection_clear(0, END)

def uncross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#464646")

delete_button = Button(button_frame, text="Delete smth", command=delete_item)
add_button = Button(button_frame, text="add smth", command=add_item)
cross_button = Button(button_frame, text="cross smth", command=cross_item)
uncross_button = Button(button_frame, text="uncross smth", command=uncross_item)
details_button = Button(button_frame, text="details", command=details)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)
details_button.grid(row=0, column=4, padx=20)

root.mainloop()
