from datetime import datetime

import random

from geneticAI.neuralNetworks.network_weights import AVAILABLE_WEIGHTS


def randomize_gene(gene):
    if len(gene.shape) != 1:
        for i in range(len(gene)):
            randomize_gene(gene[i])
    else:
        for i in range(len(gene)):
            gene[i] = random.choice(AVAILABLE_WEIGHTS)
    pass


def randomize_network_weights(genotype):
    print("[{}] Randomizing candidate.".format(str(datetime.now())))

    for i in range(len(genotype)):
        randomize_gene(genotype[i])

    return genotype
