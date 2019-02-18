from snake.game import Game


def test_game_init():
    game = Game()
    assert game._running == True