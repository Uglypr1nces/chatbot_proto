import pyautogui as pt
import time

limit = input("Enter limit:")
message = ("lil nigga boy")
i = 0

while i < int(limit):
    pt.typewrite(message)
    pt.press("enter")
    i+=1
