from pygame import image

from snake.assets import get_absolute_file_path, SNAKE_BODY
from snake.engine.state.game_state import GameState


class Tail:
    def __init__(self, player):
        self.__player = player
        self.__tail_blocks = [player.get_position()]
        self.__newest_block = player.get_position()
        self.__TILE = image.load(get_absolute_file_path(SNAKE_BODY))
        pass

    def process(self, delta):
        if self.__newest_block != self.__player.get_position():
            GameState.take_up_field(self.__newest_block)
            new_pos = self.__player.get_position()
            self.__tail_blocks.append(new_pos)
            self.__newest_block = new_pos
            is_eating = GameState.is_eating()
            if not is_eating:
                GameState.release_field(self.__tail_blocks.pop(0))
            else:
                GameState.finish_eating()
        pass

    def render(self, display):
        for body_element in self.__tail_blocks:
            if body_element is not self.__newest_block:
                display.blit(
                    self.__TILE,
                    body_element
                )
        pass
