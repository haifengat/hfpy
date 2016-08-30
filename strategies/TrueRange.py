#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'TR实际变动范围'
__author__ = 'HaiFeng'
__mtime__ = '2016/8/25'
"""

class TrueRange:

	def __init__(self, high, low, close):
		self.H = high
		self.L = low
		self.C = close
		self.Result = []

	def Update(self):
		if len(self.H) <= 1:
			rtn = 0
		else:
			#rtn = max(self.H[0] - self.L[0], max(self.H[0] - self.C[1], self.C[1] - self.L[0]))
			rtn = max(self.H[0], self.C[1]) - min(self.L[0], self.C[1])

		if len(self.Result) < len(self.H):
			self.Result.insert(0, rtn)
		else:
			self.Result[0] = rtn
