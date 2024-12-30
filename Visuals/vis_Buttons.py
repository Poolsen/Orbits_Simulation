from config import *

class Button:
    def __init__(self,text,width,height,pos,elevation):
        #Core attributes
        self.pressed = False
        self.elevation = elevation

        # top rectangle
        self.rect = pygame.Rect(pos,(width,height))
        self.color = (200, 200, 200)

        #text
        self.text_surf = font.render(text,True,(255, 255, 255))
        self.text_rect = self.text_surf.get_rect(center = self.rect.center)

    def draw(self):
        # elevation logic
        pygame.draw.rect(screen,self.color, self.rect,border_radius = 12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.color = (200, 200, 200)
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed is True:
                    print('click')
                    self.pressed = False
        else:
            self.color = (100, 100, 100)


