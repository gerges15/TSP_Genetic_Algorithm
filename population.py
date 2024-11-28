import random


def create_route(city_list):
    route = random.sample(city_list, len(city_list))
    return route


def initial_population(pop_size, city_list):
    population = []

    for _ in range(0, pop_size):
        population.append(create_route(city_list))
    return population


arr = [1, 2, 3, 4, 5, 6]
print(create_route(arr))
print(initial_population(10, arr))
