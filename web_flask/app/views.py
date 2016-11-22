#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/11/16'
"""
import flask
from app import app
from flask import make_response, render_template, request, session, redirect, url_for, escape, jsonify
import os
from datetime import timedelta

app.secret_key = os.urandom(10) #'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

import json

@app.route('/')
@app.route('/index')
def index():
	return 'welcome to at py.'

@app.route('/report', methods=['POST'])
def report():
	data = json.loads(request.form['data'])
	bars = json.loads(request.form['bars'])
	return render_template('report.html', data=data, bars=bars) #loads后会变为'

@app.route('/echarts')
def echarts():
	return render_template('echarts.html')
