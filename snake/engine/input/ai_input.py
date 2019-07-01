from snake.engine.input.actions import *
import numpy as np
from snake.utils.logger import Logger
from snake.engine.state.snake_view import get_snake_view

TRANSLATION = {
    0: RIGHT_ACTION,
    1: LEFT_ACTION,
    2: UP_ACTION,
    3: DOWN_ACTION
}

class AIInput:
    def __init__(self, actions, neural_network, state_provider):
        self.__actions = actions
        self.__neural_network = neural_network
        self.__state_provider = state_provider

    def __call__(self):
        move = self.__neural_network.predict(np.array([get_snake_view(self.__state_provider.get_state())]), verbose=0)

        action = TRANSLATION[move.argmax()]
        Logger.log_info(self, 'Action: {}'.format(action))

        self.__actions[action]()
