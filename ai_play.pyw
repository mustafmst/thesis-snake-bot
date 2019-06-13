import os
import argparse

import tensorflow as tf

from geneticAI.config import RUN_CONFIG
from snake.game import Game

parser = argparse.ArgumentParser(description="runs AI playing Snake")
parser.add_argument('-training-file', '-t', help="path to file with training data for snake play")
parser.add_argument('-model-file', '-m', help='path to model .h5 file')
parser.add_argument('-game-config', '-c', help='path to game config data')
args = parser.parse_args()

print(args)


class IllegalArgumentException(ValueError):
    pass


def get_config():
    return RUN_CONFIG["base_game_config"]


def get_network():
    if args.training_file is not None:
        return None
    elif args.model_file is not None:
        return tf.keras.models.load_model(os.path.join(os.getcwd(), args.model_file))
    raise IllegalArgumentException("There is no argument for model load.")


def main():
    config = get_config()
    config["neural_network"] = get_network()
    game = Game(config=RUN_CONFIG["base_game_config"])
    print(game.run())
    pass


if __name__ == '__main__':
    main()
