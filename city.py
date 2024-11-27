import numpy as np


class City:
    def __init__(self, x, y):
        self._x_coordinate = x
        self._y_coordinate = y

    def distance(self, city):
        x_difference = abs(self.get_x - city.get_x)
        y_difference = abs(self.get_y - city.get_y)
        y_distance = y_difference
        result = np.sqrt((x_difference**2) + (y_distance**2))
        return result

    @property
    def get_x(self):
        return self._x_coordinate

    @property
    def get_y(self):
        return self._y_coordinate


cit = City(4, 5)
cit2 = City(1, 9)

print(cit.distance(cit2))
