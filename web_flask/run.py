#!flask/bin/python

from flask import Flask, render_template
from app import app,socketio
import logging
import logging.handlers

app.config['SECRET_KEY'] = 'secret!'  #app.secret_key = os.urandom(10)

#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

LOG_FILE = 'at_py.log'

handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # 实例化handler
fmt = '%(asctime)s | %(filename)-12s:%(lineno)-5s | %(levelname)-8s | %(message)s'
datefmt='%Y-%m-%d %H:%M:%S'

formatter = logging.Formatter(fmt, datefmt)   # 实例化formatter
handler.setFormatter(formatter)      # 为handler添加formatter

logger = logging.getLogger('at_py')    # 获取名为tst的logger
logger.addHandler(handler)           # 为logger添加handler
logger.setLevel(logging.DEBUG)


if __name__ == "__main__":
	#socketio.run(app, debug=False, host='0.0.0.0')
	socketio.run(app, debug=False, host='0.0.0.0', port=5000)
	#app.run(debug=True, port=5000)
	#socketio.run(app)
