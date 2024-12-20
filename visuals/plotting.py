import pygame

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
