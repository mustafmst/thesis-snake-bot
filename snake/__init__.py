from snake.utils import logger_levels


def get_resolution(board_size):
    return (
        board_size[0] * FIELD_SIZE + SIDE_PANEL_WIDTH,
        board_size[1] * FIELD_SIZE
    )


PLAYER_MODE = "PLAYER_MODE"
AI_MODE = "AI_MODE"

FIELD_SIZE = 16
SIDE_PANEL_WIDTH = 100

DEFAULT_CONFIG = dict(
    board_size=(10, 10),
    game_mode=PLAYER_MODE,
    move_sleep=240,
    log_level=logger_levels.DEBUG
)
