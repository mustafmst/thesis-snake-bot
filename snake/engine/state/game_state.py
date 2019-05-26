from snake.utils.logger import Logger
from snake import FIELD_SIZE


class GameState:
    __points = 0
    __has_finished = False
    __empty_fields = []
    __fruit_position = None
    __game_config = None
    __player = None
    __tail = None
    __was_fruit_eaten = False
    __moves_count = 0

    @staticmethod
    def add_move():
        GameState.__moves_count += 1

    @staticmethod
    def register_player(player):
        GameState.__player = player

    @staticmethod
    def register_tail(tail):
        GameState.__tail = tail

    @staticmethod
    def set_game_config(config):
        GameState.__game_config = config

    @staticmethod
    def add_fruit(field_id):
        pos = GameState.__empty_fields[field_id]
        GameState.__fruit_position = pos
        return pos

    @staticmethod
    def remove_fruit():
        GameState.__was_fruit_eaten = True
        GameState.__fruit_position = None
        GameState.__moves_count = 0

    @staticmethod
    def finish_eating():
        GameState.__was_fruit_eaten = False

    @staticmethod
    def is_eating():
        return GameState.__was_fruit_eaten
    
    @staticmethod
    def is_there_a_fruit(position):
        if GameState.fruit_exist():
            return position == GameState.__fruit_position
        return False

    @staticmethod
    def fruit_exist():
        return GameState.__fruit_position is not None

    @staticmethod
    def get_fruit_position():
        return GameState.__fruit_position

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
        board = GameState.__game_config['board_size']
        fields = board[0] * board[1]
        if GameState.__moves_count > fields:
            GameState.finish_game()
        return GameState.__has_finished

    @staticmethod
    def get_state():
        board_size = GameState.__game_config["board_size"]
        state = [[0 for i in range(board_size[0])] for j in range(board_size[1])]
        if GameState.__player is not None:
            player_position = GameState.__player.get_position()
            state[int(player_position[0]/FIELD_SIZE)][int(player_position[1]/FIELD_SIZE)] = 1
        if GameState.__tail is not None:
            for t in GameState.__tail.get_tail_blocks():
                state[int(t[0]/FIELD_SIZE)][int(t[1]/FIELD_SIZE)] = 0.2
        if GameState.__fruit_position is not None:
            state[int(GameState.__fruit_position[0] / FIELD_SIZE)][int(GameState.__fruit_position[1] / FIELD_SIZE)] = 2
        return state

