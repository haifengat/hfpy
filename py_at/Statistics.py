#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/11/2'
"""
import urllib
import webbrowser
from urllib import request

import py_at.switch
from py_at.EnumDefine import *
from functools import reduce
import zmq
import gzip
import json
import os
import sys

class Statistics():
	""""""

	def __init__(self, stra):
		""""""
		self.stra = stra

		self.Product = None
		self.Report = []

		#更新品种数据
		products = self.get_product_zmq()
		for prod in products:
			if prod['_id'] == stra.Instrument[0: len(prod['_id'])]:
				self.Product = prod
				break

		self.CalculateProfit()

	def get_product_zmq(self):
		"""从zmq读取合约信息"""
		context = zmq.Context()
		socket = context.socket(zmq.REQ)  # REQ模式,即REQ-RSP  CS结构
		socket.connect('tcp://58.247.171.146:5055')  # 实际netMQ数据服务器地址

		socket.send_json({"Type" :4})  # 直接发送__dict__转换的{}即可,不需要再转换成str

		# msg = socket.recv_unicode()	#服务器此处查询出现异常, 排除中->C#正常
		# 用recv接收,但是默认的socket中并没有此提示函数(可能是向下兼容的函数),不知能否转换为其他格式
		bs = socket.recv()  # 此处得到的是bytes

		# gzip解压:decompress(bytes)解压,会得到解压后的bytes,再用decode转成string
		str_json = gzip.decompress(bs).decode()  # decode转换为string
		return json.loads(str_json)

	def CalculateProfit(self):
		"""计算盈亏"""

		#盈亏曲线
		profitLong_list = []
		profitShort_list = []
		profit_list = []

		#持仓均价
		avgPositionLong = 0
		avgPositionShort = 0

		#持仓
		positionLong = 0
		positionShort = 0

		#记录
		records = []

		#单项指标
		#交易次数
		tradeTimes = 0
		tradeProfitTimes = 0
		tradeLossTimes = 0
		maxContinueTradeProfitTimes = 0		#最大连续盈利次数
		maxContinueTradeLossTimes = 0		#最大连续亏损次数

		tradeProfitTimesLong = 0
		tradeLossTimesLong = 0
		maxContinueTradeProfitTimesLong = 0		#最大连续盈利次数-多头
		maxContinueTradeLossTimesLong = 0		#最大连续亏损次数-多头

		tradeProfitTimesShort = 0
		tradeLossTimesShort = 0
		maxContinueTradeProfitTimesShort = 0		#最大连续盈利次数-空头
		maxContinueTradeLossTimesShort = 0		#最大连续亏损次数-空头

		#order当前位置
		idx_order = 0

		for i in range(0, len(self.stra.C)-1):
			profitLong_list.append((self.stra.C[i] - avgPositionLong) * positionLong)
			profitShort_list.append((avgPositionShort - self.stra.C[i]) * positionShort)
			profit_list.append(profitLong_list + profitShort_list)


			#当前bar有order
			if idx_order < len(self.stra.Orders):
				order = self.stra.Orders[idx_order]
				if order.DateTime == self.stra.D[i]:
					idx_order += 1
					if order.Offset == Offset.Open:
						if order.Direction == Direction.Buy:
							avgPositionLong = order.Price if positionLong == 0 else (avgPositionLong * positionLong + order.Price * order.Volume) / (positionLong + order.Volume)
							positionLong += order.Volume
						else:
							avgPositionShort = order.Price if positionShort == 0 else (avgPositionShort * positionShort + order.Price * order.Volume) / (positionShort + order.Volume)
							positionShort += order.Volume
					# 平仓
					else: #if order.Offset == Offset.Close:
						openDire = Direction.Buy if order.Direction == Direction.Sell else Direction.Sell
						# 找到对应的开仓,计算开平对
						for x in range(idx_order-1, -1, -1):#第一个-1表示结束只(不包括)
							openOrder = self.stra.Orders[x]
							if openOrder.Direction == openDire and openOrder.Offset == Offset.Open:
								profit = (1 if openDire == Direction.Buy else -1) * (order.Price - openOrder.Price) * order.Volume * self.Product['VolumeTuple']
								records.append({
									"多空": "多",
									"开仓时间": openOrder.DateTime,
									"开仓价格": openOrder.Price,
									"平仓时间": order.DateTime,
									"平仓价格": order.Price,
									"手数": order.Volume,
									"净利": profit
								})
								tradeTimes += 1
								if profit > 0:
									tradeProfitTimes += 1
									maxContinueTradeProfitTimes = max(maxContinueTradeProfitTimes, tradeProfitTimes)
									maxContinueTradeLossTimes = 0

									tradeLossTimes = 0
								else:
									maxContinueTradeProfitTimes = 0
									tradeLossTimes += 1
									maxContinueTradeLossTimes = max(maxContinueTradeLossTimes, tradeLossTimes)

								if openDire == Direction.Buy:
									if profit > 0:
										tradeLossTimesLong = 0

										tradeProfitTimesLong += 1
										maxContinueTradeProfitTimesLong = max(maxContinueTradeProfitTimesLong, tradeProfitTimesLong)
									else:
										tradeProfitTimesLong = 0

										tradeLossTimesLong += 1
										maxContinueTradeLossTimesLong = max(maxContinueTradeLossTimesLong, tradeLossTimesLong)
								else:
									if profit_list > 0:
										tradeLossTimesShort = 0
										maxContinueTradeLossTimesShort = 0

										tradeProfitTimesShort += 1
										maxContinueTradeProfitTimesShort = max(maxContinueTradeProfitTimesShort, tradeProfitTimesShort)
										maxLossShort = 0
									else:
										tradeProfitTimesShort = 0
										maxContinueTradeProfitTimesShort = 0

										tradeLossTimesShort += 1
										maxContinueTradeLossTimesShort = max(maxContinueTradeLossTimesShort, tradeLossTimesShort)
								#1开1平（多开多平待完善）
								break
		#报表
		recordsLong = [n for n in records if n["多空"] == "多"]
		recordsShort = [n for n in records if n["多空"] == "空"]

		profit_net = sum([n['净利'] for n in recordsLong])
		profit_sum = sum([n['净利'] for n in recordsLong if n['净利'] > 0])
		loss_sum = sum([n['净利'] for n in recordsLong if n['净利'] < 0])
		profit_lots = sum([n['手数'] for n in recordsLong if n['净利'] > 0])
		lots = sum([n['手数'] for n in recordsLong])
		profit_max = max([n['净利'] for n in recordsLong])
		loss_max = min([n['净利'] for n in recordsLong])
		a = 0
		b = 0
		max_down = 0
		for i in range(0, len(profitLong_list)):
			a = max(a, profitLong_list[i])
			b = min(a, profitLong_list[i])
			max_down = max(max_down, a - b)

		self.Report.append({
			"多空": "多",
			"净利": profit_net,
			"总盈利": profit_sum,
			"总亏损": loss_sum,
			"盈亏比": profit_sum/ loss_sum,
			"盈利手数": profit_lots,
			"交易手数": lots,
			"盈利比率": profit_lots / lots,
			"平均盈利": profit_sum / profit_lots,
			"平均亏损": loss_sum / (lots - profit_lots),
			"最大盈利": profit_max,
			"最大亏损": loss_max,
			"最大盈利/总盈利": profit_max / profit_sum,
			"最大亏损/总亏损": loss_max / loss_sum,
			"最大连续盈利次数": maxContinueTradeProfitTimesLong,
			"最大连续亏损次数": maxContinueTradeLossTimesLong,
			"最大回撤": max_down,
		})


	def ShowWeb(self):
		""""""
		stra = self.stra
		orders = stra.Orders
		# orders = [{"Direction": 0, "DateTime": "20161019 14:00:00", "Price": 2300},
		# # 		{"Direction":1,"DateTime":"20161019 09:00:00","Price":2400}]
		orders_json = []
		for i in range(0, len(orders)):
			# 遇到diction=Diction.Buy转换后:diction:<Diction.Buy:1> 后面报错
			# orders_str.append(ord.__dict__)
			ord = orders[i]
			orders_json.append({"DateTime": ord.DateTime.replace('-', ''), "Direction": (0 if ord.Direction == Direction.Buy else 1), "Offset": 0 if ord.Offset == Offset.Open else 1, "Price": ord.Price})

		it = 'year'
		for case in py_at.switch.switch(stra.IntervalType):
			if case(IntervalType.Minute):
				it = 'min'
				break
			if case(IntervalType.Hour):
				it = 'hour'
				break
			if case(IntervalType.Day):
				it = 'day'
				break
			if case(IntervalType.Month):
				it = 'month'
				break

		data_req = {'instrument': stra.Instrument, 'begin': stra.BeginDate, 'end': stra.EndDate, 'interval': stra.Interval, 'intervalType': it, }

		indexes_json = []
		for key, values in stra.IndexDict.items():
			array = []
			for value in values:
				array.append(value)
			indexes_json.append({'name': key, 'array': array})

		bars_json = []
		for bar in stra.Bars:
			bars_json.append({"Open":bar.O, "High":bar.H, "Low": bar.L, "Close": bar.C, "Date": bar.D})
		bars_json = json.dumps(bars_json)

		report_json = self.Report


		# data_req = json.dumps(data_req)
		# orders_json = json.dumps(orders_json)
		# indexes_json = json.dumps(indexes_json)
		# report = json.dumps(report, ensure_ascii=False)

		url_report = 'http://58.247.171.146:27017/report'
		data = json.dumps({'data_req': data_req, 'orders': orders_json, 'indexes': indexes_json, 'report': report_json})
		tmp = open('tmp.html', 'w', encoding='utf-8')
		tmp.write('''
	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta Content-Type="application/json">
		<title>galaxy data</title>
	</head>
	<body onload="init()">
		<form id="postToReport" action="{0}" method="post">
			<input type="text" id="txt_data" name="data" />
			<input type="text" id="txt_bars" name="bars" />
		</form>
		<script>
			function init(){{
				document.getElementById('txt_data').value='{1}';
				document.getElementById('txt_bars').value='{2}';
				document.getElementById('postToReport').submit();
			}}
		</script>
	</body>
	</html>'''.format(url_report, data, bars_json))  # 赋值时用',避免与json的"冲突
		tmp.close()

		os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" {0}'.format(os.path.join(sys.path[0], 'tmp.html')))

if __name__ == '__main__':
	stat = Statistics(None)
