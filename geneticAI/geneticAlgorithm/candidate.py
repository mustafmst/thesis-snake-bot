import numpy as np
from datetime import datetime

import geneticAI.neuralNetworks.random as NN
from geneticAI.geneticAlgorithm.mutation_handler import mutate_genotype
from snake.game import Game
from geneticAI.geneticAlgorithm.crossing_handler import cross_candidates


def game_function(config, model):
    game_config = config['base_game_config']
    game_config["neural_network"] = model
    game = Game(game_config)
    result = game.run()
    return result


def create_model(config, genotype):
    # board_size = config['base_game_config']['board_size']
    # input_shape = np.array([[0 for i in range(board_size[0])] for j in range(board_size[1])]).shape
    input_shape = np.array([[0 for j in range(8)] for i in range(3)]).shape
    builder = NN.NeuralNetworkBuilder()
    builder.with_input_shape(input_shape)
    for layer in config['network_schema']:
        builder.with_layer(layer[0], layer[1])
    return builder.build(genotype=genotype)


class Candidate:
    def __init__(self, config, genotype=None):
        self.__score = None
        self.__config = dict(config)
        self.__genotype = genotype
        self.__model = None
        print("[{}] Candidate is created!".format(str(datetime.now())))
        pass

    def get_genotype(self):
        return self.__genotype

    def play_game(self):
        print("[{}] Candidate is playing!".format(str(datetime.now())))
        try:
            self.initiate_model()
            game_config = dict(self.__config)
            self.__score = game_function(game_config, self.__model)
        finally:
            del self.__model
        pass

    def initiate_model(self):
        if self.__genotype is None:
            self.__model = create_model(self.__config, self.__genotype)
            self.__genotype = self.__model.get_weights()
        else:
            self.__model = create_model(self.__config, self.__genotype)

    def cross_with(self, other):
        genotype = cross_candidates(self.__genotype, other.get_genotype())
        return Candidate(self.__config, genotype)

    def save_model(self, file_name):
        self.initiate_model()
        self.__model.save(file_name)
        pass

    def mutate(self):
        print("[{}] Candidate is mutating!".format(str(datetime.now())))
        self.__score = None
        self.__genotype = mutate_genotype(self.__genotype)
        pass

    def get_score(self):
        if self.__score is None:
            self.play_game()
        return self.__score
