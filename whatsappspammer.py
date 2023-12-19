import pyautogui as pt
import time

limit = input("Enter limit:")
message = ("pictures/lawliet1.jpeg")
i = 0

while i < int(limit):
    pt.typewrite(message)
    pt.press("enter")
    i+=1
