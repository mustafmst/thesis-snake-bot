import os
import sys

import tensorflow as tf

from geneticAI.config import RUN_CONFIG
from snake.game import Game


def main():
    config = RUN_CONFIG["base_game_config"]
    config["neural_network"] = tf.keras.models.load_model(os.path.join(os.getcwd(), sys.argv[1]))
    game = Game(config=RUN_CONFIG["base_game_config"])
    print(game.run())
    pass


if __name__ == '__main__':
    main()
