import random
from datetime import datetime
import tensorflow as tf
import gc

from geneticAI.geneticAlgorithm.candidate import Candidate
from geneticAI.geneticAlgorithm.statistics import AlgorithmStatistics


def get_random_specimen(temporary_population):
    return temporary_population.pop(random.randint(0, len(temporary_population) - 1))


class GeneticAlgorithm:
    def __init__(self, run_config):
        self.__config = run_config
        self.__population = []
        self.__new_population = []
        self.__best_network = None
        self.__best_score = (0, 0)
        self._statistic_helper = AlgorithmStatistics(run_config)
        pass

    def __generate_population(self):
        for i in range(self.__config['population_size']):
            self.__population.append(Candidate(self.__config))
        pass

    def __select(self):
        """
            TODO:
            2 factor win rezolution (points and lifetime)
        """
        print("[{}] ==> SELECT STAGE!".format(str(datetime.now())))
        temporary_population = self.__population[:]
        for c in temporary_population:
            c.play_game()
            tf.keras.backend.clear_session()
            gc.collect()

        # [c.play_game() for c in temporary_population]
        result_population = []
        while len(temporary_population) > 1:
            first = get_random_specimen(temporary_population)
            second = get_random_specimen(temporary_population)
            if first.get_score()[0] == second.get_score()[0]:
                if first.get_score()[1] > second.get_score()[1]:
                    winner = first
                else:
                    winner = second
            elif first.get_score()[0] > second.get_score()[0]:
                winner = first
            else:
                winner = second
            if winner.get_score()[0] > self.__best_score[0] and winner.get_score()[1] > self.__best_score[1]:
                self.__best_score = winner.get_score()
                self.__best_network = winner
            result_population.append(winner)
            tf.keras.backend.clear_session()
        self.__population = result_population[:]

    def __cross(self):
        """
            TODO:
            Roulette selection for crossing
        """
        print("[{}] ==> CROSS STAGE!".format(str(datetime.now())))
        temporary_population = self.__population[:]
        self.__new_population = []
        while len(temporary_population) > 1:
            first = get_random_specimen(temporary_population)
            second = get_random_specimen(temporary_population)
            self.__new_population.append(first.cross_with(second))
            self.__new_population.append(second.cross_with(first))
        pass

    def __mutate(self):
        print("[{}] ==> MUTATION STAGE!".format(str(datetime.now())))
        for i in range(self.__config['generation_mutation_rate']):
            get_random_specimen(self.__new_population[:]).mutate()
        self.__population = self.__population + self.__new_population
        pass

    def __log_best_score(self, generation):
        self._statistic_helper.log_generation_result(self.__best_score, generation)
        print('[{}] Best score: {}'.format(generation, self.__best_score))

    def __save_best_network(self):
        self._statistic_helper.save_model(self.__best_network)
        pass

    def run(self):
        """
            TODO:
            save best model for each generation
        """
        self.__generate_population()
        try:
            for i in range(self.__config['generations']):
                print("[{}] ==> Start {} generation".format(str(datetime.now()), i))
                self.__select()
                self.__cross()
                self.__mutate()
                self.__log_best_score(i)
        finally:
            self.__save_best_network()
