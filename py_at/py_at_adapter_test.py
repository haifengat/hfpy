#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/23'
"""
import sys

sys.path.append('..')	 #调用父目录下的模块

from py_at.Bar import Bar
from py_at.EnumDefine import *
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

		self.TradingDay = ''
		self.log = open('orders.csv', 'w')
		self.log.write('')  # 清空内容
		self.real = False  # 控制实际下单

		self.stra_instances = []

		cur_path = os.getcwd()
		# 目录到接口下
		os.chdir(os.path.join(os.getcwd(), '../py_ctp/'))
		self.q = CtpQuote()
		self.q.OnFrontConnected = self.q_OnFrontConnected
		self.q.OnRspUserLogin = self.q_OnRspUserLogin
		self.q.OnRtnTick = self.q_Tick

		self.t = CtpTrade()
		self.t.OnFrontConnected = self.OnFrontConnected
		self.t.OnRspUserLogin = self.OnRspUserLogin

		os.chdir(cur_path)

	# -------此处调用ctp接口即可实现实际下单---------------------------------------------------------------
	def on_order(self, stra, order):
		"""strategy's order"""
		p = Data()
		p = stra
		_order = OrderItem()
		_order = order
		print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}'.format(len(p.Orders), stra.Bars[0].D, _order.Direction, _order.Offset, _order.Price, _order.Volume, _order.Remark))
		self.log.write('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\n'.format(len(p.Orders), stra.Bars[0].D, _order.Direction, _order.Offset, _order.Price, _order.Volume, _order.Remark))

		if self.real:
			print(order)
			# 平今与平昨;逻辑从C#抄过来;没提示...不知道为啥,只能盲码了.
			dire = DirectionType.Buy if _order.Direction == Direction.Buy else DirectionType.Sell
			if _order.Offset != Offset.Open:
				key = '{0}_{1}'.format(_order.Instrument, int(DirectionType.Sell if _order.Direction == Direction.Buy else DirectionType.Buy))
				# 无效,没提示...pf = PositionField()
				pf = self.t.DicPositionField.get(key)
				if not pf or pf.Position <= 0:
					print('没有对应的持仓')
				else:
					volClose = min(pf.Position, _order.Volume)  # 可平量
					instField = self.t.DicInstrument[_order.Instrument]
					if instField.ExchangeID == 'SHFE':
						tdClose = min(volClose, pf.TdPosition)
						if tdClose > 0:
							self.t.ReqOrderInsert(_order.Instrument, dire, OffsetFlagType.CloseToday, _order.Price, tdClose, OrderType.Limit, 100)
							volClose -= tdClose
					if volClose > 0:
						self.t.ReqOrderInsert(_order.Instrument, dire, OffsetFlagType.Close, _order.Price, volClose, OrderType.Limit, 100)
			else:
				self.t.ReqOrderInsert(stra.Instrument, dire, OffsetFlagType.Open, _order.Price, _order.Volume, OrderType.Limit, 100)

	# ----------------------------------------------------------------------
	def load_strategy(self):
		"""加载../strategy目录下的策略"""

		"""通过文件名取到对应的继承Data的类并实例"""
		# for path in ['strategies', 'private']:
		for path in ['private']:
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
				obj = Data()
				obj = c()  # new class
				print("#obj:{0}", obj)
				self.stra_instances.append(obj)

	# ----------------------------------------------------------------------
	def read_from_mq(self, stra):
		"""netMQ"""
		_stra = Data()
		_stra = stra
		# pip install pyzmq即可安装
		context = zmq.Context()
		socket = context.socket(zmq.REQ)  # REQ模式,即REQ-RSP  CS结构
		# socket.connect('tcp://localhost:8888')	#连接本地测试
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
	def read_data_test(self):
		"""取历史和实时K线数据,并执行策略回测"""
		stra = Data()
		for stra in self.stra_instances:
			# 取数据
			ddoc = self.read_from_mq(stra)

			# print params os strategy
			stra.OnOrder = self.on_order
			for p in stra.Params:
				print("{0}:{1}".format(p, stra.Params[p]), end=' ')

			bars = []
			for doc in ddoc:
				bar = Bar(doc["_id"], doc["High"], doc["Low"], doc["Open"], doc["Close"], doc["Volume"], doc["OpenInterest"])
				stra.__new_min_bar__(bar)  # 调Data的onbar

		print("\ntest history is end.")

		self.real = True


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
		print(field)
		for stra in self.stra_instances:
			if stra.Instrument == field.Instrument:
				stra.on_tick(field)
				print(field)

	def Run(self):
		""""""
		self.t.ReqConnect('tcp://180.168.146.187:10000')



if __name__ == '__main__':
	""""""

	a = AdapterTest()
	a.load_strategy()
	a.read_data_test()
	a.Run()
	input()

