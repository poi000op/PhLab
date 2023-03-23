#импорт модулей:
import pygame as pg
from random import randrange
import pymunk.pygame_util
pymunk.pygame_util.positive_y_is_up = False

#параметры PyGame
RES = WIDTH, HEIGHT = 900, 720
FPS = 60

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)

#настройки Pymunk
space = pymunk.Space()
space.gravity = 0, 8000

#платформа
platform_angle=2
platform_shape = pymunk.Segment(space.static_body, (1, HEIGHT), (WIDTH, HEIGHT/platform_angle), 2)

space.add(platform_shape)
platform_shape.elasticity = 0.8
platform_shape.friction = 9.0

#соединение двух объектов
class PinJoint:
    def __init__(self, b, b2, a=(0, 0), a2=(0, 0)):
        joint = pymunk.constraint.PinJoint(b, b2, a, a2)
        space.add(joint)


#квадратики
body = pymunk.Body()
def create_square(space, pos):
    square_mass, square_size = 1, (60, 100)
    square_moment = pymunk.moment_for_box(square_mass, square_size)
    square_body = pymunk.Body(square_mass, square_moment)
    square_body.position = pos
    square_shape = pymunk.Poly.create_box(square_body, square_size)
    square_shape.elasticity = 0.4
    square_shape.friction = 1.0
    square_shape.color = [randrange(256) for i in range(4)]
    space.add(square_body, square_shape)
#шарики
def create_circle(space, pos):
    circle_mass, circle_radius = 1, 60
    circle_moment = pymunk.moment_for_circle(circle_mass,0, circle_radius,(0,0))
    circle_body = pymunk.Body(circle_mass, circle_moment)
    circle_body.position = pos
    circle_shape = pymunk.Circle(circle_body, circle_radius)
    circle_shape.elasticity = 0.4
    circle_shape.friction = 1.0
    circle_shape.color = [randrange(256) for i in range(4)]
    space.add(circle_body, circle_shape)

#Отрисовка
b0 = space.static_body
b1 = pymunk.Body(1,pymunk.moment_for_circle(1,0, 3,(0,0)) )
while True:
    surface.fill(pg.Color('white'))

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        # спавн кубиков
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                create_square(space,i.pos)
                #PinJoint(b0,b1, 0)


                print(i.pos)

    space.step(1 / FPS)
    space.debug_draw(draw_options)

    pg.display.flip()
    clock.tick(FPS)

print('end')