from flask import Flask
from flask_socketio import SocketIO #pip install flask-socketio


app = Flask(__name__, static_url_path='')   #创建 flask application 对象
socketio = SocketIO(app, async_mode=None)#'eventlet')

from app import router   #引入视图,还没实现
from app import socket_io
