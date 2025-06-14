# definition aller variablen
#constants

FPS = 60    #maximale FPS, kann auch weniger sein, falls nicht genug computing resources

#screen to show
#screen_to_show = "vis_Himmelskoerper"    #default

#colors
weiss = (255, 255, 255)     #eine rgb farbe
gelb = (255, 255, 0)        #eine rgb farbe
hellblau = (102, 178, 255)

#pygame stuff
breite = 800
hoehe = 800


deltaTime = 60          # 1 Minute pro Frame wird "berechnet"

logarithmic_scroll: bool = True

scale_divis = 1e5
scale = 1 / scale_divis

# laut dem tollen typen auf Stack Overflow kann man so farbigen output auch auf alten windows-kerneln erzeugen (:

import os

if os.name == 'nt':
    import ctypes
    kernel32 = ctypes.windll.kernel32
    handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
    mode = ctypes.c_uint32()
    kernel32.GetConsoleMode(handle, ctypes.byref(mode))
    mode.value |= 0x0004  # ENABLE_VIRTUAL_TERMINAL_PROCESSING
    kernel32.SetConsoleMode(handle, mode)


class Colors:
    HEADER     = "\033[95m"
    OKBLUE     = "\033[94m"
    OKCYAN     = "\033[96m"
    OKGREEN    = "\033[92m"
    WARNING    = "\033[93m"
    FAIL       = "\033[91m"
    ENDC       = "\033[0m"
    BOLD       = "\033[1m"
    UNDERLINE  = "\033[4m"
    BLACK      = "\033[30m"
    RED        = "\033[31m"
    ERROR      = "\033[31m"
    GREEN      = "\033[32m"
    SUCCESS    = "\033[32m"
    YELLOW     = "\033[33m"
    BLUE       = "\033[34m"
    PURPLE     = "\033[35m"
    CYAN       = "\033[36m"
    WHITE      = "\033[37m"

#screen to show

#screen_to_show = "vis_Himmelskoerper"    #default
""" -> verschoben nach launch < pygame_launcher
screen = pygame.display.set_mode((breite, hoehe))   #window wird erstellt
pygame.display.set_caption("Orbits_Simulation")     # Titel des Windows

#initialise fonts for display on screen
font_comic_sans = pygame.font.SysFont(name="comicsans", size=15, bold=False, italic=False)
font_pause_button = pygame.font.SysFont(name=None, size=30, bold=True, italic=False)
font_arial = pygame.font.SysFont(name="Arial", size=20, bold=False, italic=False)

#initialisiert die clock (für FPS maximum und für FPS anzeigen wichtig)
clock = pygame.time.Clock()  # eine Uhr, die u.a. restricted wie weit die Zeit gehen kann und für richtige "steps" sorgt, wird initialised

pygame.display.set_caption("Orbits_Simulation")  # Titel des Windows"""
