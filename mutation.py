import random


def mutate(individual, mutation_rate):
    for swapped, _ in enumerate(individual):
        if random.random() < mutation_rate:
            swap_within(individual, swapped)
    return individual


def swap_within(individual, swapped_index):
    swap_with = int(random.random() * len(individual))

    city1 = individual[swapped_index]
    city2 = individual[swap_with]

    individual[swapped_index], individual[swap_with] = city2, city1


indiv = ["a", "b", "c", "d"]
mr = 0.24
print(mutate(indiv, mr))
