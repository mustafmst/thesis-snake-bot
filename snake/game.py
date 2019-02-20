import sys, time
import pygame
from pygame.locals import *

from snake import DEFAULT_CONFIG, FIELD_SIZE, PLAYER_MODE, SIDE_PANEL_WIDTH
from snake.engine.objects import init_game_objects

BLACK = (0,0,0)

class Game:

    def __init__(self, config = DEFAULT_CONFIG):
        self._config = config
        if config["game_mode"] == PLAYER_MODE:
            pygame.init()
            self.DISPLAY = pygame.display.set_mode(
                self.__get_resolution(config["board_size"]))
            pygame.display.set_caption("SNAKE - AI")
        self._game_objects = init_game_objects(config)

    def run(self):
        self._game_loop()

    def _game_loop(self):
        while True:
            self._handle_events()
            self._proces()
            self._render()
            self._sleep()
    
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                print("[{}] Quit event.".format(time.ctime()))
                self._quit()

    def _proces(self):
        print("[{}] Proces.".format(time.ctime()))
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
