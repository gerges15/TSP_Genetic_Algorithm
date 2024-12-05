from model.city import generate_city_list
from model.ga import genetic_algorithm

CITY_NUMBERS = 20

tsp_data = {
    "population": generate_city_list(CITY_NUMBERS),
    "pop_size": 100,
    "elite_size": 20,
    "mutation_rate": 0.01,
    "generations": 5,
}

best_rout = genetic_algorithm(tsp_data)
