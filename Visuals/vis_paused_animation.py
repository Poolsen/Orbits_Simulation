import sys
import pygame
import config

def vis_draw_paused_animation(buttons):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #run = False
            pygame.quit()
            sys.exit()
        #elif event.type == pygame.MOUSEWHEEL: #während vis_paused_animation sollte man nicht scale andern können, da das sonst ganze update logic mit optimization zerstört
        #    vis_scroll_change_scale(event.y)

    button_returns = []
    for button in buttons:
        if button.id == 0:  # button 0 ist der pause button, dieser darf nicht im animation screen gerendert werden
            button_returns.append(False)    # der pause button kann nicht gedrückt werden, da an seiner stelle der continue button ist.
            continue                        # der pause button soll in der pausierten animation logischerweise nicht gezeichnet werden, sonst wären pause und continue übereinander, die iteration wird geskippt, der button wird nicht gezeichnet, der return wurde manuell automatisch erzeugt

        button_returns.append(button.draw())
        if button.id == 1 and button_returns[1]:       # wenn button 1 (continue button) gedrückt wurde (es muss nur bei button 1 gecheckt werden, da sonst ja erst bei
            screen_to_show = "vis_Himmelskoerper"  # wird geändert, wenn gedrückt wurde
            return screen_to_show  # sollte der pause button gedrückt worden sein, dann kann der loop unterbrochen werden, es kann schließlich nur ein button gedrückt worden sein

    screen_to_show = "vis_paused_animation"
    return screen_to_show
