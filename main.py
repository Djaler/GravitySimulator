from itertools import combinations
from tkinter import Canvas, Tk

from Collapses import Collapses
from FlyObject import FlyObject

root = Tk()
width = 1366
height = 700
c = Canvas(root, width=width, height=height)
c.pack()

system = set()
system.add(FlyObject(c, width / 2, height / 2, 10000000, 0, 0))
system.add(FlyObject(c, width / 2 + 200, height / 2, 10, 0, 800))
system.add(FlyObject(c, width / 2 + 400, height / 2, 10, 0, 400))
system.add(FlyObject(c, width / 2 + 500, height / 2, 100, 0, 300))


def go(objects, canvas):
    collapses = Collapses()
    
    collapsed = set()
    for object1, object2 in combinations(objects, 2):
        if object1.dist(object2) < 2:
            collapsed.add(object1)
            collapsed.add(object2)
            collapses.add(object1, object2)
    
    objects.difference_update(collapsed.union(collapses.calc()))
    
    for obj in objects:
        obj.set_others(objects.difference((obj,)))
    
    for obj in objects:
        obj.move()
    
    c.after(50, go, objects, canvas)


go(system, c)

root.mainloop()
