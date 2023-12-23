import webbrowser
import subprocess
import datetime
from playsound import playsound
from time import sleep

ascii_art = """
W   W  III  L      L           K   K  OOO  M     M  EEEEE  N     N
W   W   I   L      L           K  K   O   O MM   MM  E      NN    N
W W W   I   L      L           KKK    O   O M M M M  EEEE   N N   N
W W W   I   L      L           K  K   O   O M  M  M  E      N  N  N
 W W   III  LLLLL  LLLLL  LLLLL K   K  OOO  M     M  EEEEE  N   N N
"""

a = 1

x = datetime.datetime.now()
y = datetime.datetime(2024, 1, 1)

if x > y or a == 1:

    print(ascii_art)
    playsound('htmlpages/sounds/intro.mp3')
    sentence = "oh wow, du hast mich bekommen, scheint so als wärst du wichtig für jemanden.. \njedoch um reinzu kommen musst du ein paar fragen beantworten bist du ready?"

    for letter in sentence:
        sleep(0.1)
        print(letter)

    question1 = input("ja oder nein schreiben")

    if question1.lower() == "ja":
        url = "example.html"
        webbrowser.open(url)

        playsound('htmlpages/sounds/beginning_music.mp3')
        sleep(3)
        playsound('htmlpages/sounds/relaxing.mp3')

        secretcode = input("Wenn du fertig bist, kannst du hier den geheimen Code eingeben:")
        if secretcode == "a3b2c1":
            subprocess.run(["python", "chatbot.py"])

    else:
        while True:
            subprocess.run(["python", "windowspammer.py"])
            
else:
    print("einbisschen zu früh nicht?")
    playsound('htmlpages/sounds/gameover.wav')
