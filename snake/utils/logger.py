import time

from snake.utils import logger_levels


class Logger:
    __log_level = logger_levels.NONE

    @staticmethod
    def set_log_level(level):
        Logger.__log_level = level

    @staticmethod
    def log(level, sender, message):
        if Logger.__log_level >= level:
            print("[{}][{}] - {}".format(
                time.ctime(),
                sender.name,
                message
            ))

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
