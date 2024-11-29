class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0.0

    def route_fitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.route_distance)
        return self.fitness

    @property
    def route_distance(self):
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
