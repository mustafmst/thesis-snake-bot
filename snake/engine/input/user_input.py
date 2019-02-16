from pygame.locals import *

from snake.engine.input import Input


class UserInput(Input):
    def __init__(self, up_action, down_action, left_action, right_action, escape_action):
        return super().__init__(
            up_action, 
            down_action, 
            left_action, 
            right_action, 
            escape_action)
    
    def handle_events(self):
        keys = pygame.key.get_pressed()
        if (keys[K_RIGHT]):
            self.right()

        if (keys[K_LEFT]):
            self.left()

        if (keys[K_UP]):
            self.up()

        if (keys[K_DOWN]):
            self.down()

        if (keys[K_ESCAPE]):
            self.escape