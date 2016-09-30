#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/26'
"""

import numpy as np
from talib import abstract


inputs = {
	'open': np.random.rand(20),
	'high': np.random.rand(20),
	'low': np.random.rand(20),
	'close': np.random.rand(20)
}

print(abstract.SMA(inputs, 5, price = 'close'))

inputs['open'] = np.append(inputs['open'], np.random.rand(1))
inputs['high'] = np.append(inputs['high'], np.random.rand(1))
inputs['low'] = np.append(inputs['low'], np.random.rand(1))
inputs['close'] = np.append(inputs['close'], np.random.rand(1))

print(abstract.SMA(inputs, 5, price = 'close'))
