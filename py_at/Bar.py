#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/8/16'
"""

class Bar(object):
	'''K线数据'''

	def __init__(self, datetime, h, l, o, c, v, i):
		self.D = datetime
		self.H = h
		self.L = l
		self.O = o
		self.C = c
		self.V = v
		self.I = i
		self.__preVolume = 0

	#----------------------------------------------------------------------
	def __str__(self):
		""""""
		return '{self.D}, {self.H}, {self.L}, {self.O}, {self.C}, {self.V}, {self.I}'.format(self = self)