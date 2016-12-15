#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/12/15'
"""

from app import socketio
from flask_socketio import emit, join_room, leave_room, rooms, disconnect

#report events

import sys
import os
from py_at.py_at_adapter_test import *

adapter = None
stra_json_array = []

@socketio.on('get_strategies', namespace='/strategy')
def get_strategies():
	'''get all strategies instanse and return json'''
	#if adapter == None:

	adapter = AdapterTest()
	adapter.load_strategy()

	stra_json_array.clear()
	for stra in adapter.stra_instances:
		stra_json_array.append({
			'id': stra.ID,
			'class_name': stra.__class__.__name__,
			'instrument': stra.Instrument,
			'interval': stra.Interval,
			'interval_type': stra.IntervalType,

			'params': stra.Params,
		})

	socketio.emit('rsp_strategies', strategies=stra_json_array)

@socketio.on('run_stra', namespace='/strategy')
def run_stra(stra_json):
	'''run strategy'''
	id = stra_json['id']
	params = stra_json['params']

	socketio.emit('rsp_run_stra', 'starting...')

	stra = [s for s in a.stra_instances if s.ID == id]
	stra = stra[0]
	stra = stra.__class__()

	# 重新设置参数
	for p in params:
		print(stra.Params[p])
		stra.Params[p] = params[p]
		print(stra.Params[p])

	a.read_data_test(stra)
	socketio.emit('rsp_run_stra', 'succeed.')

@socketio.on('get_stra_report', namespace='/strategy')
def get_stra_report(stra_json):
	'''get report'''
	id = stra_json['id']

	stra = [s for s in a.stra_instances if s.ID == id]
	stra = stra[0]

	report, bar_json = Statistics(stra).GetDataAndBars()
	socketio.emit('rsp_report', report = {'bars':bar_json,'report':report})
