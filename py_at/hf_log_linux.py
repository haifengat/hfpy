#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = 'hf logging'
__author__ = 'HaiFeng'
__mtime__ = '20180712'


import logging
import os
from logging.handlers import TimedRotatingFileHandler

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

# The background is set with 40 plus the number of the color, and the foreground with 30

# These are the sequences need to get colored ouput
RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"
BOLD_SEQ = "\033[1m"


def formatter_message(message, use_color=True):
    if use_color:
        message = message.replace("$RESET", RESET_SEQ).replace("$BOLD", BOLD_SEQ)
    else:
        message = message.replace("$RESET", "").replace("$BOLD", "")
    return message


COLORS = {
    'WARNING': YELLOW,
    'INFO': WHITE,
    'DEBUG': BLUE,
    'CRITICAL': YELLOW,
    'ERROR': RED
}


class ColoredFormatter(logging.Formatter):
    def __init__(self, msg, use_color=True):
        logging.Formatter.__init__(self, msg, '%Y-%m-%d %H:%M:%S')
        self.use_color = use_color

    def format(self, record):
        levelname = record.levelname
        if self.use_color and levelname in COLORS:
            levelname_color = COLOR_SEQ % (30 + COLORS[levelname]) + levelname + RESET_SEQ
            record.levelname = levelname_color
        return logging.Formatter.format(self, record)

# Custom logger class with multiple destinations


class ColoredLogger(logging.Logger):
    FORMAT = "[$BOLD%(asctime)s$RESET][%(levelname)-18s]  %(message)s"  # ($BOLD%(filename)s$RESET:%(lineno)d)"
    COLOR_FORMAT = formatter_message(FORMAT, True)

    def __init__(self, name):
        logging.Logger.__init__(self, name, logging.INFO)

        color_formatter = ColoredFormatter(self.COLOR_FORMAT)

        console = logging.StreamHandler()
        console.setFormatter(color_formatter)

        self.addHandler(console)
        return


logging.setLoggerClass(ColoredLogger)


class Logger:
    def __init__(self, clevel=logging.INFO, Flevel=logging.INFO):
        if not os.path.exists('logs'):
            os.mkdir('logs')
        self.logger = logging.Logger('log')  # logging.getLogger('log')

        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')

        # 设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)

        # 设置文件日志
        # fh = logging.FileHandler(logfile_dir + '/log.log', 'a', encoding='utf-8')

        # 每天凌晨,备份之前的记录
        fh = TimedRotatingFileHandler(filename="logs/log", when="MIDNIGHT", interval=1, backupCount=30)
        fh.suffix = "%Y-%m-%d.log"  # 此格式必须与上面when对应,否则无法实现backcount设置的保留删除功能
        # fh.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
        # fh.suffix = "%Y-%m-%d_%H-%M.log"
        # fh.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)

        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def war(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)


def main():
    log = Logger(logging.INFO)
    while True:
        log.info('test')
        log.war('test')
        log.error('test')


if __name__ == '__main__':
    main()
