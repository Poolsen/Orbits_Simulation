# installed packages: pygame

# Path to your virtual environment
venv_path = r"venv\Scripts\activate_this.py" #das ist der Pfad, um zu activate_this.py zu kommen und es dann auszuführen, was dann das venv startet → packages verfügbar

# Activate the virtual environment
with open(venv_path) as file_:
    exec(file_.read(), {'__file__': venv_path})

import pygame
import math as ma   # für ein paar funktionen nützlich

pygame.init()

breite = 800   #hoehe des windows
hoehe = 800    #breite des windows

window = pygame.display.set_mode((breite, hoehe))   #window wird erstellt
pygame.display.set_caption("Orbits_Simulation")     # Titel des Windows

weiss = (255, 255, 255)     #eine rgb farbe
gelb = (255, 255, 0)        #eine rgb farbe
FPS = 60        #mit wie viel FPS die Animation laufen soll

class Sattelit:
    AE = 149600000 * 1000   #149,6 Millionen km, aber in metern also * 1000
    G = 6.67428e-11         #Gravitationskonstante  ((N * m ** 2) / kg **2)
    Scale = 250 / AE        # 1 Astronomische Einheit entspricht ca. 100 pixeln
    TimeStep = 3600 * 24    # 1 Tag, der Sattelit updated sich also 1 mal pro Tag

    def __init__(self, x, y, radius, masse, farbe):
        self.x = x
        self.y = y

        #global self_x
        #self_x = self.x

        #global self_y
        #self_y = self.y

        self.radius = radius
        self.masse = masse      # in kg
        self.farbe = farbe

        self.orbit = []
        self.planet = False
        self.abstand_zu_Planet = 0

        self.x_v = 0    #geschwindigkeit (in x - Richtung)
        self.y_v = 0    #geschwindigkeit (in y - Richtung)

    def draw(self, window):
        x = self.x * self.Scale + breite / 2
        y = self.y * self.Scale + hoehe / 2


        if len(self.orbit) > 2:
            neue_punkte = []
            for point in self.orbit:
                x, y = point
                x = x * self.Scale + breite / 2
                y = y * self.Scale + hoehe / 2
                neue_punkte.append((x, y))
            pygame.draw.lines(window, self.farbe, False, neue_punkte, 2)

        pygame.draw.circle(window, self.farbe, (x, y), self.radius)

    def anziehung(self, other):     #Static?
        other_x = other.x
        other_y = other.y

        #distance_x = other_x - self_x
        #distance_y = other_y - self_y

        distance_x = other_x - self.x
        distance_y = other_y - self.y

        distance_generell = ma.sqrt(distance_x ** 2 +  distance_y ** 2)

        f_generell = (self.G * self.masse * other.masse) / distance_generell ** 2

        fx =
        fy =



def main():
    run = True  #by default soll das Programm laufen und sich nicht schließen
    clock = pygame.time.Clock()     #eine Uhr, die u.a. restricted wie weit die Zeit gehen kann und für richtige "steps" sorgt

    planet = Sattelit(0, 0, 30, gelb, 1.98892 * 10 ** 30 )      #! hier noch mit Sonnen - Variablen

    while run:  #während run is True gilt, wird das window und pygame offen bleiben
        clock.tick(FPS)      # der loop läuft mit max. 60 fps, da das programm nach jedem loop schaut, wie lang es gebraucht hat
        #window.fill(weiss)  # hintergrundfarbe des windows
        #pygame.display.update()     #updated, was angezeigt wird

        for event in pygame.event.get():    # alles, was in pygame und dem window passiert, mich interessiert nur, ob auf das X gedrückt wird, um zu schließen
            if event.type == pygame.QUIT:   # wenn auf das X gedrückt wird
                run = False                 # soll das Programm nicht mehr laufen, da run = false wird, wird der while loop nicht mehr ausgeführt

    pygame.quit()       # nachdem wir aus dem loop raus sind, soll auch

main()      #ich lasse die main() function laufen / ausführen (call)
