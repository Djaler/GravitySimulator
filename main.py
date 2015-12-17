#!/usr/bin/env python3
from tkinter import Tk, Canvas
from FlyObject import FlyObject
from random import randint
from itertools import combinations
from Collapses import Collapses

root = Tk()
width = 1366
height = 700
c = Canvas(root, width=width, height=height)
c.pack()

system = []
for i in range(300):
    x = randint(0, width)
    y = randint(0, height)
    mass = randint(1, 100)
    vx = randint(-20, 20) / 10
    vy = randint(-20, 20) / 10
    system.append(FlyObject(c, x, y, mass, vx, vy))


def go(objects, canvas):
    collapses = Collapses()

    collapsed = set()
    for object1, object2 in combinations(objects, 2):
        if object1.dist(object2) < 5:
            collapsed.add(object1)
            collapsed.add(object2)
            collapses.add(object1, object2)

    for obj in collapsed:
        objects.remove(obj)

    objects.extend(collapses.calc())

    for obj in objects:
        others = objects.copy()
        others.remove(obj)
        obj.set_others(others)

    for obj in objects:
        obj.move()

    c.after(10, go, objects, canvas)


go(system, c)

root.mainloop()