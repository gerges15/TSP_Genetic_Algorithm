import matplotlib.pyplot as plt
from index import next_generation
from population import initial_population
from selection import rank_routes


def genetic_algorithm_plot(tsp_data):
    pop = initial_population(tsp_data["pop_size"], tsp_data["population"])
    progress = []
    progress.append(1 / rank_routes(pop)[0][1])

    for _ in range(0, tsp_data["generations"]):
        pop = next_generation(pop, tsp_data["elite_size"], tsp_data["mutation_rate"])
        progress.append(1 / rank_routes(pop)[0][1])

    plt.plot(progress)
    plt.ylabel("Distance")
    plt.xlabel("Generation")
    plt.show()


def improved_generations(pop, tsp_data):
    for _ in range(0, tsp_data["generations"]):
        pop = next_generation(pop, tsp_data["elite_size"], tsp_data["mutation_rate"])
    return pop
