from config import *

def draw_current_screen(satelliten, buttons, clock, screen_to_show):
    run = True #default, damit das programm anfängt zu laufen
    screen_to_show = screen_to_show

    while run:  # während run is True gilt, wird das window und pygame offen bleiben
        clock.tick(FPS)  # der loop läuft mit max. 60 fps, da das programm nach jedem loop schaut, wie lang es gebraucht hat
        screen.fill((0, 0, 0))  # hintergrundfarbe des windows (schwarz)

        match screen_to_show:
            case "vis_Himmelskoerper":

                for event in pygame.event.get():    # alles, was in pygame und dem window passiert, mich interessiert nur, ob auf das X gedrückt wird, um zu schließen
                    if event.type == pygame.QUIT:   # wenn auf das X gedrückt wird
                        run = False                 # soll das Programm nicht mehr laufen, da run = false wird, wird der while loop nicht mehr ausgeführt

                for (koerper, koerper_vis) in satelliten:
                    koerper.position_berechnen(satelliten)

                    koerper_vis.draw(koerper, screen)

                for button in buttons:
                    button_returns = [button.draw()]
                    print(button_returns)
                    if button_returns[0] is True:
                        screen_to_show = "vis_paused_animation"

            case "vis_paused_animation":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                for button in buttons:
                    button.draw()

            case "vis_start_menu":
                pass
            case "vis_new_animation":
                pass
            case "vis_saved_animation":
                pass
            case _:
                print("Diese Option exisitiert nicht!")

        pygame.display.update()  # updated, was angezeigt wird
