from snake.engine.objects.game_board import GameBoard
from snake.engine.objects.player import Player


def init_game_objects(config):
    game_objects = []
    game_objects.append(GameBoard(config))
    game_objects.append(Player(config))
    return game_objects