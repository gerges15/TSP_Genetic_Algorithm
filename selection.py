import operator
from fitness import Fitness


def rank_routes(population):
    list_of_tuples = fitness_results(population).items()
    return sorted(list_of_tuples, key=operator.itemgetter(1), reverse=True)


def fitness_results(population):
    results = {}
    for i, _ in enumerate(population):
        results[i] = Fitness(population[i]).route_fitness()
    return results
