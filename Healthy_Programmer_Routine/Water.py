import time
from pygame import mixer
mixer.init()
mixer.music.load("Water.mp3")
mixer.music.play()
while True:
    c = input("Have you drink the Water : (y/n)? : ")
    if c=="n":
        mixer.music.pause()
        time.sleep(15)
        mixer.music.play()
    elif c=="y":
        mixer.music.stop()
        f=open("Water", "r+")
        print(f.read())
        f.write(input("Enter how much glass? (triple click space bar) :"))
        break