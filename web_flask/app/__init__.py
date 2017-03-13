from flask import Flask
from flask_socketio import SocketIO #pip install flask-socketio


app = Flask(__name__, static_url_path='')   #创建 flask application 对象
#threading eventlet  gevent 后两者不能实现连续推送
socketio = SocketIO(app, async_mode='threading', engineio_logger=False) #eventlet存在多次连接不断开的现象

@socketio.on_error()
def error_handler(e):
	print("error:" + e)

#以下为需要加载的模块
from app import router

#socket.io通用处理
from app import shfe_depth

#ctp封装
from app import ctp_socketio