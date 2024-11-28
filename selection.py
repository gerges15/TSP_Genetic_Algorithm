import operator
import random
import numpy as np
import pandas as pd
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


def selection(pop_ranked, elite_size):
    result = apply_elitism(elite_size, pop_ranked) + apply_roulette_wheel(
        elite_size, pop_ranked
    )
    return result


def apply_elitism(elite_size, pop_ranked):
    return [pop_ranked[i][0] for i in range(elite_size)]


def apply_roulette_wheel(elite_size, pop_ranked):
    to_percent = 100
    result = []
    df = rank_df(pop_ranked)
    for i in range(0, len(pop_ranked) - elite_size):
        pick = to_percent * random.random()
        for row, _ in enumerate(pop_ranked):
            # i => row and iat[row, column] where 3 is a percent column
            if pick <= df.iat[row, 3]:
                # index => pop_ranked[i][0]
                result.append(pop_ranked[row][0])
                break
    return result


def rank_df(pop_ranked):
    to_percent = 100
    data = np.array(pop_ranked)
    new_df = pd.DataFrame(data, columns=["Index", "Fitness"])
    new_df["cumulative_sum"] = new_df.Fitness.cumsum()
    new_df["cum_percent"] = to_percent * new_df.cumulative_sum / new_df.Fitness.sum()
    return new_df


city1 = City(3, 5)
city2 = City(3, 6)
city3 = City(23, 5)
city4 = City(8, 65)
city5 = City(35, 25)

cityList = [city1, city2, city3, city4, city5]
pop = initial_population(10, cityList)
ranked = rank_routes(pop)
print(ranked)
print(selection(ranked, 3))
