from snake.engine.objects.game_board import GameBoard
from snake.engine.objects.player import Player
from snake.engine.objects.tail import Tail


def init_game_objects(config):
    board = GameBoard(config)
    player = Player(config)
    tail = Tail(config, player)
    game_objects = [
        board, player, tail
    ]
    return game_objects
