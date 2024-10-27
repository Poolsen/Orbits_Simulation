# installed packages: pygame

# Path to your virtual environment
venv_path = r"venv\Scripts\activate_this.py" #das ist der Pfad, um zu activate_this.py zu kommen und es dann auszuführen, was dann das venv startet → packages verfügbar

# Activate the virtual environment
with open(venv_path) as file_:
    exec(file_.read(), {'__file__': venv_path})

import pygame
import math as ma   # für ein paar funktionen nuetzlich

pygame.init()

breite = 1000   #hoehe des windows
hoehe = 1000    #breite des windows
weiss = (255, 255, 255)     #eine rgb farbe
FPS = 60        #mit wie viel FPS die Animation laufen soll

window = pygame.display.set_mode((breite, hoehe))   #window wird erstellt
pygame.display.set_caption("Orbits_Simulation")     # Titel des Windows

def main():
    run = True  #by default soll das Programm laufen und sich nicht schließen
    clock = pygame.time.Clock()     #eine Uhr, die u.a. restricted wie weit die Zeit gehen kann und für richtige "steps" sorgt


    while run:  #während run is True gilt, wird das window und pygame offen bleiben
        clock.tick(FPS)      # der loop läuft mit max. 60 fps, da das programm nach jedem loop schaut, wie lang es gebraucht hat
        #window.fill(weiss)  # hintergrundfarbe des windows
        #pygame.display.update()     #updated, was angezeigt wird

        for event in pygame.event.get():    # alles, was in pygame und dem window passiert, mich interessiert nur, ob auf das X gedrückt wird, um zu schließen
            if event.type == pygame.QUIT:   # wenn auf das X gedrückt wird
                run = False                 # soll das Programm nicht mehr laufen, da run = false wird, wird der while loop nicht mehr ausgeführt

    pygame.quit()       # nachdem wir aus dem loop raus sind, soll auch

main()      #ich lasse die main() function laufen / ausführen
