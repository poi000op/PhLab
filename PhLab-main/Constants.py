import pymunk
import pygame as pg

# Настройки экрана и фона. Параметры для отрисовки.

RES = WIDTH, HEIGHT = 900, 720
FPS = 60

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)

# Параметры физического пространства

space = pymunk.Space()
space.gravity = 0, 8000









