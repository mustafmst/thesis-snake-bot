import numpy as np

from snake.constans import PLAYER_VALUE, TAIL_VALUE, FRUIT_VALUE


def get_player_pos(state):
    where = np.where(state == PLAYER_VALUE)
    if len(where[0]) is 0:
        x = 0
    else:
        x = where[0][0]
    if len(where[1]) is 0:
        y = 0
    else:
        y = where[1][0]
    return x, y


def get_horizontal(state, player_pos):
    return state[player_pos[0]]


def get_vertical(state, player_pos):
    return state[:, player_pos[1]]


def get_diagonal(state, player_pos, direction=1):
    if direction < 0:
        player_pos = ((len(state) - 1) - player_pos[0], player_pos[1])
    return state[::direction, :].diagonal(player_pos[1]-player_pos[0])


def get_player_index(axis):
    where = np.where(axis == PLAYER_VALUE)[0]
    if len(where) is 0:
        return 0
    else:
        return where[0]


def get_distances(from_index, to_value, axis):
    indexes = np.where(axis == to_value)[0]
    if len(indexes) is 0:
        return 0, 0
    all_distances = [from_index-e for e in indexes]

    plus = [e for e in all_distances if e > 0]
    if len(plus) is 0:
        plus = 0
    else:
        plus = min(plus)

    minus = [-e for e in all_distances if e < 0]
    if len(minus) is 0:
        minus = 0
    else:
        minus = min(minus)

    return plus, minus


def transform_to_vision(param):
    if param != 0:
        return 1
    return 0


def create_fruit_view(view, horizontal, vertical, first_diagonal, second_diagonal):
    # Horizontal
    player_index = get_player_index(horizontal)
    distances = get_distances(player_index, FRUIT_VALUE, horizontal)
    view[0][0] = transform_to_vision(distances[0])
    view[0][1] = transform_to_vision(distances[1])

    # Vertical
    player_index = get_player_index(vertical)
    distances = get_distances(player_index, FRUIT_VALUE, vertical)
    view[0][2] = transform_to_vision(distances[0])
    view[0][3] = transform_to_vision(distances[1])

    # 1 diag
    player_index = get_player_index(first_diagonal)
    distances = get_distances(player_index, FRUIT_VALUE, first_diagonal)
    view[0][4] = transform_to_vision(distances[0])
    view[0][5] = transform_to_vision(distances[1])

    # 2 diag
    player_index = get_player_index(second_diagonal)
    distances = get_distances(player_index, FRUIT_VALUE, second_diagonal)
    view[0][6] = transform_to_vision(distances[0])
    view[0][7] = transform_to_vision(distances[1])


def create_tail_view(view, horizontal, vertical, first_diagonal, second_diagonal):
    # Horizontal
    player_index = get_player_index(horizontal)
    distances = get_distances(player_index, TAIL_VALUE, horizontal)
    view[1][0] = transform_to_vision(distances[0])
    view[1][1] = transform_to_vision(distances[1])

    # Vertical
    player_index = get_player_index(vertical)
    distances = get_distances(player_index, TAIL_VALUE, vertical)
    view[1][2] = transform_to_vision(distances[0])
    view[1][3] = transform_to_vision(distances[1])

    # 1 diag
    player_index = get_player_index(first_diagonal)
    distances = get_distances(player_index, TAIL_VALUE, first_diagonal)
    view[1][4] = transform_to_vision(distances[0])
    view[1][5] = transform_to_vision(distances[1])

    # 2 diag
    player_index = get_player_index(second_diagonal)
    distances = get_distances(player_index, TAIL_VALUE, second_diagonal)
    view[1][6] = transform_to_vision(distances[0])
    view[1][7] = transform_to_vision(distances[1])


def get_distances_to_wall(player_index, axis):
    return player_index + 1, (len(axis) - player_index)


def create_walls_view(view, horizontal, vertical, first_diagonal, second_diagonal):
    # Horizontal
    player_index = get_player_index(horizontal)
    distances = get_distances_to_wall(player_index, horizontal)
    view[2][0] = 1/distances[0]
    view[2][1] = 1/distances[1]

    # Vertical
    player_index = get_player_index(vertical)
    distances = get_distances_to_wall(player_index, vertical)
    view[2][2] = 1/distances[0]
    view[2][3] = 1/distances[1]

    # 1 diag
    player_index = get_player_index(first_diagonal)
    distances = get_distances_to_wall(player_index, first_diagonal)
    view[2][4] = 1/distances[0]
    view[2][5] = 1/distances[1]

    # 2 diag
    player_index = get_player_index(second_diagonal)
    distances = get_distances_to_wall(player_index, second_diagonal)
    view[2][6] = 1/distances[0]
    view[2][7] = 1/distances[1]


def get_snake_view(board_state):
    state = np.array(board_state)
    player_pos = get_player_pos(state)
    view = [[0 for j in range(8)] for i in range(3)]
    horizontal = get_horizontal(state, player_pos)
    vertical = get_vertical(state, player_pos)
    first_diagonal = get_diagonal(state, player_pos, direction=1)
    second_diagonal = get_diagonal(state, player_pos, direction=-1)
    create_fruit_view(view, horizontal, vertical, first_diagonal, second_diagonal)
    create_tail_view(view, horizontal, vertical, first_diagonal, second_diagonal)
    create_walls_view(view, horizontal, vertical, first_diagonal, second_diagonal)
    return view

