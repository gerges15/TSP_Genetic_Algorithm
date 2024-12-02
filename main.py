from city import generate_city_list
from ga import genetic_algorithm

CITY_NUMBERS = 20
cityList = generate_city_list(CITY_NUMBERS)

tsp_data = {
    "population": cityList,
    "pop_size": 100,
    "elite_size": 20,
    "mutation_rate": 0.01,
    "generations": 50,
}

best_rout = genetic_algorithm(tsp_data)
