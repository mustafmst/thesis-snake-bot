from snake.engine.objects.game_board import GameBoard


def init_game_objects(config):
    game_objects = []
    game_objects.append(GameBoard(config))
    return game_objects