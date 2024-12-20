import random
import numpy as np


class City:
    _counter = 0

    def __init__(self, x, y):
        self._x_point = x
        self._y_point = y
        City._counter += 1
        self._name = f"C{City._counter}"

    def distance(self, city):
        return np.sqrt(
            (self.square(self.x_difference(city)))
            + (self.square(self.y_difference(city)))
        )

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

    @property
    def get_name(self):
        return self._name

    def square(self, num):
        return num**2


def generate_city_list(num):
    return [City(x=random_position(), y=random_position()) for i in range(num)]


def random_position():
    return int(random.random() * 200)
