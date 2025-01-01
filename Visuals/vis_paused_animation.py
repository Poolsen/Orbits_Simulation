from config import *

def vis_draw_paused_animation(buttons):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
    for button in buttons:
        button.draw()

    pygame.display.update()  # updated, was angezeigt wird