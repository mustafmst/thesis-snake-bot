from geneticAI.geneticAlgorithm.candidate import Candidate
from geneticAI.config import RUN_CONFIG
import numpy as np


def main():
    a = Candidate(RUN_CONFIG)
    b = Candidate(RUN_CONFIG)
    a.get_genotype()
    b.get_genotype()

    c = a.cross_with(b)

    w = c.get_genotype()
    c.get_score()


if __name__ == '__main__':
    main()
