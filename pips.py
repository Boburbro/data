pips= ["pyautogui","colorama","pyfiglet"]

import os
def up(*a):
    for i in pips:
        os.system(f"pip install {i}")
        print(f"{i}")
