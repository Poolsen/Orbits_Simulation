from config import *
from Visuals import vis_draw_himmelskoeper, vis_draw_paused_animation

def draw_current_screen(satelliten, buttons, clock, screen_to_show, buttons_update_pos):
    run = True #default, damit das programm anfängt zu laufen
    screen_to_show = screen_to_show

    while run:  # während run is True gilt, wird das window und pygame offen bleiben
        clock.tick(FPS)  # der loop läuft mit max. 60 fps, da das programm nach jedem loop schaut, wie lang es gebraucht hat

        match screen_to_show:
            case "vis_Himmelskoerper":
                screen.fill((0, 0, 0))  # hintergrundfarbe des windows (schwarz)
                screen_to_show = (vis_draw_himmelskoeper(satelliten, buttons))  #funktion macht gesamte logik und gibt gleichzeitig auch aus, ob der screen_to_show sich geändert hat
                pygame.display.update()

            case "vis_paused_animation":
                screen_to_show = vis_draw_paused_animation(buttons)
                pygame.display.update(buttons_update_pos[1])

            case "vis_start_menu":
                pass
            case "vis_new_animation":
                pass
            case "vis_saved_animation":
                pass
            case _:
                print("Der ausgewählte Screen existiert nicht!")
                input(r"Drücke Enter, falls ")
