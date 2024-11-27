import numpy as np


class City:
    def __init__(self, x, y):
        self._x_coordinate = x
        self._y_coordinate = y

    def distance(self, city):
        x_difference = abs(self.get_x - city.get_x)
        x_distance = x_difference
        y_distance = abs(self.get_y - city.get_y)
        result = np.sqrt((x_distance**2) + (y_distance**2))
        return result

    @property
    def get_x(self):
        return self._x_coordinate

    @property
    def get_y(self):
        return self._y_coordinate
