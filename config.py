# definition aller variablen
import pygame
import sys  #wird gebraucht in main.py (unused - Anzeige ignorieren)

pygame.init()

#constants
FPS = 60

#colors
weiss = (255, 255, 255)     #eine rgb farbe
gelb = (255, 255, 0)        #eine rgb farbe
hellblau = (102, 178, 255)

#pygame stuff
breite = 800
hoehe = 800
screen = pygame.display.set_mode((breite, hoehe))   #window wird erstellt
pygame.display.set_caption("Orbits_Simulation")     # Titel des Windows
font = pygame.font.SysFont("comicsans", 16)

breite = 800  # breite des windows
hoehe = 800  # hoehe des windows

pygame.display.set_caption("Orbits_Simulation")  # Titel des Windows
