from index import next_generation
from population import initial_population
from selection import rank_routes


#! need to refactor make less parameters as you can
def genetic_algorithm(population, pop_size, elite_size, mutation_rate, generations):
    tspData = {"population": population, "pop_size": pop_size}

    return zz_genetic_algorithm(
        pop_size, elite_size, mutation_rate, generations, tspData
    )


def zz_genetic_algorithm(pop_size, elite_size, mutation_rate, generations, tspData):
    pop = initial_population(tspData["pop_size"], tspData["population"])
    print("Initial distance: " + str(1 / rank_routes(pop)[0][1]))

    for _ in range(0, generations):
        pop = next_generation(pop, elite_size, mutation_rate)

    print("Final distance: " + str(1 / rank_routes(pop)[0][1]))
    best_route_index = rank_routes(pop)[0][0]
    best_route = pop[best_route_index]
    return best_route
