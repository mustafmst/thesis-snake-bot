from snake.engine.input.actions import *
import numpy as np
from snake.utils.logger import Logger


class AIInput:
    def __init__(self, actions, neural_network, state_provider):
        self.__actions = actions
        self.__neural_network = neural_network
        self.__state_provider = state_provider
        self.__translation = {
            0: RIGHT_ACTION,
            1: LEFT_ACTION,
            2: UP_ACTION,
            3: DOWN_ACTION
        }

    def __call__(self):
        move = self.__neural_network.predict(np.array([self.__state_provider.get_state()]), verbose=0)

        action = self.__translation[move.argmax()]
        Logger.log_info(self, 'Action: {}'.format(action))

        self.__actions[action]()
