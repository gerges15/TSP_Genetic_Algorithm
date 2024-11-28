import operator
from fitness import Fitness


def rank_routes(population):
    fitness_results = {}
    for i, _ in enumerate(population):
        fitness_results[i] = Fitness(population[i]).route_fitness()
    return sorted(fitness_results.items(), key=operator.itemgetter(1), reverse=True)
