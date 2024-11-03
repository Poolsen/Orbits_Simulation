# installed packages: pygame

# Path to your virtual environment
venv_path = r"venv\Scripts\activate_this.py" #das ist der Pfad, um zu activate_this.py zu kommen und es dann auszuführen, was dann das venv startet → packages verfügbar

# Activate the virtual environment
with open(venv_path) as file_:
    exec(file_.read(), {'__file__': venv_path})

import pygame
import math as ma   # für ein paar funktionen nützlich

pygame.init()

breite = 800   #breite des windows
hoehe = 800    #hoehe des windows

window = pygame.display.set_mode((breite, hoehe))   #window wird erstellt
pygame.display.set_caption("Orbits_Simulation")     # Titel des Windows

weiss = (255, 255, 255)     #eine rgb farbe
gelb = (255, 255, 0)        #eine rgb farbe
hellblau = (102, 178, 255)
FPS = 60        #mit wie viel FPS die Animation laufen soll

class Satellit:
    AE = 149600000 * 1000   #149,6 Millionen km, aber in metern also * 1000
    G = 6.67428e-11         #Gravitationskonstante  ((N * m ** 2) / kg **2)
    Scale = 1 / 1e5         # 1 Pixel = 100.000 m = 100 km
    TimeStep = 60           # 1 Minute pro Frame
    font = pygame.font.SysFont("comicsans", 16)


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
        #self.fx = 0

    def draw(self, surface):
        x = self.x * self.Scale + breite / 2
        y = self.y * self.Scale + hoehe / 2


        if len(self.orbit) > 2:
            neue_punkte = []
            for point in self.orbit:
                x, y = point
                x = x * self.Scale + breite / 2
                y = y * self.Scale + hoehe / 2
                neue_punkte.append((x, y))
            pygame.draw.lines(surface, self.farbe, False, neue_punkte, 2)

        pygame.draw.circle(surface, self.farbe, (x, y), self.radius)


    def anziehung(self, other):     #Static?        resolved: Nein

        other_x = other.x
        other_y = other.y

        #distance_x = other_x - self_x
        #distance_y = other_y - self_y

        distance_x = other_x - self.x
        distance_y = other_y - self.y

        distance_generell = ma.sqrt(distance_x ** 2 + distance_y ** 2)


        if distance_generell == 0:
            f_generell = 0

            # ab hier eigentlich unnötig, da fy und fx sowieso = 0 sind, aber für Verständlichkeit // UND: dass eventuell kein Fehler bei distance = 0 kommt, da fx und fy = undefined
            alpha = ma.atan2(distance_y, distance_x)

            fy = ma.sin(alpha) * f_generell

            fx = ma.cos(alpha) * f_generell

        else:
            f_generell = (self.G * self.masse * other.masse) / distance_generell ** 2

            alpha = ma.atan2(distance_y, distance_x)

            fy = ma.sin(alpha) * f_generell

            fx = ma.cos(alpha) * f_generell
            #print(alpha * 180 / ma.pi) #debugging fertig
        return fx, fy

    def postion_berechnen(self, satelliten):
        f_x_total = f_y_total = 0

        for satellit in satelliten:

            if self.planet is True:
                continue

            if self != satellit:
                fx, fy = self.anziehung(satellit)
                f_x_total += fx
                f_y_total += fy

        self.x_v = self.x_v + (f_x_total / self.masse) * self.TimeStep      # das Gleiche wie self.x_v += (f_x_total / self.masse) * self.TimeStep aber schöner
        self.y_v = self.y_v + (f_y_total / self.masse) * self.TimeStep

        self.x += self.x_v * self.TimeStep
        self.y += self.y_v * self.TimeStep


        self.orbit.append((self.x, self.y))



def main():
    run = True  #by default soll das Programm laufen und sich nicht schließen
    clock = pygame.time.Clock()     #eine Uhr, die u.a. restricted wie weit die Zeit gehen kann und für richtige "steps" sorgt

    erde = Satellit(0, 0, 30, 5.972 * 10**24, hellblau)
    erde.planet = True

    s1 = Satellit(-36000 * 1000, 0, 20, 200, weiss)
    s1.y_v = 3.1  * 1000      #3.1 km/s --> 3100 m/s

    satelliten = [erde, s1]


    while run:  #während run is True gilt, wird das window und pygame offen bleiben
        clock.tick(FPS)      # der loop läuft mit max. 60 fps, da das programm nach jedem loop schaut, wie lang es gebraucht hat
        window.fill((0, 0, 0))  # hintergrundfarbe des windows (schwarz)
        for event in pygame.event.get():    # alles, was in pygame und dem window passiert, mich interessiert nur, ob auf das X gedrückt wird, um zu schließen
            if event.type == pygame.QUIT:   # wenn auf das X gedrückt wird
                run = False                 # soll das Programm nicht mehr laufen, da run = false wird, wird der while loop nicht mehr ausgeführt

        for satellit in satelliten:
            satellit.postion_berechnen(satelliten)
            satellit.draw(window)

        pygame.display.update()     #updated, was angezeigt wird

    pygame.quit()       # nachdem wir aus dem loop raus sind, soll auch

main()      #ich lasse die main() function laufen / ausführen (call)