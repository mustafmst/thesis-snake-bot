import pygame
import random

from snake import FIELD_SIZE
from snake.assets import get_absolute_file_path, EMPTY_FIELD, FRUIT
from snake.utils.logger import Logger
from snake.engine.state.game_state import GameState


class GameBoard:
    def __init__(self, config):
        self.size = config["board_size"]
        self.__game_state = config["gamestate"]
        self.__game_state.init_empty_fields(self.size)
        self._TILE = pygame.image.load(
            get_absolute_file_path(EMPTY_FIELD)
        )
        self.__FRUIT_TILE = pygame.image.load(
            get_absolute_file_path(FRUIT)
        )
        self.__fruit_pos = None
        Logger.log_trace(self, "GameBoard initialized")

    def process(self, delta):
        if not self.__game_state.fruit_exist():
            self.__fruit_pos = self.__game_state.add_fruit(
                random.randint(
                    0, self.__game_state.get_empty_fields_count()-1
                )
            )

    def render(self, display):
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                tmp_pos = (x*FIELD_SIZE,y*FIELD_SIZE)
                if tmp_pos != self.__fruit_pos:
                    display.blit(
                        self._TILE, 
                        tmp_pos
                    )
                else:
                    display.blit(
                        self.__FRUIT_TILE, 
                        tmp_pos
                    )
