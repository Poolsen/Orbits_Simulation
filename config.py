# definition aller variablen
import pygame
import sys  #wird hier gebraucht, da auch in main.py gebraucht (→ unused - Anzeige ignorieren)
import datetime     #wird für vis_zeit gebraucht

pygame.init()

#constants
FPS = 60    #maximale FPS, kann auch weniger sein, falls nicht genug computing ressources

#screen to show
#screen_to_show = "vis_Himmelskoerper"    #default

#colors
weiss = (255, 255, 255)     #eine rgb farbe
gelb = (255, 255, 0)        #eine rgb farbe
hellblau = (102, 178, 255)

#pygame stuff
breite = 800
hoehe = 800
screen = pygame.display.set_mode((breite, hoehe))   #window wird erstellt
pygame.display.set_caption("Orbits_Simulation")     # Titel des Windows

#initialise fonts for display on screen
font_comic_sans = pygame.font.SysFont(name="comicsans", size=15, bold=False, italic=False)
font_pause_button = pygame.font.SysFont(name=None, size=30, bold=True, italic=False)
font_arial = pygame.font.SysFont(name="Arial", size=20, bold=False, italic=False)

#initialisiert die clock (für FPS maximum und für FPS anzeigen wichtig)
clock = pygame.time.Clock()  # eine Uhr, die u.a. restricted wie weit die Zeit gehen kann und für richtige "steps" sorgt, wird initialised

breite = 800  # breite des windows
hoehe = 800  # hoehe des windows

pygame.display.set_caption("Orbits_Simulation")  # Titel des Windows


deltaTime = 60          # 1 Minute pro Frame wird "berechnet"


scale_divis = 1e5
scale = 1 / scale_divis