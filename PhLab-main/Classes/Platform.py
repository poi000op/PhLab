
from Constants import *
from Constants import *

# Класс Платформа
# Входные параметры: угол наклона, коэффициент трения, коэффициент упругости.
# Умеет создаваться (начало в левом нижнем углу)

class Platform:
    def __init__(self,platform_angle,platform_friction,platform_elasticity):
        self.angle = platform_angle
        self.shape = pymunk.Segment(space.static_body, (1, HEIGHT), (WIDTH, HEIGHT / self.angle), 2)
        self.shape.elasticity = platform_elasticity
        self.shape.friction = platform_friction

    def create(self, space):

        space.add(self.shape)
