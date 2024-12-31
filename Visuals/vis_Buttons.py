from config import *

class Button:
    def __init__(self,text,width,height,pos,elevation):
        #Core attributes
        self.pressed = False
        self.elevation = elevation

        #rectangle
        self.rect = pygame.Rect(pos,(width,height))
        self.color = (100, 100, 100)

        #text
        self.text_surf = font.render(text,True,(255, 255, 255))
        self.text_rect = self.text_surf.get_rect(center = self.rect.center)

    def draw(self):
        pygame.draw.rect(screen,self.color, self.rect,border_radius = 12)
        screen.blit(self.text_surf, self.text_rect)
        return self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.color = (200, 200, 200)
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
                return False
            elif self.pressed is True:
                print('click')
                self.pressed = False
                return True     # wurde gecklicked
            else:
                return False
        else:
            self.color = (100, 100, 100)
            return False        # wurde nicht gecklicked

def init_buttons():
    button0 = Button('Click me',200,40,(200,250),5)
    buttons = [button0, ]
    return buttons