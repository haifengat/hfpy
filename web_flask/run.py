#!flask/bin/python

from flask import Flask, render_template
from app import app,socketio

app.config['SECRET_KEY'] = 'secret!'  #app.secret_key = os.urandom(10)


if __name__ == "__main__":
	socketio.run(app, debug=False, host='0.0.0.0')
	#app.run(debug=True, port=5000)
	#socketio.run(app)
