import random
from city import City
from ga import genetic_algorithm


cityList = []
CITY_NUMBERS = 20
for i in range(0, CITY_NUMBERS):
    cityList.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))

genetic_algorithm(
    population=cityList,
    pop_size=100,
    elite_size=20,
    mutation_rate=0.01,
    generations=500,
)
