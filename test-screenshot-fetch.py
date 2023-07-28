import cv2
import numpy
import mss.tools
import pytesseract
import pyautogui
import re
import time
import keyboard
from PIL import Image



def loot(num):
    for i in range(0, num):
        pyautogui.keyDown("enter")
        time.sleep(0.001)
        pyautogui.keyUp("enter")
        time.sleep(0.1)



def main():
    inv_slot = 0
    #1440p fullscreen 2560x1440
    monitor_boxes = [
        {"top":388,"left":1773,"width":590,"height":47},
        {"top":446,"left":1773,"width":590,"height":47},
        {"top":503,"left":1773,"width":590,"height":47},
        {"top":561,"left":1773,"width":590,"height":47},
        {"top":618,"left":1773,"width":590,"height":47},
        {"top":676,"left":1773,"width":590,"height":47},
        {"top":733,"left":1773,"width":590,"height":47},
        {"top":791,"left":1773,"width":590,"height":47},
        {"top":848,"left":1773,"width":590,"height":47},
        {"top":906,"left":1773,"width":590,"height":47},
        {"top":964,"left":1773,"width":590,"height":47},
        {"top":1021,"left":1773,"width":590,"height":47},
        {"top":1079,"left":1773,"width":590,"height":47},
    ]

    while True:
        with mss.mss() as sct:
            # The screen part to capture
            monitor = monitor_boxes[inv_slot]

            # Grab the data
            sct_grab_monitor = sct.grab(monitor)
            sct_img = numpy.array(sct_grab_monitor, dtype=numpy.uint8)
            #sct_img = numpy.flip(sct_img[:, :, :3], 2)  # BGRA -> RGB conversion
            sct_img = cv2.cvtColor(sct_img, cv2.COLOR_BGR2GRAY)

            #debug
            #mss.tools.to_png(sct_grab_monitor.rgb, sct_grab_monitor.size, output="sct.png")

            # Get item list
            loot_list = pytesseract.image_to_string(Image.fromarray(sct_img)).replace("\n","") #.split("\n")

            # ['.45 Round', '5.56 Round (5)', 'Assault Rifle', 'Assault Rifle', 'Biometric Scanner', 
            # 'Charging Laser Sniper Rifle', 'Charging Laser Sniper Rifle', 'Fragmentation Grenade', 
            # 'Fuse', 'Rib Cage and Spine', 'Short Hunting Rifle', 'Short Hunting Rifle', 
            # 'Skull Eye Socket', '']
            # ['Nocturnal T-45 Right Leg *', 'Cap (4)', 'Cap (4)', 'Cap (6)', 'Cap (7)', '.308 Round (4)',
            # '.38 Round (6)', '.38 Round (7)', '.38 Round (7)', '.38 Round (8)', '.45 Round (2)',
            # '.45 Round (2)', '.45 Round (2)', '']

            entry = loot_list
            print(entry)
            if entry != "":
                if "*" in entry:
                    loot(1)
                elif entry == "Cap" or "Cap (" in entry:
                    loot(1)
                elif " Round" in entry:
                    loot(1)
                    try:
                        round_count = re.search('\(([0-9]+)\)', entry).group(0)
                    except AttributeError:
                        continue
                    #print(f"round count = {round_count.group(0)}")
                elif "Gunpowder" in entry:
                    loot(1)
                # Figure out why "enter" works in/out of game but
                #  "down" doesn't work ingame
                else:
                    break
            time.sleep(0.500)
                #    inv_slot += 1
                #    pyautogui.keyDown("down")
                #    time.sleep(1)
                #    pyautogui.keyUp("down")
            #input()



pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

keyboard.add_hotkey('y', main)
keyboard.wait()
