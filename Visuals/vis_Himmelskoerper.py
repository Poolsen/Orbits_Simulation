import pygame

#pygame.init()      # wird in main.py gemacht

breite = 800   #breite des windows
hoehe = 800    #hoehe des windows

screen = pygame.display.set_mode((breite, hoehe))   #window wird erstellt
pygame.display.set_caption("Orbits_Simulation")     # Titel des Windows

weiss = (255, 255, 255)     #eine rgb farbe
gelb = (255, 255, 0)        #eine rgb farbe
hellblau = (102, 178, 255)
font = pygame.font.SysFont("comicsans", 16)

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

