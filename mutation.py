import random


def apply_mutation(chromosome, mutation_rate):
    for gene_index, _ in enumerate(chromosome):
        if random.random() < mutation_rate:
            swap_genes(chromosome, gene_index)
    return chromosome


def swap_genes(chromosome, gene_index):
    random_index = int(random.random() * len(chromosome))

    gene1 = chromosome[gene_index]
    gene2 = chromosome[random_index]
    chromosome[gene_index], chromosome[random_index] = gene2, gene1


def mutate_population(population, mutation_rate):
    mutated_pop = []

    for ind, _ in enumerate(population):
        mutated_ind = apply_mutation(population[ind], mutation_rate)
        mutated_pop.append(mutated_ind)
    return mutated_pop
