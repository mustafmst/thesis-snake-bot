from snake.utils.logger import Logger
from snake import FIELD_SIZE


class GameState:
    __points = 0
    __has_finished = False
    __empty_fields = []
    __fruit_position = None

    @staticmethod
    def add_fruit(field_id):
        pos = GameState.__empty_fields[field_id]
        GameState.__fruit_position = pos
        return pos

    @staticmethod
    def remove_fruit():
        GameState.__fruit_position = None
    
    @staticmethod
    def is_there_a_fruit(position):
        if GameState.__fruit_position is not None:
            return position == GameState.__fruit_position
        return False

    @staticmethod
    def fruit_exist():
        return GameState.__fruit_position is not None

    @staticmethod
    def init_empty_fields(size):
        for x in range(size[0]):
            for y in range(size[1]):
                GameState.__empty_fields.append(
                    (x*FIELD_SIZE, y*FIELD_SIZE)
                )

    @staticmethod
    def take_up_field(field):
        GameState.__empty_fields.remove(field)
    
    @staticmethod
    def release_field(field):
        GameState.__empty_fields.append(field)

    @staticmethod
    def is_field_taken(field):
        return field not in GameState.__empty_fields
    
    @staticmethod
    def get_empty_fields_count():
        return len(GameState.__empty_fields)

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
