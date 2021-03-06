import sys
import logging

class LogConfig(object):

    active_loggers = {}
    logfmt = '%(asctime)s, %(levelname)s, %(filename)s:%(lineno)d, %(message)s'
    default_loglevel = logging.INFO
    default_logdest = logging.StreamHandler(sys.stdout)

    @staticmethod
    def getLogger(obj, level=default_loglevel, dest=default_logdest):
        if obj in LogConfig.active_loggers:
            return LogConfig.active_loggers[obj]

        logger = logging.Logger(obj)
        logger.setLevel(level)
        dest.setFormatter(logging.Formatter(LogConfig.logfmt))
        logger.addHandler(dest)
        LogConfig.active_loggers[obj] = logger
        return logger

    @staticmethod
    def setLogLevel(level):
        LogConfig.default_loglevel = level
        for logger in LogConfig.active_loggers.values():
            logger.setLevel(level)

    @staticmethod
    def setLogDestination(dest):
        LogConfig.default_logdest = dest
        dest.setFormatter(logging.Formatter(LogConfig.logfmt))
        for logger in LogConfig.active_loggers.values():
            logger.setLogDestination(dest)
