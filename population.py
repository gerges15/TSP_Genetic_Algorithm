import random


def create_route(city_list):
    return random.sample(city_list, len(city_list))


def initial_population(pop_size, city_list):
    population = []

    for _ in range(0, pop_size):
        population.append(create_route(city_list))
    return population
