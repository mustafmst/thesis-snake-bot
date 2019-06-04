import numpy as np
import random


class CrossingException(Exception):
    def __int__(self, value):
        self.__value = value

    def __str__(self):
        return 'Error during gene crossing: {}'.format(self.__value)


def cross_gene(gene_one: np.ndarray, gene_two: np.ndarray) -> np.ndarray:
    if gene_one.shape != gene_two.shape:
        raise CrossingException("Gene shape mismatch")
    new_gene = gene_one.copy()
    if len(gene_one.shape) != 1:
        for i in range(gene_one.shape[0]):
            new_gene[i] = cross_gene(gene_one[i], gene_two[i])
    else:
        crossing_point = random.randint(0, gene_one.shape[0])
        if random.randint(0,100) > 50:
            first_half = gene_one[0:crossing_point]
            second_half = gene_two[crossing_point:len(gene_two)]
        else:
            first_half = gene_two[0:crossing_point]
            second_half = gene_one[crossing_point:len(gene_one)]
        new_gene = np.concatenate((first_half, second_half))

    return new_gene


def cross_candidates(first, second):
    print("Crossing!")
    genotype_one = first.get_genotype()
    genotype_two = second.get_genotype()
    if len(genotype_one) != len(genotype_two):
        raise CrossingException("Whole genotype size mismatch")

    new_genotype = []

    for i in range(len(genotype_one)):
        new_genotype.append(cross_gene(genotype_one[i], genotype_two[i]))

    return new_genotype
