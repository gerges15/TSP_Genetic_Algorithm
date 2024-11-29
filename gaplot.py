import matplotlib.pyplot as plt
from index import next_generation
from population import initial_population
from selection import rank_routes


def genetic_algorithm_plot(
    population, pop_size, elite_size, mutation_rate, generations
):
    pop = initial_population(pop_size, population)
    progress = []
    progress.append(1 / rank_routes(pop)[0][1])

    for _ in range(0, generations):
        pop = next_generation(pop, elite_size, mutation_rate)
        progress.append(1 / rank_routes(pop)[0][1])

    plt.plot(progress)
    plt.ylabel("Distance")
    plt.xlabel("Generation")
    plt.show()
