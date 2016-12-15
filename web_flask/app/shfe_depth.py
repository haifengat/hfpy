#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/12/15'
"""

from app import socketio
from flask_socketio import emit, join_room, leave_room, rooms, disconnect
import zmq
import struct

thread = None


################################### shfe_multi ###################################
def background_thread():
	context = zmq.Context()
	socket = context.socket(zmq.SUB)
	socket.setsockopt(zmq.LINGER, 0)

	socket.connect('tcp://192.168.105.197:5058')
	socket.subscribe('')
	#socket.setsockopt(zmq.SUBSCRIBE, 'rb1701')

	#use poll for timeouts
	poller = zmq.Poller()
	poller.register(socket, zmq.POLLIN)

	count = 0
	try:
		while True:
			#因为C#是sendrame所以会收到两次消息:instrument 和 array
			if poller.poll(3*1000): #set timeout
				msg = socket.recv()
				if len(msg) > 6:
					array = struct.unpack('@16s20d20i20d20i', msg)
					if array[0].decode('utf-8')[0:6] == 'finish':
						count += 1
						socketio.sleep(0.1)#必须的,不然会卡死
					else:
						data = {
							'instrument': array[0].decode().replace('\0',''),#去掉尾部的空
							'askprice': array[1:21],
							'askvolume': array[21:41],
							'bidprice': array[41:61],
							'bidvolume': array[61:]
						}
						if data['instrument'] not in insts:
							insts.append(data['instrument'])

						socketio.emit('rsp_data', {'data': data, 'count': count},
									namespace='/shfe_multi', room=data['instrument'])
			else:
				#print('sleep 3s')
				socketio.sleep(3)
	finally:
		poller.unregister(socket)
		poller.close()
		socket.close()

# shfe depth quote
insts = []
@socketio.on("connect", namespace='/shfe_multi')
def connect():
	global thread
	if thread is None:
		thread = socketio.start_background_task(target=background_thread)
	print("connected{0}".format(socketio.__dict__))


@socketio.on("disconnect", namespace='/shfe_multi')
def disconnect():
	print("dis_connected{0}".format(socketio.__dict__))


@socketio.on('getinsts', namespace='/shfe_multi')
def get_insts(message):
	socketio.emit('rtninsts', insts, namespace='/shfe_multi')


@socketio.on('sub_instrument', namespace='/shfe_multi')
def sub_instrument(message):
	print('{0}:join_room'.format(message))
	join_room(message)


@socketio.on('unsub_instrument', namespace='/shfe_multi')
def unsub_instrument(message):
	print('{0}:leave_room'.format(message))
	leave_room(message)




