from pygame import image

from snake.assets import get_absolute_file_path, SNAKE_HEAD
from snake.utils.logger import Logger
from snake import FIELD_SIZE


class Player:
    def __init__(self, config):
        self.__board_size = config["board_size"]
        self.__move_sleep = config["move_sleep"]
        self.__position = (0, 0)
        self.__direction = (1,0)
        self.__ellapsed_from_move = 0
        self.__TILE = image.load(get_absolute_file_path(SNAKE_HEAD))
        Logger.log_trace(self, "Player initialized")
    
    def process(self, delta):
        self.__ellapsed_from_move = self.__ellapsed_from_move + delta
        if self.__ellapsed_from_move > self.__move_sleep:
            self.__ellapsed_from_move = 0
            self.move(
                self.__direction[0],
                self.__direction[1]
            )

    def move(self, x, y):
        self.__position = (
            self.__position[0] + x * FIELD_SIZE, 
            self.__position[1] + y * FIELD_SIZE
        )

    def up(self):
        self.__direction = ( 0,-1)

    def down(self):
        self.__direction = ( 0, 1)

    def left(self):
        self.__direction = (-1, 0)

    def right(self):
        self.__direction = ( 1, 0)

    def render(self, display):
        display.blit(self.__TILE, self.__position)
