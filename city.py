import numpy as np


class City:
    def __init__(self, x, y):
        self._x_point = x
        self._y_point = y

    def distance(self, city):
        y_difference = self.y_difference(city)
        result = np.sqrt(
            (self.square(self.x_difference(city))) + (self.square(y_difference))
        )
        return result

    def x_difference(self, city):
        return abs(self.get_x - city.get_x)

    def y_difference(self, city):
        return abs(self.get_y - city.get_y)

    @property
    def get_x(self):
        return self._x_point

    @property
    def get_y(self):
        return self._y_point

    def square(self, num):
        return num**2


city1 = City(4, 5)
city2 = City(1, 9)
print(city1.distance(city2))
