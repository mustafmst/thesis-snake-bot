from snake.utils.logger import Logger
from snake import FIELD_SIZE


class GameState:
    __points = 0
    __has_finished = False
    __empty_fields = set()
    __empty_fields_count = 0

    @staticmethod
    def init_empty_fields(size):
        for x in range(size[0]):
            for y in range(size[1]):
                GameState.__empty_fields.add(
                    (x*FIELD_SIZE, y*FIELD_SIZE)
                )
                GameState.__empty_fields_count = GameState.__empty_fields_count + 1

    @staticmethod
    def take_up_field(field):
        GameState.__empty_fields.remove(field)
        GameState.__empty_fields_count = GameState.__empty_fields_count - 1
    
    @staticmethod
    def release_field(field):
        GameState.__empty_fields.add(field)
        GameState.__empty_fields_count = GameState.__empty_fields_count + 1

    @staticmethod
    def is_field_taken(field):
        return field not in GameState.__empty_fields
    
    @staticmethod
    def get_empty_fields_count():
        return GameState.__empty_fields_count

    @staticmethod
    def get_points():
        return GameState.__points

    @staticmethod
    def add_point():
        GameState.__points = GameState.__points + 1
    
    @staticmethod
    def finish_game():
        Logger.log_info(None, "GAME OVER!")
        GameState.__has_finished = True
    
    @staticmethod
    def is_game_finished():
        return GameState.__has_finished
