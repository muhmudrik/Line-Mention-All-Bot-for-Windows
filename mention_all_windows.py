'''
Original File Creator       : Arya Seputra
Modified for Windows use by : Muhammad Mudrik
'''

import keyboard
import time
import clipboard

def list_all(amount_of_members, file_to_write="unknown"):
    holder = ''
    print("Waiting for hotkey (s+l+n)...")
    keyboard.wait('s+l+n')
    time.sleep(0.3)
    keyboard.press("backspace")
    keyboard.press("backspace")
    keyboard.press("backspace")
    keyboard.press("backspace")
    keyboard.press("backspace")

    for i in range(amount_of_members-1):
        keyboard.write("@")
        time.sleep(0.4)
        for j in range(i):
            keyboard.press("down")
            time.sleep(0.0001)
        keyboard.press("shift+enter")
        keyboard.release("shift")
        if (i+1)%20 == 0 or i == amount_of_members-2:
            keyboard.press('ctrl+a')
            keyboard.press('ctrl+c')
            keyboard.press('ctrl+a')
            keyboard.release('ctrl')
            keyboard.press('backspace')
            time.sleep(0.5)
            holder += clipboard.paste()

    members_lst = holder.split(' ')
    while '' in members_lst:
        members_lst.remove('')
    members_lst = [i.strip(' @').split(' @') for i in members_lst]
    members_txt_w = open(f"{file_to_write}.txt", "w")

    for i in range(len(members_lst)):
        for j in members_lst[i]:
            try:
                print(j+"\n", file=members_txt_w, end="")
            except:
                print(j)
    
    members_txt_w.close()
    
    while True:
        try:
            print("Do you want to continue to tag all members of this group?")
            print("1. Yes")
            print("2. No")
            resp = int(input("Enter: "))
            if resp == 1:
                return True
            return False
        except:
            pass

def tag_all(members_file_name):
    members_txt_r = open(f"{members_file_name}.txt", "r")
    members_lst = [i.strip(' @') for i in members_txt_r.read().split('\n')]
    members_txt_r.close()

    message = input("Enter your message: ")
    print("Waiting for hotkey (m+a+l)...")
    keyboard.wait('m+a+l')
    time.sleep(0.3)
    keyboard.press('backspace')
    keyboard.press('backspace')
    keyboard.press('backspace')
    keyboard.press('backspace')
    keyboard.press('backspace')

    keyboard.write("[" + message + "]")
    keyboard.press("shift+enter")
    keyboard.release("shift")
    for i in range(len(members_lst)):
        keyboard.write(f"{i+1}. ")
        time.sleep(0.1)
        clipboard.copy(members_lst[i])
        keyboard.write("@")
        keyboard.press('ctrl+v')
        keyboard.release('ctrl')
        time.sleep(1)
        keyboard.press('shift+enter')
        keyboard.release('shift')

        if (i+1)%20 != 0 and i != len(members_lst)-1:
            keyboard.press("shift+enter")
            keyboard.release("shift")
        if (i+1)%20 == 0:
            keyboard.press("Enter")
    keyboard.press("Enter")

while True:
    try:
        print("1. I have a list of all the members")
        print("2. I don't have a list of all the members")
        to_do = int(input("Enter: "))
        break
    except:
        pass

if to_do == 1:
    members_file_name = input("Enter the members file name: ")
    tag_all(members_file_name)
elif to_do == 2:
    amount_of_members = int(input("Enter amount of members in the group: "))
    file_to_write = input("Enter the file name to write: ")
    decision = list_all(amount_of_members, file_to_write)

    if decision:
        tag_all(file_to_write)