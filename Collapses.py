from FlyObject import FlyObject


class Collapses(object):
    def __init__(self):
        self.collapses = []

    def add(self, object1, object2):
        for collapse in self.collapses:
            if object1 in collapse:
                collapse.add(object2)
                break
            elif object2 in collapse:
                collapse.add(object1)
                break
        else:
            self.collapses.append({object1, object2})

    def calc(self):
        result = []
        for collapse in self.collapses:
            collapse = list(collapse)
            main_object = FlyObject.join(collapse[0], collapse[1])
            for obj in collapse[2:]:
                main_object = FlyObject.join(main_object, obj)
            result.append(main_object)

        return result