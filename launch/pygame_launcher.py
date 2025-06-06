import pygame
import config


#pygame initalizer

pygame.init()
#pygame stuff
screen = pygame.display.set_mode((config.breite, config.hoehe))   #window wird erstellt
pygame.display.set_caption("Orbits_Simulation")     # Titel des Windows

#initialise fonts for display on screen
font_comic_sans = pygame.font.SysFont(name="comicsans", size=15, bold=False, italic=False)
font_pause_button = pygame.font.SysFont(name=None, size=30, bold=True, italic=False)
font_arial = pygame.font.SysFont(name="Arial", size=20, bold=False, italic=False)

#initialisiert die clock (für FPS maximum und für FPS anzeigen wichtig)
clock = pygame.time.Clock()  # eine Uhr, die u.a. restricted wie weit die Zeit gehen kann und für richtige "steps" sorgt, wird initialised

pygame.display.set_caption("Orbits_Simulation")  # Titel des Windows
