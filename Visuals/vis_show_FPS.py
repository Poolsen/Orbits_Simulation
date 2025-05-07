import config
from Visuals import vis_draw_text

def vis_show_current_fps():
    current_fps = str(int((config.clock.get_fps())))
    current_fps_text = f"FPS: {current_fps}"
    return vis_draw_text(current_fps_text, config.font_arial, (255, 255, 255), (5, 5), None)
