from index import next_generation
from population import initial_population
from selection import rank_routes


def genetic_algorithm(tsp_data):
    pop = initial_population(tsp_data["pop_size"], tsp_data["population"])
    print("Initial distance: " + str(1 / rank_routes(pop)[0][1]))

    for _ in range(0, tsp_data["generations"]):
        pop = next_generation(pop, tsp_data["elite_size"], tsp_data["mutation_rate"])

    print("Final distance: " + str(1 / rank_routes(pop)[0][1]))
    best_route_index = rank_routes(pop)[0][0]
    best_route = pop[best_route_index]
    return best_route
