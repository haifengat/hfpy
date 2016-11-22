from flask import Flask

app = Flask(__name__)   #创建 flask application 对象
from app import views   #引入视图,还没实现

