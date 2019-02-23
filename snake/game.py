import sys, time
import pygame
from pygame.locals import *

from snake import DEFAULT_CONFIG, FIELD_SIZE, PLAYER_MODE, SIDE_PANEL_WIDTH
from snake.engine.objects import init_game_objects, get_player
from snake.engine.input import get_input_handler, create_actions_dict
from snake.utils.logger import Logger
from snake.utils import logger_levels
from snake.engine.state.game_state import GameState


BLACK = (0,0,0)

class Game:

    def __init__(self, config = DEFAULT_CONFIG):
        Logger.set_log_level(config["log_level"])
        self.__running = True
        self._config = config

        self._game_objects = init_game_objects(config)
        self.__player = get_player(config)
        self.__CLOCK = pygame.time.Clock()
        
        if config["game_mode"] == PLAYER_MODE:
            self.__event_handler = get_input_handler(config,
                create_actions_dict(
                    self.__player.up,
                    self.__player.down,
                    self.__player.left,
                    self.__player.right
                )
            )
            pygame.init()
            self.DISPLAY = pygame.display.set_mode(
                self.__get_resolution(config["board_size"])
            )
            pygame.display.set_caption("SNAKE - AI")
        Logger.log_trace(self, "Game initialized")

    def run(self):
        Logger.log_trace(self, "Starting game")
        self._game_loop()

    def _game_loop(self):
        self.__CLOCK.tick()
        while self.__running:
            self._handle_events()
            if not GameState.is_game_finished():
                if not self.__running:
                    continue
                self._proces(self.__CLOCK.get_rawtime())
                self._render()

                self.__CLOCK.tick()
                Logger.log_fps(self, self.__CLOCK)
    
    def _handle_events(self):
        for event in pygame.event.get():

            if event.type == QUIT:
                Logger.log_debug(self,"Quit event.")
                self._quit()

            self.__event_handler(event)

    def _proces(self, delta):
        for obj in self._game_objects:
            obj.process(delta)
        pass

    def _render(self):
        self.DISPLAY.fill(BLACK)

        for obj in self._game_objects:
            obj.render(self.DISPLAY)
        
        pygame.display.flip()
        pass

    def _quit(self):
        self.__running = False
        pygame.quit()
    
    def __get_resolution(self, board_size):
        return (
            board_size[0]*FIELD_SIZE + SIDE_PANEL_WIDTH, 
            board_size[1]*FIELD_SIZE
        )
