#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/23'
"""

from py_at.at_struct import *

class QuoteAdapter:
	""""""

	def __init__(self):
		self.DicTick = {}


	def ReqConnect(self, pAddress=''):
		pass

	def ReqUserLogin(self, user='', pwd='', broker=''):
		pass

	def ReqSubscribeMarketData(self, pInstrument = ''):
		pass



	def OnFrontConnected(self):
		""""""
		pass


	# ----------------------------------------------------------------------
	def OnUserLogin(self, info=InfoField):
		""""""
		pass


	# ----------------------------------------------------------------------
	def OnRtnTick(self, field=Tick):
		""""""
		pass