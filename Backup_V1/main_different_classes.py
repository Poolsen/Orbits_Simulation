import sys
import pygame
import math as ma

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

class Himmelskoerper:

    # AE = 149600000 * 1000  #149,6 Millionen km, aber in metern also * 1000 // jetzt bei class Visualisierung
    G = 6.67428e-11          #Gravitationskonstante  ((N * m ** 2) / kg **2)
    # scale = 1 / 1e5        # 1 Pixel = 100.000 m = 100 km // jetzt bei class Visualisierung
    deltaTime = 60           # 1 Minute pro Frame
    def __init__(self, x, y, masse):
        self.x = x
        self.y = y
        # self.radius = radius // jetzt bei class Visualisierung
        self.masse = masse      # in kg
        # self.farbe = farbe // jetzt bei class Visualisierung
        self.orbit = []
        self.planet = False
        self.x_v = 0    #geschwindigkeit (in x - Richtung)
        self.y_v = 0    #geschwindigkeit (in y - Richtung)


class BewegenderHimmelskoerper(Himmelskoerper):

    def anziehung(self, other):     #Static?        resolved: Nein

        other_x = other.x
        other_y = other.y

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

    def position_berechnen(self, satelliten):
        f_x_total = f_y_total = 0

        for tupel in satelliten:    # satellit (bzw. "koerper") muss erst aus tupel an stelle 0 extrahiert werden, sonst versuch tupel mit attribut aufzurufen
            satellit = tupel[0]

            if self.planet is True:     # WARUM?
                continue

            if self != satellit:
                fx, fy = self.anziehung(satellit)
                f_x_total += fx
                f_y_total += fy

        self.x_v = self.x_v + (f_x_total / self.masse) * self.deltaTime      # das Gleiche wie self.x_v += (f_x_total / self.masse) * self.TimeStep aber schöner
        self.y_v = self.y_v + (f_y_total / self.masse) * self.deltaTime

        self.x += self.x_v * self.deltaTime
        self.y += self.y_v * self.deltaTime

        self.orbit.append((self.x, self.y))

class Visualisierung:

    def __init__(self, farbe, radius):
        self.scale = 1 / 1e5        # 1 Pixel = 100.000 m = 100 km // jetzt bei class Visualisierung
        self.farbe = farbe          #farbe des Koerpers beim Visualisieren
        self.radius = radius        #radius beim Vis
        #koerper.orbit = orbit         #punkte, die gezeichnet bzw. in draw_punkte übertragen werden
        #koerper.x = x                 # wird aus class BewegenderHimmelskoerper übernommen
        #koerper.y = y                 # wird aus class BH übernommen

    def draw(self, koerper, surface):
        x = koerper.x * self.scale + breite / 2
        y = koerper.y * self.scale + hoehe / 2

        if len(koerper.orbit) >= 2:    #muss, da sonst fehler bei pygame.draw: müssen zum drawn mind. 2 punkte vorhanden sein
            draw_punkte = []
            for point in koerper.orbit:
                x, y = point
                x = x * self.scale + breite / 2     # hier in pixeln
                y = y * self.scale + hoehe / 2      # in pixeln
                draw_punkte.append((x, y))
            pygame.draw.lines(surface, self.farbe, False, draw_punkte, 2)

        pygame.draw.circle(surface, self.farbe, (x, y), self.radius)


def main():
    run = True  #by default soll das Programm laufen und sich nicht schließen
    clock = pygame.time.Clock()     #eine Uhr, die u.a. restricted wie weit die Zeit gehen kann und für richtige "steps" sorgt

    erde = BewegenderHimmelskoerper(0, 0,  5.972 * 10**24)
    erde.planet = True
    erde_vis = Visualisierung(hellblau, 30)


    s1 = BewegenderHimmelskoerper(-36000 * 1000, 0,  200)
    s1.y_v = 3.1 * 1000      #3.1 km/s --> 3100 m/s
    s1_vis = Visualisierung(weiss, 20)

    satelliten = [(erde, erde_vis), (s1, s1_vis)]


    while run:  #während run is True gilt, wird das window und pygame offen bleiben
        clock.tick(FPS)      # der loop läuft mit max. 60 fps, da das programm nach jedem loop schaut, wie lang es gebraucht hat
        window.fill((0, 0, 0))  # hintergrundfarbe des windows (schwarz)

        for event in pygame.event.get():    # alles, was in pygame und dem window passiert, mich interessiert nur, ob auf das X gedrückt wird, um zu schließen
            if event.type == pygame.QUIT:   # wenn auf das X gedrückt wird
                run = False                 # soll das Programm nicht mehr laufen, da run = false wird, wird der while loop nicht mehr ausgeführt

        for (koerper, koerper_vis) in satelliten:
            koerper.position_berechnen(satelliten)

            koerper_vis.draw(koerper, window)

        pygame.display.update()     #updated, was angezeigt wird

    pygame.quit()       # nachdem wir aus dem loop raus sind, soll auch
    sys.exit()

main()      #ich lasse die main() function laufen / ausführen (call)
