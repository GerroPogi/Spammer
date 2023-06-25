import pyautogui as py
import time as t
import keyboard as k
import threading
import sys
r=True
s=False
def spam(sinput, chat_key):
    global r
    i=1
    while r:
        py.press(chat_key.lower())
        py.write(f"{sinput} {i}")
        i+=1
        t.sleep(2)
while True:
    try:
        print("Welcome to the 6b6t spammer made by Beronic. \n Remember, the off switch/key is t")
        t.sleep(0.5)
        while True:
            sinput=input("What do you want to spam?")
            if sinput=="":
                print("kys do it again")
            else:
                break
        while True:
            chat_key=input("What is your chat key (The hotkey for your chat)")
            if chat_key=="":
                print("kys do it again")
            else:
                break
        print("\n")
        break
    except:
        print("Congratulations! you crashed the program, lemme restart it for you...")
        t.sleep(2)
        
x=threading.Thread(target=spam,args=(sinput,chat_key))
x.start()

k.wait("t")
r=False

