import sys
import pygame
from Satellites_Calculations import BewegenderHimmelskoerper
from Visuals import Visualisierung


#constants
FPS = 60

#colors
weiss = (255, 255, 255)     #eine rgb farbe
gelb = (255, 255, 0)        #eine rgb farbe
hellblau = (102, 178, 255)

#pygame stuff
breite = 800
hoehe = 800
window = pygame.display.set_mode((breite, hoehe))   #window wird erstellt
pygame.display.set_caption("Orbits_Simulation")     # Titel des Windows

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
