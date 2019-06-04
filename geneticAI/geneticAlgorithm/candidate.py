from multiprocessing import Process, Queue
from keras.models import Model
import numpy as np
import random

import geneticAI.neuralNetworks.random as randomNN
from snake.game import Game
from geneticAI.geneticAlgorithm.crossing_handler import cross_candidates


def game_function(queue, config):
    game = Game(config)
    result = game.run()
    queue.put(result)


def play_game_in_process(config):
    q = Queue()
    p = Process(target=game_function, args=(q, config))
    p.start()
    p.join()
    return q.get()


class Candidate:
    """
    Todo:
    implement creating model based on configurations
    """
    def __init__(self, config, genotype=None):
        self.__score = None
        self.__config = dict(config)
        self.__genotype = genotype
        self.__create_model()
        pass

    def get_genotype(self):
        return self.__model.get_weights()

    def __create_model(self):
        board_size = self.__config['base_game_config']['board_size']
        input_shape = np.array([[0 for i in range(board_size[0])] for j in range(board_size[1])]).shape
        builder = randomNN.NeuralNetworkBuilder()
        builder.with_input_shape(input_shape)
        for layer in self.__config['network_schema']:
            builder.with_layer(layer[0], layer[1])
        self.__model: Model = builder.build(genotype=self.__genotype)
        # a = self.__model.get_weights()
        pass

    def __play_game(self):
        game_config = dict(self.__config['base_game_config'])
        game_config["neural_network"] = self.__model
        self.__score = play_game_in_process(game_config)  # random.randint(0, 100)
        pass

    """
    Todo:
    implement real crossing
    """
    def cross_with(self, other):
        genotype = cross_candidates(self, other)
        return Candidate(self.__config, genotype)

    """
    Todo
    """
    def mutate(self):
        self.__score = None
        pass

    def get_score(self):
        #if self.__score is None:
        try:
            self.__play_game()
        except KeyboardInterrupt:
            print("znowu...")
        return self.__score
