'''
Original File Creator       : Arya Seputra
Modified for Windows use by : Muhammad Mudrik
Modified for Windows telegram use by: Abdurrafi Arief
'''

import keyboard
import time
import clipboard

def tag_all(amount_of_members):
    holder = ''
    print("Waiting for hotkey to tag all(s+l+n)...")
    keyboard.wait('s+l+n')
    time.sleep(0.3)
    keyboard.press("backspace")
    keyboard.press("backspace")
    keyboard.press("backspace")
    keyboard.press("backspace")
    keyboard.press("backspace")

    for i in range(amount_of_members):
        keyboard.write("@")
        time.sleep(0.4)
        for j in range(i):
            keyboard.press("down")
            time.sleep(0.0001)
        keyboard.press("enter")
    time.sleep(0.1)
    keyboard.press("shift+enter")
    keyboard.release("shift+enter")
    keyboard.write("[Haha a bot tagged you guys]")
    keyboard.press('enter')
    keyboard.release("enter")
    exit()

while True:
    try:
        print("1. I want to tag all")
        print("2. I don't want to tag all")
        to_do = int(input("Enter: "))
        break
    except:
        pass

if to_do == 1:
    amount_of_members = int(input("Enter amount of members in the group: "))
    tag_all(amount_of_members)
elif to_do == 2:
    print("ok lol bye")
    exit()