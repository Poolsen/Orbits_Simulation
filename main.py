from config import *

# initiates both physics and visual aspects of buttons and satellites, imports the function that decides what screen should be drawn
from Visuals import init_buttons, init_satelliten, draw_current_screen


def main():
    clock = pygame.time.Clock()     #eine Uhr, die u.a. restricted wie weit die Zeit gehen kann und für richtige "steps" sorgt, wird initialised
    satelliten = init_satelliten()
    buttons = init_buttons()

    draw_current_screen(satelliten, buttons, clock, "vis_Himmelskoerper")       #der hier gepasste screen ist nur am Anfang, also mit was angefangen werden soll

    pygame.quit()       # nachdem wir aus dem loop raus sind, soll auch
    sys.exit()

main()      #ich lasse die main() function laufen / ausführen (call)
