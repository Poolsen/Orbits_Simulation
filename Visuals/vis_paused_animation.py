from config import *

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False
    for button in buttons:
        button.draw()
