import config

# initiates both physics and visual aspects of buttons and satellites, imports the function that decides what screen should be drawn
from Visuals import init_buttons, init_satelliten, draw_current_screen


def main():
    satelliten = init_satelliten()
    buttons, buttons_update_pos = init_buttons()

    draw_current_screen(satelliten, buttons, config.clock, "vis_Himmelskoerper", buttons_update_pos)       #der hier gepasste screen ist nur am Anfang, also mit was angefangen werden soll

    config.pygame.quit()       # nachdem wir aus dem loop raus sind, soll auch pygame geschlossen werden (eigtl, sollte der code nie hier hinkommen, da schon jeweils bei der vis_draw_... Funktion geschlossen wird, aber als Backup )
    config.sys.exit()

main()      #ich lasse die main() function laufen / ausführen (call)
