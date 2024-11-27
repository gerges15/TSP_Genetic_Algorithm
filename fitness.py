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
            for i in range(0, len(self.route)):
                from_city = self.route[i]
                to_city = None
                if i + 1 < len(self.route):
                    to_city = self.route[i + 1]
                else:
                    to_city = self.route[0]
                path_distance += from_city.distance(to_city)
            self.distance = path_distance
        return self.distance

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
