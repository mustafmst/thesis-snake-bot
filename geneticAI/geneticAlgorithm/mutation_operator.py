import copy, random


def _mutate_gene(gene):
    """
        TODO:
        change functionality to operate only in range of values (-1, 1)
    """
    selection = random.randint(0, gene.shape[0] - 1)
    if len(gene.shape) != 1:
        _mutate_gene(gene[selection])
    else:
        gene[selection] = -gene[selection]


def mutate_genotype(genotype):
    new_genotype = copy.deepcopy(genotype)
    selection = random.randint(0, len(new_genotype) - 1)
    _mutate_gene(new_genotype[selection])
    return new_genotype
