from datetime import datetime

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
            new_gene = gene_one.copy()
            for i in range(crossing_point, len(gene_two)-1):
                new_gene[i] = gene_two[i]
        else:
            new_gene = gene_two.copy()
            for i in range(crossing_point, len(gene_one)-1):
                new_gene[i] = gene_one[i]
    return new_gene


def cross_candidates(first, second):
    print("[{}] Crossing two candidates!".format(str(datetime.now())))
    genotype_one = first
    genotype_two = second
    if len(genotype_one) != len(genotype_two):
        raise CrossingException("Whole genotype size mismatch")

    new_genotype = []

    for i in range(len(genotype_one)):
        new_genotype.append(cross_gene(genotype_one[i], genotype_two[i]))

    return new_genotype
