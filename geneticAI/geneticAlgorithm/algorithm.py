class GeneticAlgorithm:
    def __init__(self, run_config):
        self.__config = run_config
        self.__population = []
        pass

    def __generate_population(self):
        pass

    def __select(self):
        pass

    def __cross(self):
        pass

    def __mutate(self):
        pass

    def __log_best_score(self, generation):
        pass

    def __get_best_network(self):
        pass

    def __save_best_network(self):
        pass

    def run(self):
        self.__generate_population()
        for i in range(self.__config.generations):
            self.__select()
            self.__cross()
            self.__mutate()
            self.__log_best_score(i)
        self.__save_best_network()
