import pygame
import config
import os

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

# kp wie das funktioniert, macht aber, dass Farben farbig sind, also cool ig
if os.name == 'nt':
    import ctypes
    kernel32 = ctypes.windll.kernel32
    handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
    mode = ctypes.c_uint32()
    kernel32.GetConsoleMode(handle, ctypes.byref(mode))
    mode.value |= 0x0004  # ENABLE_VIRTUAL_TERMINAL_PROCESSING
    kernel32.SetConsoleMode(handle, mode)
