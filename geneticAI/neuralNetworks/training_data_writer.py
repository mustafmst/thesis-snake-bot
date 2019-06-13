import json
import os
from datetime import datetime

from snake.engine.input.ai_input import TRANSLATION
from snake.engine.input.actions import *


def get_action(x, y):
    if x == 1:
        return RIGHT_ACTION
    elif x == -1:
        return LEFT_ACTION
    else:
        if y == 1:
            return DOWN_ACTION
        elif y == -1:
            return UP_ACTION


class TrainingDataWriter:
    def __init__(self, config):
        self.__config = config
        self.__game_state = self.__config["gamestate"]
        self.__session_data = []

    def write_data(self, x, y):
        action = get_action(x, y)
        input = self.__game_state.get_state()
        output = [0, 0, 0, 0]
        pos = next(i[0] for i in TRANSLATION.items() if i[1] is action)
        output[pos] = 100
        data = (input, output)
        self.__session_data.append(data)
        with open(
                os.path.join(os.getcwd(), "{}-{}.json".format(datetime.now().strftime("%Y%m%d:%H:%M"), "training")),
                'w') as training_json:
            json.dump(dict(
                board=self.__config["board_size"],
                data=self.__session_data
            ), training_json, indent=4)
        pass
