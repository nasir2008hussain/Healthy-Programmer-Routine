import time
from pygame import mixer
mixer.init()
mixer.music.load("Eyes.mp3")
mixer.music.play()
while True:
    c = input("Have you complete the Eye's Exercise : (y/n)? : ")
    if c=="n":
        mixer.music.pause()
        time.sleep(15)
        mixer.music.play()
    elif c=="y":
        mixer.music.stop()
        f=open("Eyes Exercise", "r+")
        print(f.read())
        f.write(input("Enter duration(triple click space bar) :"))
        break
