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
font = pygame.font.SysFont("comicsans", 16)


from physics import CalculationsMixin
from visuals import PlottingMixin

class Satellit(CalculationsMixin, PlottingMixin):
    AE = 149600000 * 1000   #149,6 Millionen km, aber in metern also * 1000
    G = 6.67428e-11         #Gravitationskonstante  ((N * m ** 2) / kg **2)
    scale = 1 / 1e5         # 1 Pixel = 100.000 m = 100 km
    deltaTime = 60           # 1 Minute pro Frame

    def __init__(self, x, y, radius, masse, farbe):
        self.x = x
        self.y = y

        self.radius = radius
        self.masse = masse      # in kg
        self.farbe = farbe

        self.orbit = []
        self.planet = False
        self.abstand_zu_Planet = 0

        self.x_v = 0    #geschwindigkeit (in x - Richtung)
        self.y_v = 0    #geschwindigkeit (in y - Richtung)


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