import numpy as np
from datetime import datetime
import uuid

import geneticAI.neuralNetworks.random as NN
from geneticAI.geneticAlgorithm.mutation_operator import mutate_genotype
from snake.game import Game
from geneticAI.geneticAlgorithm.crossing_operator import cross_candidates
from geneticAI.geneticAlgorithm.randomize_operator import randomize_network_weights


def get_better_score(first, second):
    if first[0] == second[0]:
        if first[1] > second[1]:
            winner = first
        else:
            winner = second
    elif first[0] > second[0]:
        winner = first
    else:
        winner = second
    return winner


def game_function(config, model):
    game_config = config['base_game_config']
    game_config["neural_network"] = model
    game = Game(game_config)
    result = game.run()
    return result


def create_model(config, genotype):
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
        self.ID = uuid.uuid1()
        pass

    def are_same(self, other):
        return self.ID is other.ID

    def get_genotype(self):
        return self.__genotype

    def play_game(self):
        print("[{}] Candidate is playing!".format(str(datetime.now())))
        try:
            self.initiate_model()
            game_config = dict(self.__config)
            new_score = game_function(game_config, self.__model)
            if self.__score is None:
                self.__score = new_score
            self.__score = get_better_score(self.__score, new_score)
            print("[{}] Got score: {}".format(str(datetime.now()), self.__score))
        finally:
            del self.__model
        pass

    def initiate_model(self):
        if self.__genotype is None:
            self.__model = create_model(self.__config, self.__genotype)
            self.__genotype = randomize_network_weights(self.__model.get_weights())
            self.__model.set_weights(self.__genotype)
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

    def fitness(self):
        result = self.__score[0]
        if self.__score[1] > 50:
            result += 1
        return result

    def get_score(self):
        if self.__score is None:
            self.play_game()
        return self.__score
