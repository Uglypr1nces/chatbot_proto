#password generator

import random

easy = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
hard = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ';', ':', '\'', '\"', ',', '.', '<', '>', '/', '?']

#! do no choose a large number

lenght = input("how long do you want your password to be?")
newlenght = int(lenght)

def createhardpassword():
    return ''.join(random.choice(hard)for _ in range(newlenght))  # Generates an 8-character password

def createeasypassword():
    return ''.join(random.choice(easy)for _ in range(newlenght))  # Generates an 8-character password

question = input("Do you want a simple password or a hard one? (simple, hard) ")
if question == "hard":
    while True:
        password = createhardpassword()
        print("Generated password:", password)
        question1 = input("Are you satisfied? (y or n) ")
        if question1.lower() == "y":
            break
else:
    while True:
        password1 = createeasypassword()
        print("Generated password:", password1)
        question2 = input("Are you satisfied? (y or n) ")
        if question2.lower() == "y":
            break


def passwordchecker():
    pass

