import random


def breed_population(mating_pool, elite_size):
    children = breed_elitism(mating_pool, elite_size) + generate_children(
        mating_pool, elite_size
    )
    return children


def breed_elitism(mating_pool, elite_size):
    return [mating_pool[i] for i in range(0, elite_size)]


def generate_children(mating_pool, elite_size):
    result = []
    length = len(mating_pool) - elite_size
    pool = random.sample(mating_pool, len(mating_pool))
    for i in range(0, length):
        child = breed(pool[i], pool[len(mating_pool) - i - 1])
        result.append(child)
    return result


def breed(parent1, parent2):
    child = []
    child_p1 = []
    child_p2 = []

    gene_a = int(random.random() * len(parent1))
    gene_b = int(random.random() * len(parent1))

    start_gene = min(gene_a, gene_b)
    end_gene = max(gene_a, gene_b)

    for i in range(start_gene, end_gene):
        child_p1.append(parent1[i])

    child_p2 = [item for item in parent2 if item not in child_p1]

    child = child_p1 + child_p2
    return child
