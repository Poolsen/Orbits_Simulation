import sys

from config import *
from Satellites_Calculations import init_satelliten_physics

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



def init_satelliten():

    erde, s1 = init_satelliten_physics()

    erde_vis = Visualisierung(hellblau, 30)

    s1_vis = Visualisierung(weiss, 20)

    return [(erde, erde_vis), (s1, s1_vis)]

def vis_draw_himmelskoeper(satelliten, buttons):
    for event in pygame.event.get():  # alles, was in pygame und dem window passiert, mich interessiert nur, ob auf das X gedrückt wird, um zu schließen
        if event.type == pygame.QUIT:  # wenn auf das X gedrückt wird
            # run = False  # soll das Programm nicht mehr laufen, da run = false wird, wird der while loop nicht mehr ausgeführt
            pygame.quit()
            sys.exit()
    for (koerper, koerper_vis) in satelliten:
        koerper.position_berechnen(satelliten)

        koerper_vis.draw(koerper, screen)

    for button in buttons:
        button_returns = [button.draw()]
        #print(button_returns) #nur fpr debugging
        if button_returns[0] is True:
            screen_to_show = "vis_paused_animation" #wird geändert, wenn gedrückt wurde
            return screen_to_show   #sollte der pause button gedrückt worden sein, dann kann der loop unterbrochen werden, es kann schließlich nur ein button gedrückt worden sein

    screen_to_show = "vis_Himmelskoerper"
    return screen_to_show
