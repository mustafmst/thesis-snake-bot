from snake.utils import logger_levels


PLAYER_MODE = "PLAYER_MODE"
AI_MODE = "AI_MODE"

FIELD_SIZE = 16
SIDE_PANEL_WIDTH = 100

DEFAULT_CONFIG = dict(
    board_size = (20,20),
    game_mode = PLAYER_MODE,
    sleep = 0.01,
    log_level = logger_levels.DEBUG
)