#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = '主程序'
__author__ = 'HaiFeng'
__mtime__ = '20180822'

from py_at.hf import HFPY
import sys

if __name__ == '__main__':
    HFPY().Run()
    while input().lower() != 'q':
        continue
