from math import hypot
from profiler import Profiler

T = 0.25


class FlyObject(object):
    def __init__(self, canvas, x, y, mass, vx=0.0, vy=0.0):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.mass = mass
        self.radius = int((mass ** (1 / 3.0)) / 2)
        self.vx = vx
        self.vy = vy
        self.id = canvas.create_oval(x - self.radius, y - self.radius,
                                     x + self.radius, y + self.radius,
                                     fill='#000')
        self.others = []

    def set_others(self, others):
        self.others = others

    def dist(self, other):
        return hypot((self.x - other.x),
                     (self.y - other.y)) - self.radius - other.radius

    def move(self):
        ax = 0
        ay = 0
        x = self.x
        y = self.y
        for other in self.others:
            dx = other.x - x
            dy = other.y - y
            r = hypot(dx, dy)
            ax += other.mass * dx / r ** 3
            ay += other.mass * dy / r ** 3

        self.vx += ax
        self.vy += ay

        dx = T * self.vx
        dy = T * self.vy
        self.x += dx
        self.y += dy

        self.canvas.move(self.id, dx, dy)

    @staticmethod
    def join(object1, object2):
        mass = object1.mass + object2.mass

        x = (object1.x * object1.mass + object2.x * object2.mass) / mass
        y = (object1.y * object1.mass + object2.y * object2.mass) / mass

        vx = (object1.vx * object1.mass + object2.vx * object2.mass) / mass
        vy = (object1.vy * object1.mass + object2.vy * object2.mass) / mass

        object1.canvas.delete(object1.id)
        object1.canvas.delete(object2.id)
        return FlyObject(object1.canvas, x, y, mass, vx, vy)