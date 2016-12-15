#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/12/5'
"""
import _thread

from py_at.adapters.ctp_trade import *
from py_at.adapters.ctp_quote import *
from flask_socketio import emit, join_room, leave_room, rooms, disconnect

class CTPProxy:
	''''''
	def __init__(self, investor, pwd):

		# 目录到接口下
		self.q = CtpQuote()
		self.q.OnFrontConnected = self.q_OnFrontConnected
		self.q.OnRspUserLogin = self.q_OnRspUserLogin
		self.q.OnRtnTick = self.q_Tick

		self.t = CtpTrade()
		self.t.OnFrontConnected = self.OnFrontConnected
		self.t.OnRspUserLogin = self.OnRspUserLogin
		self.t.OnRtnOrder = self.OnRtnOrder
		self.t.OnRtnCancel = self.OnRtnCancel
		self.t.OnRtnTrade = self.OnRtnTrade
		self.t.OnRtnInstrumentStatus = self.OnRtnInstrumentStatus

		self.Investor = investor
		self.PassWord = pwd

	def io_emit(self, rsp_type_str, data):
		socketio.emit(rsp_type_str, data, namespace='/ctp', room=self.Investor)

	def OnFrontConnected(self):
		print('connected')
		self.t.ReqUserLogin(self.Investor, self.PassWord, '9999')


	def OnRspUserLogin(self, info=InfoField):
		""""""
		print(info)
		self.io_emit('rsp_login', info.__dict__,)
		if info.ErrorID == 0:
			_thread.start_new_thread(self.OnData, ())
			self.q.ReqConnect('tcp://180.168.146.187:10010')

	#Onrspuserlogin中调用
	def OnData(self):
		stats = 1
		while self.t.IsLogin and stats > 0:#没有交易的品种时不再循环发送
			sleep(1)
			stats = sum(1 for n in self.t.DicInstrumentStatus.keys() if self.t.DicInstrumentStatus[n] == InstrumentStatusType.Continous)
			#print(self.t.Account.__dict__)
			self.io_emit('rsp_account', self.t.Account.__dict__)
			# 需要在struct中增加obj2json的转换函数
			for p in self.t.DicPositionField:
				self.io_emit('rsp_position', self.t.DicPositionField[p].__dict__)

	def OnRtnOrder(self, f = OrderField):
		""""""
		self.io_emit('rtn_order', f.__dict__)


	def OnRtnTrade(self, f = TradeField):
		""""""
		self.io_emit('rtn_trade', f.__dict__)


	def OnRtnCancel(self, f = OrderField):
		""""""
		self.io_emit('rtn_cancel', f.__dict__)


	def OnRtnErrOrder(self, f = OrderField, info = InfoField):
		""""""
		# print(f)
		# print(info)
		self.io_emit('rtn_err_order', {'order':f.__dict__, 'info':info.__dict__})

	def q_OnFrontConnected(self):
		""""""
		print("q:connected by client")
		self.q.ReqUserLogin(self.Investor, self.PassWord, '9999')

	def OnRtnInstrumentStatus(self, inst, status):
		print('{0}:{1}'.format(inst, status))

	# ----------------------------------------------------------------------
	def q_OnRspUserLogin(self, info=InfoField):
		""""""
		print('quote')
		print(info)

		self.io_emit('rsp_login', info.__str__())


	def q_Tick(self, field=Tick):
		""""""
		pass


	def Run(self):
		""""""
		self.t.ReqConnect('tcp://180.168.146.187:10000')

from app import socketio
ctps = {}


@socketio.on('connect', namespace='/ctp')
def ctp_connect():
	print('ctp connect...')

@socketio.on('disconnect', namespace='/ctp')
def disconnect():
	print('ctp disconnected')

@socketio.on('login', namespace='/ctp')
def login(data):
	#隔夜登录
	user = data['investor']
	ctp = None
	if user in ctps.keys():
		ctp = ctps[user]
		if not ctp.t.IsLogin:
			ctp.t.Release()
			ctp = CTPProxy(data['investor'], data['pwd'])
			ctps[user] = ctp
			ctp.Run()
		else:   #重复登录时需要发送的数据(收盘后不会发送)
			socketio.emit('rsp_account', ctp.t.Account.__dict__, namespace='/ctp')
			for p in ctp.t.DicPositionField:
				socketio.emit('rsp_position', ctp.t.DicPositionField[p].__dict__, namespace='/ctp')
		print(user)
	else:
		ctp = CTPProxy(data['investor'], data['pwd'])
		ctps[user] = ctp
		print(ctps)
		ctp.Run()
	join_room(user)