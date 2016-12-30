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
		""""""
		self.q = None
		self.t = None
		self.Investor = investor
		self.PassWord = pwd
		self.init_ctp()

	def init_ctp(self):
		""""""
		if self.q:
			self.q.Release()
		if self.t:
			self.t.Release()

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
		self.t.OnRtnErrOrder = self.OnRtnErrOrder

	def io_emit(self, rsp_type_str, data):
		socketio.emit(rsp_type_str, data, namespace='/ctp', room=self.Investor+self.PassWord)

	def OnFrontConnected(self):
		print('{0} ctp connected'.format(self.Investor))
		self.t.ReqUserLogin(self.Investor, self.PassWord, '9999')


	def OnRspUserLogin(self, info=InfoField):
		""""""
		print(info)
		if info.ErrorID == 0:
			_thread.start_new_thread(self.OnData, ())
			self.q.ReqConnect('tcp://180.168.146.187:10010')
		else:
			if info.ErrorID == 7:
				print('ctp relogin')
				_thread.start_new_thread(self.relogin, ())
			else:
				self.io_emit('rsp_login', info.__dict__)
				_thread.start_new_thread(self.release, ())  # 须放在thread中，否则无法释放资源

	def relogin(self):
		self.init_ctp()
		sleep(60*5)
		print('relogin')
		self.Run()

	def release(self):
		self.t.Release()

	#Onrspuserlogin中调用
	def OnData(self):
		stats = 1
		while self.t.IsLogin and stats > 0:#没有交易的品种时不再循环发送::隔夜重启后会停止发送
			sleep(1)
			stats = sum(1 for n in self.t.DicInstrumentStatus.values() if n == InstrumentStatusType.Continous)
			#print(self.t.Account.__dict__)
			self.io_emit('rsp_account', self.t.Account.__dict__)
			# 需要在struct中增加obj2json的转换函数
			for p in self.t.DicPositionField:
				self.io_emit('rsp_position', self.t.DicPositionField[p].__dict__)
			#首次时发送title
			#所有position一次发送,先合成str再发.

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
		self.io_emit('rtn_err_order', {'order':f.__dict__, 'info':info.__dict__})

	def q_OnFrontConnected(self):
		""""""
		self.q.ReqUserLogin(self.Investor, self.PassWord, '9999')

	def OnRtnInstrumentStatus(self, inst, status):
		#print('{0}:{1}'.format(inst, status))
		pass

	# ----------------------------------------------------------------------
	def q_OnRspUserLogin(self, info=InfoField):
		""""""
		print('quote' + info.__str__())
		self.io_emit('rsp_login', info.__dict__)


	def q_Tick(self, field=Tick):
		""""""
		pass


	def Run(self):
		""""""
		self.t.ReqConnect('tcp://180.168.146.187:10000')

from app import socketio
import flask
ctps = {}
sid_investor = {}

@socketio.on('release', namespace='/ctp')
def ctp_release(data):
	leave_room(sid_investor[data['sid']])
	print('release from ' + data['investor'])

@socketio.on('connect', namespace='/ctp')
def ctp_connect():
	# client_sid = socketio.__dict__['server'].__dict__['manager'].__dict__['rooms']['/ctp'].keys()
	# ids = [id for id in client_sid if id not in ctps]
	# print(ids)

	#新连接
	new_sid = flask.request.sid
	print('ctp connect:' + new_sid)
	#使用emit为对此客户端发送消息
	emit('sid', new_sid)

@socketio.on('disconnect', namespace='/ctp')
def disconnect():
	sid = flask.request.sid
	print('ctp disconnected:' + sid)
	if sid in sid_investor:
		leave_room(sid_investor[sid])

@socketio.on('login', namespace='/ctp')
def login(data):
	#隔夜登录
	ctp_id = data['investor'] + data['pwd']
	ctp = None
	if ctp_id in ctps.keys():
		ctp = ctps[ctp_id]
		if not ctp.t.IsLogin:
			ctp.t.Release()
			ctp = CTPProxy(data['investor'], data['pwd'])
			ctps[ctp_id] = ctp
			ctp.Run()
		else:   #重复登录时需要发送的数据(收盘后不会发送)
			emit('rsp_login', {"ErrorID":0, "ErrorMsg":"正确"})
			emit('rsp_account', ctp.t.Account.__dict__)
			for p in ctp.t.DicPositionField:
				emit('rsp_position', ctp.t.DicPositionField[p].__dict__, namespace='/ctp')
			for o in ctp.t.DicOrderField:
				emit('rtn_order', ctp.t.DicOrderField[o].__dict__, namespace='/ctp')
			for t in ctp.t.DicTradeField:
				emit('rtn_trade', ctp.t.DicTradeField[t].__dict__, namespace='/ctp')
	else:
		ctp = CTPProxy(data['investor'], data['pwd'])
		ctps[ctp_id] = ctp
		ctp.Run()
	join_room(ctp_id)
	sid_investor[flask.request.sid] = ctp_id
	#等待登录
	i = 0
	while not ctp.t.IsLogin and i < 5:
		sleep(1)
		i+=1

	if ctp.t.IsLogin:
		print(sid_investor)
	else:
		ctps.pop(ctp_id)
		leave_room(ctp_id)
		sid_investor.pop(flask.request.sid)

@socketio.on('order', namespace='/ctp')
def order(data):
	print(data)
	inst = data['instrument']
	lots = int(data['lots'])
	price = float(data['price'])
	direction = data['direction']
	offset = data['offset']

	sid = data['sid']
	investor = sid_investor[sid]
	ctp = ctps[investor]
	ctp.t.ReqOrderInsert(inst, DirectType.Buy if direction == 'buy' else DirectType.Sell, OffsetType.Open if offset=='open' else OffsetType.Close, price, lots)


