from config import *

def vis_draw_paused_animation(buttons):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

    for button in buttons:
        if button.id == 0:  # button 0 ist der pause button, dieser darf nicht im animation screen gerendert werden
            continue
        button_returns = [button.draw()]
        # print(button_returns) #nur fpr debugging
        if button_returns[0] is True:       #rückgabewert von button 1 ist bei 0, da button 0 übersprungen wird
            screen_to_show = "vis_Himmelskoerper"  # wird geändert, wenn gedrückt wurde
            return screen_to_show  # sollte der pause button gedrückt worden sein, dann kann der loop unterbrochen werden, es kann schließlich nur ein button gedrückt worden sein

    screen_to_show = "vis_paused_animation"
    return screen_to_show
