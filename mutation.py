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


indiv = ["a", "b", "c", "d"]
mr = 0.24
print(apply_mutation(indiv, mr))
