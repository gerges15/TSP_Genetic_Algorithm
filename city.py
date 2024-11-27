import numpy as np


class City:
    def __init__(self, x, y):
        self._x_point = x
        self._y_point = y

    def distance(self, city):
        x_difference = abs(self.get_x - city.get_x)
        y_difference = abs(self.get_y - city.get_y)
        result = np.sqrt((self.square(x_difference)) + (self.square(y_difference)))
        return result

    @property
    def get_x(self):
        return self._x_point

    @property
    def get_y(self):
        return self._y_point

    def square(self, num):
        return num**2
