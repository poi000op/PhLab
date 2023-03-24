
import pymunk
from random import randrange

# Класс Круг.
# Входные параметры: масса, радиус.
# Возможные параметры: коэффициенты трения и упругости.
# Умеет создаваться в определенном месте


class Circle:
    def __init__(self, circle_mass,circle_radius):
        self.mass = circle_mass
        self.radius = circle_radius
        self.moment = pymunk.moment_for_circle(circle_mass, 0, circle_radius, (0, 0))
        self.body = pymunk.Body(circle_mass, self.moment)
        self.shape = pymunk.Circle(self.body, circle_radius)
        self.shape.elasticity = 0.4
        self.shape.friction = 1.0

    def create(self, pos, space):
        self.body.position = pos
        self.shape.color = [randrange(256) for i in range(4)]
        space.add(self.body, self.shape)

