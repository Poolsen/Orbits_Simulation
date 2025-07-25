import config
import pygame
from Visuals import vis_draw_himmelskoeper, vis_draw_paused_animation, vis_show_current_fps, vis_ingame_time
from launch import pygame_launcher

def draw_current_screen(satelliten, buttons, clock, screen_to_show, buttons_update_pos):
    run = True #default, damit das programm anfängt zu laufen

    while run:  # während run is True gilt, wird das window und pygame offen bleiben
        clock.tick(config.FPS)  # der loop läuft mit max. 60 fps, da das programm nach jedem loop schaut, wie lang es gebraucht hat

        match screen_to_show:
            case "vis_Himmelskoerper":
                pygame_launcher.screen.fill((0, 0, 0))  # hintergrundfarbe des windows (schwarz)
                screen_to_show = (vis_draw_himmelskoeper(satelliten, buttons))  #funktion macht gesamte logik und gibt gleichzeitig auch aus, ob der screen_to_show sich geändert hat
                vis_show_current_fps()
                vis_ingame_time()
                pygame.display.update()

            case "vis_paused_animation":
                buttons_update_pos[2] = vis_show_current_fps()      #muss geupdated werden, da sich die hitbox des FPS counters mit unterschiedlichen FPS ändern kann
                pygame.draw.rect(pygame_launcher.screen, (0, 0, 0), buttons_update_pos[1])   #continue button
                pygame.draw.rect(pygame_launcher.screen, (0, 0, 0), buttons_update_pos[2])   #fps counter rectangle
                screen_to_show = vis_draw_paused_animation(buttons)
                vis_show_current_fps()
                buttons_update_pos_to_pass = [buttons_update_pos[1], buttons_update_pos[2]]
                pygame.display.update(buttons_update_pos_to_pass)   #so wird nur ein bestimmter teil des screens (der mit den buttons und dem FPS Counter) geupdated

            case "vis_start_menu":
                print("Existiert noch nicht!")
                input("")
                break
            case "vis_new_animation":
                print("Existiert noch nicht!")
                input("")
                break
            case "vis_saved_animation":
                print("Existiert noch nicht!")
                input("")
                break
            case _:
                print("Der ausgewählte Screen existiert nicht!")
                input(r"Drücke Enter um das Startmenü zu benutzen. Bitte reporte diesen Bug im GitHub-Repo dieses Programms, indem du ein neues Issue öffnest, falls es noch nicht existiert!")
                screen_to_show = "vis_start_menu"
