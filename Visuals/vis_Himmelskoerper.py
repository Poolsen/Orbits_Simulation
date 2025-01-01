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
            while len(koerper.orbit) >= 900:
                del koerper.orbit[0]

            draw_punkte = []

            for point in koerper.orbit:
                x, y = point
                x = x * self.scale + breite / 2     # hier in pixeln
                y = y * self.scale + hoehe / 2      # in pixeln

                draw_punkte.append((x, y))

            #was zur hölle mache ich hier nur; ist "natürlich nur temporary" (temporary für immer)

            try:
                pygame.draw.lines(surface, (0, 0, 0),       False, draw_punkte[0:15],       2)
                pygame.draw.lines(surface, (25, 25, 25),    False, draw_punkte[15:30],      2)
                pygame.draw.lines(surface, (50, 50, 50),    False, draw_punkte[30:45],      2)
                pygame.draw.lines(surface, (75, 75, 75),    False, draw_punkte[45:60],      2)
                pygame.draw.lines(surface, (100, 100, 100), False, draw_punkte[60:75],      2)
                pygame.draw.lines(surface, (125, 125, 125), False, draw_punkte[75:90],      2)
                pygame.draw.lines(surface, (150, 150, 150), False, draw_punkte[90:105],     2)
                pygame.draw.lines(surface, (175, 175, 175), False, draw_punkte[105:120],    2)
                pygame.draw.lines(surface, (200, 200, 200), False, draw_punkte[120:135],    2)
                pygame.draw.lines(surface, (225, 225, 225), False, draw_punkte[135:150],    2)
                pygame.draw.lines(surface, (250, 250, 250), False, draw_punkte[150:900],    2)

            except ValueError:      # don't worry, be happy
               pass                 # I think I like this "try" "except" thingy (:

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
        if button.id == 1:      #button 1 ist der resume button, dieser darf nicht im animation screen gerendert werden
            continue
        button_returns = [button.draw()]
        #print(button_returns) #nur fpr debugging
        if button_returns[0] is True:
            screen_to_show = "vis_paused_animation" #wird geändert, wenn gedrückt wurde
            return screen_to_show   #sollte der pause button gedrückt worden sein, dann kann der loop unterbrochen werden, es kann schließlich nur ein button gedrückt worden sein

    screen_to_show = "vis_Himmelskoerper"
    return screen_to_show
