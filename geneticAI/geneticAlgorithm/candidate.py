import numpy as np

import geneticAI.neuralNetworks.random as NN
from snake.game import Game
from geneticAI.geneticAlgorithm.crossing_handler import cross_candidates


def game_function(config, genotype):
    game_config = config['base_game_config']
    game_config["neural_network"] = create_model(config, genotype)
    game = Game(game_config)
    result = game.run()
    return result


def create_model(config, genotype):
    board_size = config['base_game_config']['board_size']
    input_shape = np.array([[0 for i in range(board_size[0])] for j in range(board_size[1])]).shape
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
        if self.__genotype is None:
            self.__genotype = create_model(self.__config, self.__genotype).get_weights()
        pass

    def get_genotype(self):
        return self.__genotype

    def __play_game(self):
        game_config = dict(self.__config)
        self.__score = game_function(game_config, self.__genotype)
        pass

    def cross_with(self, other):
        genotype = cross_candidates(self.__genotype, other.get_genotype())
        return Candidate(self.__config, genotype)

    """
    Todo
    """

    def mutate(self):
        self.__score = None
        pass

    def get_score(self):
        if self.__score is None:
            self.__play_game()
        return self.__score
