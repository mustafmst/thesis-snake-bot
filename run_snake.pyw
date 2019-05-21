from snake.game import Game


if __name__ == '__main__':
    game = Game()
    points = game.run()
    print('Score: {}'.format(points))
