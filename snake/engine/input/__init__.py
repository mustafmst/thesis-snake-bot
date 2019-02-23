from snake.engine.input.user_input import UserInput
from snake.engine.input.actions import *


def create_actions_dict(up, down, left, right):
    return dict(
        UP_ACTION = up,
        DOWN_ACTION = down,
        LEFT_ACTION = left,
        RIGHT_ACTION = right
    )

def get_input_handler(config, actions):
    return UserInput(actions)