#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/21'
"""

from enum import Enum


class IntervalType(Enum):
    """时间类型:秒,分,时,日,周,月,年"""

    Second = 0
    '''秒'''

    Minute = 1
    '''分'''

    Hour = 2
    '''时'''

    Day = 3
    '''日'''

    Week = 4
    '''周'''

    Month = 5
    '''月'''

    Year = 6
    '''年'''

    def __int__(self):
        """return int value"""
        return self.value

class DirectType(Enum):
    """买卖"""
    Buy = 0
    """买"""
    Sell = 1
    """卖"""

class OffsetType(Enum):
    """开平"""
    Open = 0
    '''开'''
    Close = 1
    '''平'''
    CloseToday = 2
    '''平今'''