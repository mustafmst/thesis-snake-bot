class GameState:
    _ui = None
    _board = None
    _player = None
    _moving_action = None

    def __init__(self):
        pass

    def process(self):
        if self._moving_action != None:
            self._moving_action()
        pass

    def render(self):
        pass
