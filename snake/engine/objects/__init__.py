from snake.engine.objects.game_board import GameBoard
from snake.engine.objects.player import Player


class PlayerSingleton:
    player = None

def get_player(config = None):
    if PlayerSingleton.player == None:
        PlayerSingleton.player = Player(config)
    return PlayerSingleton.player

class GameBoardSingleton:
    board = None

def get_board(config = None):
    if GameBoardSingleton.board == None:
        GameBoardSingleton.board = GameBoard(config)
    return GameBoardSingleton.board

def init_game_objects(config):
    game_objects = []
    game_objects.append(get_board(config))
    game_objects.append(get_player(config))
    return game_objects