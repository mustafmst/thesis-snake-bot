from geneticAI.neuralNetworks.random import NeuralNetworkBuilder

from snake import DEFAULT_CONFIG, AI_MODE
from snake.engine.state.game_state import GameState

import numpy as np
# import json

ai_config = dict(DEFAULT_CONFIG)
ai_config["game_mode"] = AI_MODE
GameState.set_game_config(ai_config)
builder = NeuralNetworkBuilder()

test_input = np.array(GameState.get_state())

builder.with_input_shape(test_input.shape)
builder.with_layer('dense', 1)
builder.with_layer('dense', 1)

model = builder.build()

weights = model.get_weights()

weights[1][0] = 100
weights[3][0] = -300

builder2 = NeuralNetworkBuilder()

test_input = np.array(GameState.get_state())

builder2.with_input_shape(test_input.shape)
builder2.with_layer('dense', 1)
builder2.with_layer('dense', 1)

model2 = builder2.build(genotype=weights)

ai_config["neural_network"] = model


from snake.game import Game

if __name__ == '__main__':
    game = Game(config=ai_config)
    game.run()
