import time

from snake.utils import logger_levels


class Logger:
    __log_level = logger_levels.NONE

    @staticmethod
    def set_log_level(level):
        Logger.__log_level = level

    @staticmethod
    def log(level, sender, message):
        if level >= Logger.__log_level:
            print("[{}][{}] - {}".format(
                time.ctime(),
                sender.__class__.__name__ if sender != None else "Game",
                message
            ))

    @staticmethod
    def log_fps(sender, clock):
        msg = "FPS: {}".format(clock.get_fps())
        Logger.log(
            logger_levels.FPS,
            sender,
            msg
        )

    @staticmethod
    def log_debug(sender, message):
        Logger.log(
            logger_levels.DEBUG,
            sender,
            message
        )

    @staticmethod
    def log_trace(sender, message):
        Logger.log(
            logger_levels.TRACE,
            sender,
            message
        )

    @staticmethod
    def log_info(sender, message):
        Logger.log(
            logger_levels.INFO,
            sender,
            message
        )
