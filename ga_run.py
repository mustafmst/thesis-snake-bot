from geneticAI.config import RUN_CONFIG
from geneticAI.geneticAlgorithm.algorithm import GeneticAlgorithm


def main():
    algorithm = GeneticAlgorithm(RUN_CONFIG)
    algorithm.run()
    pass


if __name__ == '__main__':
    main()
