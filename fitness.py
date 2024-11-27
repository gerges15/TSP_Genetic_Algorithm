from city import City


class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0.0

    def route_distance(self):
        return self.zz_route_distance()

    def zz_route_distance(self):
        if self.distance == 0:
            path_distance = 0
            for i, city in enumerate(self.route):
                from_city = city
                next_index = i + 1
                to_city = self.to_city(next_index, self.route)
                path_distance += from_city.distance(to_city)
            self.distance = path_distance
        return self.distance

    def to_city(self, next_index, route):
        to_city = None
        if next_index < len(route):
            to_city = self.route[next_index]
        if next_index == len(route):
            to_city = self.route[0]
        return to_city

    def route_fitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.route_distance())
        return self.fitness


city1 = City(1, 5)
city2 = City(4, 9)
city3 = City(7, 8)
city4 = City(3, 1)

fitt = Fitness([city1, city2, city3, city4])

print(fitt.route_distance())
print(fitt.route_fitness())
