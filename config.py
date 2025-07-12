# definition aller variablen/Konstanten

# jede Sekunde Simulationszeit wird eine richtige Stunde Zeit simuliert. (TIME_PER_SECOND)
# die Target FPS, also angezeigte Frames per second sind 60 FPS
FPS = 60    #maximale FPS, kann auch weniger sein, falls nicht genug computing resources / HIER IST FPS WIE VIELE SCHLEIFEN PRO SEKUNDE, NICHT BILDER
deltaTime = 0.1               # bei jedem Durchlauf werden 6 Sekunden weiterberechnet
TIME_PER_SIM_SECOND = 60 * 60   # in jeder Sekunde Simulation wird 1 Stunde echte Zeit simuliert
sim_seconds_per_frame = TIME_PER_SIM_SECOND / FPS  # 3600 / 60 = 60
ITERATIONS_PER_FRAME = max(int(round(sim_seconds_per_frame / deltaTime)), 1)  # 60 / 6 = 10

#screen to show
#screen_to_show = "vis_Himmelskoerper"    #default

#colors
weiss = (255, 255, 255)     #eine rgb farbe
gelb = (255, 255, 0)        #eine rgb farbe
hellblau = (102, 178, 255)

#pygame stuff
breite = 800
hoehe = 800


logarithmic_scroll: bool = True

scale_divis = 1e5
scale = 1 / scale_divis

# laut dem tollen typen auf Stack Overflow kann man so farbigen output auch auf alten windows-kerneln erzeugen (:

orbit_points_max_length = 900

import os
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__)))   #gibt den Pfad zum dir von config.py an, also dem Hauptverzeichnis -> dynamische Erstellung
PRESET_FILE = os.path.join(PROJECT_ROOT, "data", "preset_data.json")

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
