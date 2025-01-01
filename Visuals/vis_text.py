from config import *

def vis_draw_text(text, font_to_use, color, position, where_to_center):        # where to center muss ein pygame objekt - rechteck sein
    text_surf = font_to_use.render(text, True, color)
    if type(where_to_center) is not tuple:
        screen.blit(text_surf, position)
    else:
        text_rect = text_surf.get_rect(center = where_to_center)
        screen.blit(text_surf, text_rect)

