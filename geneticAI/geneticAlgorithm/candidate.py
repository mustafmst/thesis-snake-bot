from multiprocessing import Process, Queue
import numpy as np

import geneticAI.neuralNetworks.random as randomNN
from snake.game import Game


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
    def __init__(self, config, genotype = None):
        self.__score = None
        self.__config = dict(config)
        self.__create_model()
        pass

    def __create_model(self):
        board_size = self.__config['base_game_config']['board_size']
        input_shape = np.array([[0 for i in range(board_size[0])] for j in range(board_size[1])]).shape
        builder = randomNN.NeuralNetworkBuilder()
        builder.with_input_shape(input_shape)
        for layer in self.__config['network_schema']:
            builder.with_layer(layer[0], layer[1])
        self.__model = builder.build()
        pass

    def __play_game(self):
        game_config = dict(self.__config['base_game_config'])
        game_config["neural_network"] = self.__model
        self.__score = play_game_in_process(game_config)
        pass

    """
    Todo:
    implement real crossing
    """
    def cross_with(self, other):
        return Candidate(other.__config)

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
