import operator
import random
import numpy as np
import pandas as pd
from fitness import Fitness


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
    result = []
    additional_count = len(pop_ranked) - elite_size
    df = rank_df(pop_ranked)
    for _ in range(0, additional_count):
        result += pick_selection(pop_ranked, df)
    return result


def rank_df(pop_ranked):
    to_percent = 100
    data = np.array(pop_ranked)
    new_df = pd.DataFrame(data, columns=["Index", "Fitness"])
    new_df["cumulative_sum"] = new_df.Fitness.cumsum()
    new_df["cum_percent"] = to_percent * new_df.cumulative_sum / new_df.Fitness.sum()
    return new_df


def pick_selection(pop_ranked, df):
    to_percent = 100
    pick = to_percent * random.random()
    percent_col_num = 3
    for row_num, _ in enumerate(pop_ranked):
        if pick <= df.iat[row_num, percent_col_num]:
            pop_index = [pop_ranked[row_num][0]]
            return pop_index
    return []


def mating_pool(population, selection_results):
    result = []
    for i, _ in enumerate(selection_results):
        index = selection_results[i]
        result.append(population[index])
    return result
