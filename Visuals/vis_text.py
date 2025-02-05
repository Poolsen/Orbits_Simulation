from config import *

def vis_draw_text(text, font_to_use, color, position, where_to_center):        # where to center muss ein pygame objekt - rechteck sein
    text_surf = font_to_use.render(text, True, color)
    if type(where_to_center) is not tuple:
        text_rect = text_surf.get_rect(topleft = position)

    else:
        text_rect = text_surf.get_rect(center = where_to_center)

    screen.blit(text_surf, text_rect)

    rect_position = text_rect.topleft  # oder text_rect.center, wenn man lieber will
    rect_width = text_rect.width
    rect_height = text_rect.height
    rect_width_height = (rect_width, rect_height)
    return rect_position, rect_width_height
