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
    print("UP")

def down():
    print("DOWN")

def left():
    print("LEFT")

def right():
    print("RIGHT")
#-------------------------------


class Game:

    def __init__(self, config = DEFAULT_CONFIG):
        self._config = config
        if config["game_mode"] == PLAYER_MODE:
            pygame.init()
            self.DISPLAY = pygame.display.set_mode(
                self.__get_resolution(config["board_size"]))
            pygame.display.set_caption("SNAKE - AI")
        self._game_objects = init_game_objects(config)
        self.__event_handler = get_input_handler(config,
            create_actions_dict(up,down,left,right))
        self.__CLOCK = pygame.time.Clock()
        Logger.set_log_level(logger_levels.DEBUG)

    def run(self):
        self._game_loop()

    def _game_loop(self):
        self.__CLOCK.tick()
        while True:
            self._handle_events()
            self._proces()
            self._render()
            self._sleep()
            self.__CLOCK.tick()
            print("FPS: {}".format(self.__CLOCK.get_fps()))
    
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                Logger.log_debug(self,"Quit event.")
                self._quit()
            self.__event_handler(event)

    def _proces(self):
        pass

    def _render(self):
        self.DISPLAY.fill(BLACK)
        for obj in self._game_objects:
            obj.render(self.DISPLAY)
        pygame.display.flip()
        pass
    
    def _sleep(self):
        time.sleep(self._config["sleep"])

    def _quit(self):
        pygame.quit()
        sys.exit()
    
    def __get_resolution(self, board_size):
        return (
            board_size[0]*FIELD_SIZE + SIDE_PANEL_WIDTH, 
            board_size[1]*FIELD_SIZE)
