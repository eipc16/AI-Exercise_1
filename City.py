import math

class City:
    def __init__(self, index, x_pos, y_pos):
        self._index = index
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._items = []

    def distance_to(self, other):
        return math.sqrt((self._x_pos - other.get_x_pos()) ** 2 + (self._y_pos - other.get_y_pos()) ** 2)

    def get_x_pos(self):
        return self._x_pos

    def get_y_pos(self):
        return self._y_pos

    def add_item(self, item):
        self._items.append(item)
        self._items.sort(key=lambda i: i.calc_value(), reverse=True)

    def get_best_item(self):
        return self._items[0] if len(self._items) > 0 else None

    def __repr__(self):
        return ("Id: %d {X: %f, Y: %f, Items: " % (self._index, self._x_pos, self._y_pos)) + str(self._items)