#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = '日志模块'
__author__ = 'HaiFeng'
__mtime__ = '20180707'

import logging
from logging.handlers import TimedRotatingFileHandler
from time import sleep
import re
import os
import ctypes

FOREGROUND_WHITE = 0x0007
FOREGROUND_BLUE = 0x01  # text color contains blue.
FOREGROUND_GREEN = 0x02  # text color contains green.
FOREGROUND_RED = 0x04  # text color contains red.
FOREGROUND_YELLOW = FOREGROUND_RED | FOREGROUND_GREEN

STD_OUTPUT_HANDLE = -11
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool


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

    def debug(self, message, color=FOREGROUND_GREEN):
        set_color(color)
        self.logger.debug(message)
        set_color(FOREGROUND_WHITE)

    def info(self, message):
        self.logger.info(message)

    def war(self, message, color=FOREGROUND_YELLOW):
        set_color(color)
        self.logger.warn(message)
        set_color(FOREGROUND_WHITE)

    def error(self, message, color=FOREGROUND_RED):
        set_color(color)
        self.logger.error(message)
        set_color(FOREGROUND_WHITE)

    def cri(self, message):
        self.logger.critical(message)


def main():
    log = Logger(logging.INFO)
    while True:
        log.info('test')
        log.war('test')
        log.error('test')
        sleep(10)


if __name__ == '__main__':
    main()
