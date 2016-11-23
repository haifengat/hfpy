#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/11/22'
"""

from app import socketio

@socketio.on_error()
def error_handler(e):
	print(e)

#this fires
@socketio.on("connect")
def connect():
	print("connected")

#this does not
@socketio.on('test')
def test_handler(message):
	print("TEST WORKS")