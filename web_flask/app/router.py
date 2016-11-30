#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/11/16'
"""
import flask
from app import app, socketio
from flask import make_response, render_template, request, session, redirect, url_for, escape, jsonify, send_from_directory
import os
from datetime import timedelta

app.secret_key = os.urandom(10) #'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

import json

@app.route('/static/<path:path>')
def send_js(path):
	return send_from_directory('static', path)

@app.route('/')
@app.route('/index')
def index():
	#return app.send_static_file('index.html')
	return 'welcome to at py.'

@app.route('/report', methods=['POST'])
def report():
	data = json.loads(request.form['data'])
	bars = json.loads(request.form['bars'])
	return render_template('report.html', data=data, bars=bars) #loads后会变为'

@app.route('/echarts')
def echarts():
	return render_template('echarts.html')

import sys
sys.path.append(os.path.join(sys.path[0], '..'))	 #调用父目录下的模块
from py_at.py_at_adapter_test import *

a = AdapterTest()
a.load_strategy()
stra_json_array = []

@app.route('/moniter')
def moniter():
	stra_json_array.clear()
	for stra in a.stra_instances:
		stra_json_array.append({
			'id': stra.ID,
			'name': '{0} {1} {2}'.format(stra.Instrument, stra.Interval, stra.IntervalType),
			'params': stra.Params,
		})
	return render_template('moniter.html', stras=stra_json_array)

@app.route('/test_stra', methods=['POST', 'GET'])
def test_stra():
	rsp = request.values.to_dict()
	#print(rsp['params'])#返回 ImmutableMultiDict;转成dict后可取到数据

	stra_json = rsp['strategies']
	params = json.loads(rsp['params']) #str->json

	#根据返回的标识取对应的策略
	stra = [s for s in a.stra_instances if s.ID == stra_json]
	stra = stra[0]

	#重新构建实例
	# module = __import__(stra.__module__)  # import module
	# c = getattr(getattr(module, stra.__class__.__name__), stra.__class__.__name__)  # 双层调用才是class,单层是为module
	# stra = c()
	stra = stra.__class__()

	#重新设置参数
	for p in params:
		print(stra.Params[p])
		stra.Params[p] = params[p]
		print(stra.Params[p])

	a.read_data_test(stra)
	data, bar_json = Statistics(stra).GetDataAndBars()
	return render_template('report.html', data=data, bars=bar_json)
