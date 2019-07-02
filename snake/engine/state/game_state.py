from snake.utils.logger import Logger
from snake.constans import PLAYER_VALUE, TAIL_VALUE, FRUIT_VALUE
from snake import FIELD_SIZE


class GameState:
    def __init__(self):
        self.__points = 0
        self.__has_finished = False
        self.__empty_fields = []
        self.__fruit_position = None
        self.__game_config = None
        self.__player = None
        self.__tail = None
        self.__was_fruit_eaten = False
        self.__moves_count = 0
        self.__life_time = 0

    def get_life_time(self):
        return self.__life_time

    def add_move(self):
        self.__moves_count += 1
        self.__life_time += 1

    def register_player(self, player):
        self.__player = player

    def register_tail(self, tail):
        self.__tail = tail

    def set_game_config(self, config):
        self.__game_config = config

    def add_fruit(self, field_id):
        pos = self.__empty_fields[field_id]
        self.__fruit_position = pos
        return pos

    def remove_fruit(self):
        self.__was_fruit_eaten = True
        self.__fruit_position = None
        self.__moves_count = 0

    def finish_eating(self):
        self.__was_fruit_eaten = False

    def is_eating(self):
        return self.__was_fruit_eaten

    def is_there_a_fruit(self, position):
        if self.fruit_exist():
            return position == self.__fruit_position
        return False

    def fruit_exist(self):
        return self.__fruit_position is not None

    def get_fruit_position(self):
        return self.__fruit_position

    def init_empty_fields(self, size):
        for x in range(size[0]):
            for y in range(size[1]):
                self.__empty_fields.append(
                    (x*FIELD_SIZE, y*FIELD_SIZE)
                )

    def take_up_field(self, field):
        self.__empty_fields.remove(field)

    def release_field(self, field):
        self.__empty_fields.append(field)

    def is_field_taken(self, field):
        return field not in self.__empty_fields

    def get_empty_fields_count(self):
        return len(self.__empty_fields)

    def get_points(self):
        return self.__points

    def add_point(self):
        self.__points = self.__points + 1

    def finish_game(self):
        Logger.log_info(None, "GAME OVER!")
        self.__has_finished = True

    def is_game_finished(self):
        board = self.__game_config['board_size']
        fields = board[0] * board[1]
        if self.__moves_count > 200:
            self.finish_game()
        return self.__has_finished

    def get_state(self):
        board_size = self.__game_config["board_size"]
        state = [[0 for i in range(board_size[0])] for j in range(board_size[1])]
        if self.__player is not None:
            player_position = self.__player.get_position()
            state[int(player_position[0]/FIELD_SIZE)][int(player_position[1]/FIELD_SIZE)] = PLAYER_VALUE
        if self.__tail is not None:
            for t in self.__tail.get_tail_blocks():
                state[int(t[0]/FIELD_SIZE)][int(t[1]/FIELD_SIZE)] = TAIL_VALUE
        if self.__fruit_position is not None:
            state[int(self.__fruit_position[0] / FIELD_SIZE)][int(self.__fruit_position[1] / FIELD_SIZE)] = FRUIT_VALUE
        return state

