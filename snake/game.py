import pygame
from pygame.locals import *

from snake import DEFAULT_CONFIG, get_resolution, PLAYER_MODE, AI_MODE, DISPLAY_ON
from snake.engine.input import get_input_handler, create_actions_dict
from snake.engine.objects import init_game_objects, Player
from snake.engine.state.game_state import GameState
from snake.utils.logger import Logger

BLACK = (0, 0, 0)


class Game:

    def __init__(self, config=DEFAULT_CONFIG):
        self.__game_state = GameState()
        Logger.set_log_level(config["log_level"])
        self.__running = True
        self.__config = config
        self.__config["gamestate"] = self.__game_state
        self.__game_state.set_game_config(config)

        self._game_objects = init_game_objects(config)
        self.__player = next(o for o in self._game_objects if type(o) is Player)
        self.__CLOCK = pygame.time.Clock()

        self.__event_handler = get_input_handler(config,
                                                 create_actions_dict(
                                                     self.__player.up,
                                                     self.__player.down,
                                                     self.__player.left,
                                                     self.__player.right
                                                 )
                                                 )
        if self.__config['display_mode'] == DISPLAY_ON:
            pygame.init()
            self.DISPLAY = pygame.display.set_mode(
                get_resolution(config["board_size"])
            )
            pygame.display.set_caption("SNAKE - AI")
        Logger.log_trace(self, "Game initialized")

    def run(self):
        """
            TODO:
            return tuple with points and lifetime
        """
        Logger.log_trace(self, "Starting game")
        # noinspection PyBroadException
        try:
            self.__game_loop()
        except Exception as e:
            print('Error while playing')
            print(e)
            raise
            self.__quit()
        finally:
            self.clear_all()
        return self.__game_state.get_points()

    def __game_loop(self):
        self.__CLOCK.tick()
        while self.__running:
            self.__handle_events()
            if not self.__game_state.is_game_finished():
                if not self.__running:
                    continue
                self.__process(self.__CLOCK.get_rawtime())
                if self.__config['display_mode'] == DISPLAY_ON:
                    self.__render()

                self.__CLOCK.tick()
                Logger.log_fps(self, self.__CLOCK)
            else:
                self.__quit()

    def __handle_events(self):
        if self.__config["game_mode"] == AI_MODE:
            Logger.log_debug(self, "Handle AI event")
            self.__event_handler()
        if self.__config['display_mode'] == DISPLAY_ON:
            for event in pygame.event.get():

                if event.type == QUIT:
                    Logger.log_debug(self, "Quit event.")
                    self.__quit()

                if self.__config["game_mode"] == PLAYER_MODE:
                    self.__event_handler(event)

    def __process(self, delta):
        for obj in self._game_objects:
            obj.process(delta)
        pass

    def __render(self):
        self.DISPLAY.fill(BLACK)

        for obj in self._game_objects:
            obj.render(self.DISPLAY)

        pygame.display.flip()
        pass

    def __quit(self):
        self.__running = False
        pygame.quit()

    def clear_all(self):
        for o in self._game_objects:
            del o
