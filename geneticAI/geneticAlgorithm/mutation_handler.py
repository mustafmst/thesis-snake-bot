import copy, random


def _mutate_gene(gene):
    selection = random.randint(0, gene.shape[0] - 1)
    if len(gene.shape) != 1:
        _mutate_gene(gene[selection])
    else:
        mutation_strength = round(random.random() - 0.5, 2)
        gene[selection] = gene[selection] + mutation_strength


def mutate_genotype(genotype):
    new_genotype = copy.deepcopy(genotype)
    selection = random.randint(0, len(new_genotype) - 1)
    _mutate_gene(new_genotype[selection])
    return new_genotype
