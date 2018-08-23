#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = '显示K线'
__author__ = 'HaiFeng'
__mtime__ = '20180823'


import json
from pyecharts import Kline
import pandas as pd
from pandas import DataFrame


def formatter(params, tickes, callback):
    return '日:' + params.name.split('T')[0] + '<br>时:' + params.name.split('T')[1] + '<br>开:' + params.value[1] + '<br>高:' + params.value[4] + '<br>低:' + params.value[3] + '<br>收:' + params.value[2]


def show(bars: dict):
    df: DataFrame = None
    df = pd.read_json(json.dumps(bars, ensure_ascii=True))
    df['dt'] = pd.to_datetime(df['DateTime'], format='%Y%m%d %H:%M:%S')
    # df['DateTime'] = pd.to_numeric()
    df = df.drop('DateTime', axis=1)
    df = df.set_index('dt')
    # 列排序,转成json后顺序打乱,无法正常显示数据
    cols = ['Open', 'Close', 'Low', 'High']
    df = df.ix[:, cols]
    candle = Kline('K线示例')
    candle.add('K线', df.index.tolist(), df.values.tolist(), mark_point=['max', 'min'], is_datazoom_show=True, tooltip_axispointer_type='cross', tooltip_formatter=formatter)
    candle.render()
