from model.generations import next_generation
from model.population import initial_population
from model.selection import rank_routes


def genetic_algorithm(tsp_data):
    pop = initial_population(tsp_data["pop_size"], tsp_data["population"])
    initial_dist = best_distance(pop)
    print("Initial distance: " + str(initial_dist))

    pop = improved_generations(pop, tsp_data)

    final_dist = best_distance(pop)
    print("Final distance: " + str(final_dist))
    best_route_index = rank_routes(pop)[0][0]
    best_route = pop[best_route_index]
    return best_route, final_dist


def improved_generations(pop, tsp_data):
    for _ in range(0, tsp_data["generations"]):
        pop = next_generation(pop, tsp_data["elite_size"], tsp_data["mutation_rate"])
    return pop


def best_distance(pop):
    return 1 / rank_routes(pop)[0][1]
