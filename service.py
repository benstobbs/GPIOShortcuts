from gpiozero import Button
from pyautogui import hotkey
from time import sleep

def isint(n):
    try:
        int(n)
        return True
    except:
        return False

def istuple(s):
    try:
        tuple(s)
        return True
    except:
        return False

def line_is_valid(line):
    line = line.strip()
    if len(line) > 0:
        if line[0] != "#":
            lst = line.split(",")
            if len(lst) > 1:
                lst = [el.replace(" ", "") for el in lst]
                pin_number, key_tuple = lst[0], tuple(lst[1:])
                if isint(pin_number) and istuple(key_tuple):
                    return int(pin_number), tuple(key_tuple)
    return None, None

shortcuts = []

with open("config.txt") as f:
    for line in f:
        pin_number, key_tuple = line_is_valid(line)
        if pin_number != None:
            shortcuts.append((Button(pin_number), key_tuple))

while True:
    for s in shortcuts:
        button, args = s
        if button.is_pressed:
            hotkey(*args)
            sleep(0.5)
    sleep(0.05)