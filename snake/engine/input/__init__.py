from snake.engine.input.ai_input import AIInput
from snake.engine.input.user_input import UserInput
from snake.engine.input.actions import *
from snake.engine.state.game_state import GameState
from snake import AI_MODE


def create_actions_dict(up, down, left, right):
    return dict(
        UP_ACTION=up,
        DOWN_ACTION=down,
        LEFT_ACTION=left,
        RIGHT_ACTION=right
    )


def get_input_handler(config, actions):
    if config["game_mode"] == AI_MODE:
        return AIInput(actions=actions, neural_network=config["neural_network"], state_provider=config["gamestate"])
    return UserInput(actions)
