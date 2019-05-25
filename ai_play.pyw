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
builder.with_dense_layer(124)
builder.with_dense_layer(124)

model = builder.build()

ai_config["neural_network"] = model

# with open('weights.json', 'w') as output:
#     weights = []
#     for i in range(1, len(model.layers)):
#         lw = model.get_layer(index=i).get_weights()
#         weights.append([lw[0].tolist(), lw[1].tolist()])
#     json.dump(weights, output, indent=4)


from snake.game import Game

if __name__ == '__main__':
    game = Game(config=ai_config)
    game.run()
