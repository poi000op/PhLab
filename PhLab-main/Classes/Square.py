import pymunk
from random import randrange

# Класс Прямоугольник.
# Входные параметры: масса, сторона x, сторона y.
# Возможные параметры: коэффициенты трения и упругости.
# Умеет создаваться в определенном месте

class Square:
    def __init__(self, square_mass,square_size_x,square_size_y):
        self.mass = square_mass
        self.size_x = square_size_x
        self.size_y = square_size_y
        self.size = (square_size_x,square_size_y)
        self.moment = pymunk.moment_for_box(square_mass,self.size)
        self.body = pymunk.Body(self.mass, self.moment)
        self.shape = pymunk.Poly.create_box(self.body, self.size)
        self.shape.elasticity = 0.4
        self.shape.friction = 1.0

    def create(self, pos, space):
        self.body.position = pos
        self.shape.color = [randrange(256) for i in range(4)]
        space.add(self.body, self.shape)