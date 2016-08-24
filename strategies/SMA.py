#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/8/16'
"""

class SMA:
	def __init__(self, series, period):
		self.Period = period
		self.Series = series
		self.Result = []


	def Update(self):
		rtn = 0.0

		for i in range(0, min(len(self.Series), self.Period)):
			rtn += self.Series[i]
		if len(self.Result) < len(self.Series):
			self.Result.insert(0, rtn / self.Period)
		else:
			self.Result[0] = rtn / self.Period
