#!flask/bin/python

from flask import Flask, render_template
from flask_socketio import SocketIO #pip install flask-socketio
from app import app

app.config['SECRET_KEY'] = 'secret!'  #app.secret_key = os.urandom(10)

socketio = SocketIO(app)

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

if __name__ == "__main__":
	socketio.run(app, debug=True)
	#app.run(debug=True, port=5000)
	#socketio.run(app)
