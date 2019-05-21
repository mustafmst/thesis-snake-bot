from snake.engine.objects.game_board import GameBoard
from snake.engine.objects.player import Player
from snake.engine.objects.tail import Tail


class PlayerSingleton:
    player = None


def get_player(config=None):
    if PlayerSingleton.player is None:
        PlayerSingleton.player = Player(config)
    return PlayerSingleton.player


class GameBoardSingleton:
    board = None


def get_board(config=None):
    if GameBoardSingleton.board is None:
        GameBoardSingleton.board = GameBoard(config)
    return GameBoardSingleton.board

class TailSingleton:
    tail = None

def get_tail(player):
    if TailSingleton.tail is None:
        TailSingleton.tail = Tail(player)
    return TailSingleton.tail


def init_game_objects(config):
    game_objects = [
        get_board(config),
        get_player(config),
        get_tail(get_player(config))
    ]
    return game_objects
