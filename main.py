from config import *

# initiates both physics and visual aspects of buttons and satellites
from Visuals import init_buttons, init_satelliten


def main():
    run = True  #by default soll das Programm laufen und sich nicht schließen
    clock = pygame.time.Clock()     #eine Uhr, die u.a. restricted wie weit die Zeit gehen kann und für richtige "steps" sorgt

    satelliten = init_satelliten()
    buttons = init_buttons()


    while run:  #während run is True gilt, wird das window und pygame offen bleiben
        clock.tick(FPS)      # der loop läuft mit max. 60 fps, da das programm nach jedem loop schaut, wie lang es gebraucht hat
        screen.fill((0, 0, 0))  # hintergrundfarbe des windows (schwarz)

        for event in pygame.event.get():    # alles, was in pygame und dem window passiert, mich interessiert nur, ob auf das X gedrückt wird, um zu schließen
            if event.type == pygame.QUIT:   # wenn auf das X gedrückt wird
                run = False                 # soll das Programm nicht mehr laufen, da run = false wird, wird der while loop nicht mehr ausgeführt

        for (koerper, koerper_vis) in satelliten:
            koerper.position_berechnen(satelliten)

            koerper_vis.draw(koerper, screen)

        for button in buttons:
            button.draw()

        pygame.display.update()     #updated, was angezeigt wird

    pygame.quit()       # nachdem wir aus dem loop raus sind, soll auch
    sys.exit()

main()      #ich lasse die main() function laufen / ausführen (call)
