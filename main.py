import sys


def main():
    from launch import create_moving_Objects
    satelliten = create_moving_Objects.init_moving_objects()

    from Visuals import init_buttons, draw_current_screen
    buttons, buttons_update_pos = init_buttons()

    from launch import pygame_launcher
    # initiates both physics and visual aspects of buttons and satellites, imports the function that decides what screen should be drawn
    draw_current_screen(satelliten, buttons, pygame_launcher.clock, "vis_Himmelskoerper", buttons_update_pos)       #der hier gepasste screen ist nur am Anfang, also mit was angefangen werden soll

    pygame_launcher.pygame.quit()       # nachdem wir aus dem loop raus sind, soll auch pygame geschlossen werden (eigtl, sollte der code nie hier hinkommen, da schon jeweils bei der vis_draw_... Funktion geschlossen wird, aber als Backup )
    sys.exit()

main()      #ich lasse die main() function laufen / ausführen (call)
