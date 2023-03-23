


class Platform:
    def __init__(self,platform_angle,platform_friction,platform_elasticity):
        self.angle = platform_angle
        self.shape.elasticity = platform_elasticity
        self.shape.friction = platform_friction

    def create(self, space):
        self.shape = pymunk.Segment(space.static_body, (1, HEIGHT), (WIDTH, HEIGHT / platform_angle), 2)
        space.add(self.shape)
