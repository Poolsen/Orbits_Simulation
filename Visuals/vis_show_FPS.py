import config
from Visuals import vis_draw_text
from launch import pygame_launcher

def vis_show_current_fps():
    current_fps = str(int((pygame_launcher.clock.get_fps())))
    current_fps_text = f"FPS: {current_fps}"
    return vis_draw_text(current_fps_text, pygame_launcher.font_arial, (255, 255, 255), (5, 5), None)
