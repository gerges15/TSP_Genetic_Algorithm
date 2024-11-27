from city import City


class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0.0

    def zx_route_distance(self):
        self.distance = self.path_distance if self.distance == 0 else self.distance
        return self.distance

    @property
    def path_distance(self):
        result = 0
        for i, from_city in enumerate(self.route):
            next_index = i + 1
            to_city = self.next_city(next_index, self.route)
            result += from_city.distance(to_city)
        return result

    def next_city(self, next_index, route):
        result = None
        if next_index < len(route):
            result = self.route[next_index]
        if next_index == len(route):
            result = self.route[0]
        return result

    def route_fitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.zx_route_distance())
        return self.fitness


city1 = City(1, 5)
city2 = City(4, 9)
city3 = City(7, 8)
city4 = City(3, 1)

fitt = Fitness([city1, city2, city3, city4])

print(fitt.zx_route_distance())
print(fitt.route_fitness())
