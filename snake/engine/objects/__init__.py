from snake.engine.objects.game_board import GameBoard
from snake.engine.objects.player import Player


class PlayerSingleton:
    player = None

def get_player(config = None):
    if PlayerSingleton.player == None:
        PlayerSingleton.player = Player(config)
    return PlayerSingleton.player

def init_game_objects(config):
    game_objects = []
    game_objects.append(GameBoard(config))
    game_objects.append(get_player(config))
    return game_objects