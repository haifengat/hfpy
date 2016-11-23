from flask import Flask
from flask_socketio import SocketIO #pip install flask-socketio

app = Flask(__name__)   #创建 flask application 对象
socketio = SocketIO(app)

from app import router   #引入视图,还没实现
from app import socket_io
