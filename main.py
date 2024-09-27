import pyautogui
import cv2
import keyboard
import time
import numpy as np

# Chemin vers l'image de la cible à rechercher
chemin_image_golden = 'E:/Code/Projet/CookieCliker/Golden.png'

print("START")
pyautogui.moveTo(286, 462)
cpt = cpt = 0
Seuil_Golden = 0.3


# Importation de l'image cible
template = cv2.imread(chemin_image_golden)


while True:
    # Capture de l'écran
    capture = pyautogui.screenshot()
    capture = cv2.cvtColor(np.array(capture), cv2.COLOR_RGB2BGR)

    # Recherche de la correspondance de l'image
    resultat = cv2.matchTemplate(capture, template, cv2.TM_CCOEFF_NORMED)

    # Trouver les positions des correspondances avec un seuil de similarité donné
    positions = np.where(resultat >= Seuil_Golden)
    positions = list(zip(positions[1], positions[0]))  # Inverser les coordonnées x et y

    if len(positions) > 0:
        # Coordonnées du centre de la cibles
        largeur, hauteur = template.shape[1::-1]
        golden_x = positions[0][0] + largeur // 2
        golden_y = positions[0][1] + hauteur // 2

        # Déplacement de la souris à la position de la cible
        pyautogui.moveTo(golden_x, golden_y)
        time.sleep(0.1)
        pyautogui.moveTo(286, 462)

        cpt = cpt +1
        print("Golden Cookies !!! J'en ai eu : " + str(cpt))

    time.sleep(0.1)
    if keyboard.is_pressed('s'):
        print("STOP")
        break
