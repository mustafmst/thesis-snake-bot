from pygame.locals import *

from snake.engine.input.actions import *


class UserInput:
    def __init__(self, actions):
        self.__actions = actions

    def __call__(self, event):
        if event.type == KEYDOWN:
            action = None
            if event.key == K_RIGHT:
                action = RIGHT_ACTION
            if event.key == K_LEFT:
                action = LEFT_ACTION
            if event.key == K_UP:
                action = UP_ACTION
            if event.key == K_DOWN:
                action = DOWN_ACTION
            if action is not None:
                self.__actions[action]()
