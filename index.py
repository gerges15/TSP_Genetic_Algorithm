from crossover import breed_population
from mutation import mutate_population
from selection import rank_routes, selection, mating_pool


#! need to refactor make less parameters as you can
def next_generation(current_gen, elite_size, mutation_rate):
    pop_ranked = rank_routes(current_gen)
    selection_results = selection(pop_ranked, elite_size)
    pool_mating = mating_pool(current_gen, selection_results)
    children = breed_population(pool_mating, elite_size)
    result = mutate_population(children, mutation_rate)
    return result
