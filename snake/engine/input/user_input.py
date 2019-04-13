from pygame.locals import *

from snake.engine.input.actions import *


class UserInput:
    def __init__(self, actions):
        self.__actions = actions

    def __call__(self, event):
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                self.__actions[RIGHT_ACTION]()

            if event.key == K_LEFT:
                self.__actions[LEFT_ACTION]()

            if event.key == K_UP:
                self.__actions[UP_ACTION]()

            if event.key == K_DOWN:
                self.__actions[DOWN_ACTION]()