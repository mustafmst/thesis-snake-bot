import random

from geneticAI.geneticAlgorithm.candidate import Candidate


def get_random_specimen(temporary_population):
    return temporary_population.pop(random.randint(0, len(temporary_population) - 1))


class GeneticAlgorithm:
    def __init__(self, run_config):
        self.__config = run_config
        self.__population = []
        self.__new_population = []
        self.__best_network = None
        self.__best_score = 0
        pass

    def __generate_population(self):
        for i in range(self.__config['population_size']):
            self.__population.append(Candidate(self.__config))
        pass

    def __select(self):
        temporary_population = self.__population[:]
        result_population = []
        while len(temporary_population) > 1:
            first = get_random_specimen(temporary_population)
            second = get_random_specimen(temporary_population)
            if first.get_score() == second.get_score():
                winner = [first, second][random.randint(0, 1)]
            elif first.get_score() > second.get_score():
                winner = first
            else:
                winner = second
            if winner.get_score() > self.__best_score:
                self.__best_score = winner.get_score()
                self.__best_network = winner
            result_population.append(winner)
        self.__population = result_population[:]

    def __cross(self):
        temporary_population = self.__population[:]
        self.__new_population = []
        while len(temporary_population) > 1:
            first = get_random_specimen(temporary_population)
            second = get_random_specimen(temporary_population)
            self.__new_population.append(first.cross_with(second))
            self.__new_population.append(second.cross_with(first))
        pass

    def __mutate(self):
        for i in range(self.__config['generation_mutation_rate']):
            get_random_specimen(self.__new_population[:]).mutate()
        self.__population = self.__population + self.__new_population
        pass

    def __log_best_score(self, generation):
        print('[{}] Best score: {}'.format(generation, self.__best_score))

    """
    Todo:
    """
    def __get_best_network(self):
        pass

    """
    Todo:
    """
    def __save_best_network(self):
        pass

    def run(self):
        self.__generate_population()
        for i in range(self.__config['generations']):
            self.__select()
            self.__cross()
            self.__mutate()
            self.__log_best_score(i)
        self.__save_best_network()
