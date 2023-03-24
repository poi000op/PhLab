import pymunk
from Constants import *

# Класс Жесткое Соединение
# Соединяет два объекта, сохраняя расстояние между ними
# Входные параметры: два тела и позиция первого тела

class RigidConnection:

    def __init__(self,first,second,firstpos):

        first.create(firstpos,space)
        second.create([600, 50], space)
        self.body = pymunk.PinJoint(first.body,second.body,(0,0))

    def create(self, pos, space):
        self.body.position = pos
        space.add(self.body)

