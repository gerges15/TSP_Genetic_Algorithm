from model.city import generate_city_list
from model.ga import genetic_algorithm


tsp_data = {
    "population": generate_city_list(20),
    "pop_size": 100,
    "elite_size": 2,
    "mutation_rate": 0.01,
    "generations": 500,
}

genetic_algorithm(tsp_data)
