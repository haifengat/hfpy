#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/1'
"""


class EMA:
	def __init__(self, series, period):
		self.Period = period
		self.Series = series
		self.Result = []


	def Update(self):
		n = 2 / (self.Period + 1)
		if len(self.Series) == 1:
			rtn = self.Series[0]
		else:
			if len(self.Result) == 1:
				rtn = self.Result[0] + n * (self.Series[0] - self.Result[0])
			else:
				rtn = self.Result[1] + n * (self.Series[0] - self.Result[1])

		if len(self.Result) < len(self.Series):
			self.Result.insert(0, rtn)
		else:
			self.Result[0] = rtn
