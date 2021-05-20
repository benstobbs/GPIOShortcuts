from gpiozero import Button
from pyautogui import hotkey, press, click
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
            if len(lst) > 2:
                lst = [el.replace(" ", "") for el in lst]
                command_type, pin_number, key_tuple = lst[0], lst[1], tuple(lst[2:])
                if isint(pin_number) and istuple(key_tuple) and (command_type == "sequence" or command_type == "hotkey"):
                    return command_type, int(pin_number), tuple(key_tuple)
    return None, None, None

shortcuts = []

with open("/etc/GPIOShortcuts/config.txt") as f:
    for line in f:
        command_type, pin_number, key_tuple = line_is_valid(line)
        if pin_number != None:
            shortcuts.append((command_type, Button(pin_number), key_tuple))

while True:
    for s in shortcuts:
        command_type, button, args = s
        if button.is_pressed:
            if command_type == "hotkey":
                hotkey(*args)
            else:
                keys = list(args)
                for k in keys:
                    if k == "leftclick":
                        click(x = 200, y = 200)
                    elif k == "rightclick":
                        click(x = 200, y = 200, button = "right")
                    else:
                        press(k)
                    sleep(0.1)

            sleep(0.5)
    sleep(0.05)