import sys, time
import pygame
from pygame.locals import *

from snake import DEFAULT_CONFIG, FIELD_SIZE, PLAYER_MODE, SIDE_PANEL_WIDTH
from snake.engine.objects import init_game_objects
from snake.engine.input import get_input_handler, create_actions_dict
from snake.utils.logger import Logger
from snake.utils import logger_levels

BLACK = (0,0,0)

#----------------------------TMP
def up():
    Logger.log_info(message="UP", sender=None)

def down():
    Logger.log_info(message="DOWN", sender=None)

def left():
    Logger.log_info(message="LEFT", sender=None)

def right():
    Logger.log_info(message="RIGHT", sender=None)
#-------------------------------


class Game:

    def __init__(self, config = DEFAULT_CONFIG):
        self._config = config

        self._game_objects = init_game_objects(config)
        self.__event_handler = get_input_handler(config,
            create_actions_dict(up,down,left,right)
        )
        self.__CLOCK = pygame.time.Clock()
        Logger.set_log_level(config["log_level"])
        
        if config["game_mode"] == PLAYER_MODE:
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
        while True:

            self._handle_events()
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
        pygame.quit()
        sys.exit()
    
    def __get_resolution(self, board_size):
        return (
            board_size[0]*FIELD_SIZE + SIDE_PANEL_WIDTH, 
            board_size[1]*FIELD_SIZE
        )
