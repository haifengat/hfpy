#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/23'
"""
import sys
import os

from py_at.Statistics import Statistics

sys.path.append(os.path.join(sys.path[0], '..'))	 #调用父目录下的模块

from py_at.EnumDefine import *
from py_at.Bar import *
from py_at.OrderItem import OrderItem
from py_at.adapters.ctp_trade import *
from py_at.adapters.ctp_quote import *

from py_at.Data import Data
import zmq  	#netMQ
import gzip		#解压
import json

class AdapterTest:
	""""""
	def __init__(self):
		"""Constructor"""
		self.stra_instances = []
		self.q = None
		self.t = None
		self.TradingDay = ''
		self.real = False  # 控制实际下单

	# -------此处调用ctp接口即可实现实际下单---------------------------------------------------------------
	def on_order(self, stra, order):
		"""strategy's order"""
		p = stra
		#print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}'.format(type(stra), len(p.Orders), order.DateTime, order.Direction, order.Offset, order.Price, order.Volume, order.Remark))

		if self.real:
			print(order)
			# 平今与平昨;逻辑从C#抄过来;没提示...不知道为啥,只能盲码了.
			dire = DirectionType.Buy if order.Direction == Direction.Buy else DirectionType.Sell
			if order.Offset != Offset.Open:
				key = '{0}_{1}'.format(order.Instrument, int(DirectionType.Sell if order.Direction == Direction.Buy else DirectionType.Buy))
				# 无效,没提示...pf = PositionField()
				pf = self.t.DicPositionField.get(key)
				if not pf or pf.Position <= 0:
					print('没有对应的持仓')
				else:
					volClose = min(pf.Position, order.Volume)  # 可平量
					instField = self.t.DicInstrument[order.Instrument]
					if instField.ExchangeID == 'SHFE':
						tdClose = min(volClose, pf.TdPosition)
						if tdClose > 0:
							self.t.ReqOrderInsert(order.Instrument, dire, OffsetType.CloseToday, order.Price, tdClose, OrderType.Limit, 100)
							volClose -= tdClose
					if volClose > 0:
						self.t.ReqOrderInsert(order.Instrument, dire, OffsetType.Close, order.Price, volClose, OrderType.Limit, 100)
			else:
				self.t.ReqOrderInsert(stra.Instrument, dire, OffsetType.Open, order.Price, order.Volume, OrderType.Limit, 100)

	# ----------------------------------------------------------------------
	def load_strategy(self):
		"""加载../strategy目录下的策略"""

		"""通过文件名取到对应的继承Data的类并实例"""
		# for path in ['strategies', 'private']:
		for path in ['strategies']:
			files = os.listdir("../{0}/".format(path))
			for f in files:
				if os.path.isdir(f) or os.path.splitext(f)[0] == '__init__' or os.path.splitext(f)[-1] != ".py":
					continue
				# 目录结构???
				module_name = "{1}.{0}".format(os.path.splitext(f)[0], path)
				class_name = os.path.splitext(f)[0]

				module = __import__(module_name)  # import module

				c = getattr(getattr(module, class_name), class_name)  # 双层调用才是class,单层是为module

				if not issubclass(c, Data):  # 类c是Data的子类
					continue
				print("#c:{0}", c)
				obj = c()  # new class
				obj.ID = '{0}_{1}'.format(class_name, len(self.stra_instances))
				print("#obj:{0}", obj)
				self.stra_instances.append(obj)

	# ----------------------------------------------------------------------
	def read_from_mq(self, stra=Data):
		"""netMQ"""
		_stra = stra
		# pip install pyzmq即可安装
		context = zmq.Context()
		socket = context.socket(zmq.REQ)  # REQ模式,即REQ-RSP  CS结构
		socket.connect('tcp://58.247.171.146:5055')  # 实际netMQ数据服务器地址
		# 请求数据格式
		req = ReqPackage()
		req.Type = 0  # BarType.Min ????
		req.Instrument = _stra.Instrument
		req.Begin = _stra.BeginDate
		req.End = _stra.EndDate
		# __dict__返回diction格式,即{key,value}格式
		p = req.__dict__
		socket.send_json(p)  # 直接发送__dict__转换的{}即可,不需要再转换成str

		# msg = socket.recv_unicode()	#服务器此处查询出现异常, 排除中->C#正常
		# 用recv接收,但是默认的socket中并没有此提示函数(可能是向下兼容的函数),不知能否转换为其他格式
		bs = socket.recv()  # 此处得到的是bytes

		# gzip解压:decompress(bytes)解压,会得到解压后的bytes,再用decode转成string
		gzipper = gzip.decompress(bs).decode()  # decode转换为string

		# json解析:与dumps对应,将str转换为{}
		bars = json.loads(gzipper)  # json解析

		# 此处对bars进行数据组合,即1min->nmin

		return bars

	# ----------------------------------------------------------------------
	def read_data_test(self, stra):
		"""取历史和实时K线数据,并执行策略回测"""
		# 取数据
		ddoc = self.read_from_mq(stra)

		# print params os strategy
		stra.OnOrder = self.on_order
		for p in stra.Params:
			print("{0}:{1}".format(p, stra.Params[p]), end=' ')

		for doc in ddoc:
			bar = Bar(doc["_id"], doc["High"], doc["Low"], doc["Open"], doc["Close"], doc["Volume"], doc["OpenInterest"])
			stra.__new_min_bar__(bar)  # 调Data的onbar
		print("orders:{0}, bars:{1}".format(len(stra.Orders),len(stra.Bars)))

		print("test history is end.")


	def TradeInit(self):
		# 目录到接口下
		self.q = CtpQuote()
		self.q.OnFrontConnected = self.q_OnFrontConnected
		self.q.OnRspUserLogin = self.q_OnRspUserLogin
		self.q.OnRtnTick = self.q_Tick

		self.t = CtpTrade()
		self.t.OnFrontConnected = self.OnFrontConnected
		self.t.OnRspUserLogin = self.OnRspUserLogin

		self.t.ReqConnect('tcp://180.168.146.187:10000')


	def OnFrontConnected(self):
		print('connected')
		self.t.ReqUserLogin('008105', '1', '9999')

	def OnRspUserLogin(self, info=InfoField):
		""""""
		print(info)
		if info.ErrorID == 0:
			self.q.ReqConnect('tcp://180.168.146.187:10010')

	def q_OnFrontConnected(self):
		""""""
		print("q:connected by client")
		self.q.ReqUserLogin('008105', '1', '9999')

	#----------------------------------------------------------------------
	def q_OnRspUserLogin(self, info = InfoField):
		""""""
		print('quote')
		print(info)
		self.q.ReqSubscribeMarketData('rb1610')
		for stra in self.stra_instances:
			self.q.ReqSubscribeMarketData(stra.Instrument)

	def q_Tick(self, field = Tick):
		""""""
		for stra in self.stra_instances:
			if stra.Instrument == field.Instrument:
				stra.on_tick(field)
				#print(field)



if __name__ == '__main__':
	""""""
	#orders = [{"Direction":0,"DateTime":"20161019 14:00:00","Price":2300}]
	# 		{"Direction":1,"DateTime":"20161019 09:00:00","Price":2400}]
	#
	# req = {'instrument':'rb1701',
	# 'begin':'20160101',
	# 'end':'20161231',
	# 'interval':10,
	# 'intervalType':'min',
	# }
	# url = 'http://localhost:63343/web_client/echarts_show.html?_ijt=2vjntkque47quvsfsp1d81t090'
	# #value = parse.urlencode(req) 不要用这种方式，无法解析还原为object
	#
	# #print(data)
	# webbrowser.open(url+'&data=' + parse.quote(json.dumps(req))+ '&orders=' +parse.quote(json.dumps(orders)))
	# input()

	a = AdapterTest()
	a.load_strategy()

	for stra in a.stra_instances:
		a.read_data_test(stra)
	#a.Run()
	#显示报告
	for stra in a.stra_instances:
		Statistics(stra).ShowWeb()
	input()
