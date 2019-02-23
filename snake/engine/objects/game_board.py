import pygame

from snake import FIELD_SIZE
from snake.assets import get_absolute_file_path, EMPTY_FIELD
from snake.utils.logger import Logger


class GameBoard():
    def __init__(self, config):
        self.size = config["board_size"]
        self._TILE = pygame.image.load(get_absolute_file_path(EMPTY_FIELD))
        Logger.log_trace(self, "GameBoard initialized")

    def process(self, delta):
        pass

    def render(self, display):
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                display.blit(self._TILE, (x*FIELD_SIZE, y*FIELD_SIZE))
