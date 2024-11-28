import operator
from fitness import Fitness
from city import City
from population import initial_population


def rank_routes(population):
    list_of_tuples = fitness_results(population).items()
    return sorted(list_of_tuples, key=operator.itemgetter(1), reverse=True)


def fitness_results(population):
    results = {}
    for i, _ in enumerate(population):
        results[i] = Fitness(population[i]).route_fitness()
    return results


city1 = City(3, 5)
city2 = City(3, 6)
city3 = City(23, 5)
city4 = City(8, 65)
city5 = City(35, 25)

cityList = [city1, city2, city3, city4, city5]
pop = initial_population(10, cityList)
print(rank_routes(pop))
