from config import *

class Button:
    def __init__(self,text,pos,width,height, ident, font_to_use):
        self.pressed = False
        self.id = ident
        self.font_to_use = font_to_use

        #rechteck des buttons
        self.rect = pygame.Rect(pos,(width,height))
        self.color = (100, 100, 100)

        #text
        self.text_surf = font_to_use.render(text,True,(255, 255, 255))
        self.text_rect = self.text_surf.get_rect(center = self.rect.center)

    def draw(self):
        pygame.draw.rect(screen,self.color, self.rect,border_radius = 12)
        screen.blit(self.text_surf, self.text_rect)
        return self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.color = (200, 200, 200)    #ändert farbe, wenn man darüber hovert
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
                return False
            elif self.pressed is True:
                # print('click') #nur für debugging
                self.pressed = False
                return True     # wurde gecklickt
            else:
                return False
        else:
            self.color = (100, 100, 100)
            return False        # wurde nicht gecklickt

def init_buttons():
    button0 = Button(text='| |', pos=(750, 750), width=45, height=45, ident=0, font_to_use=font_pause_button)    #pos ist hier die ecke oben links
    button1 = Button(text='continue', pos=(700, 750), width=95, height=45, ident=1, font_to_use=font_comic_sans)
    buttons = [button0, button1, ]
    buttons_update_pos = [          #welche positionen müssen durch pygame.display.update(buttons_update_pos)
        pygame.Rect((750, 750), (45, 45)),
        pygame.Rect((700, 750), (95, 45)),
    ]
    return buttons, buttons_update_pos
