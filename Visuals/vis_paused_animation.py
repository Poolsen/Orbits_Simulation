from config import *

while screen_to_show == "vis_paused_animation":
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        for button in buttons:
            button.draw()
