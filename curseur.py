import pyautogui
import time
#oui
while True:
    x, y = pyautogui.position()
    print(f"Coordonnées du curseur : x={x}, y={y}")
    time.sleep(0.5)