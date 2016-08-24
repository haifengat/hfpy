#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/8/16'
"""

from pymongo import MongoClient

########################################################################
class DBConn:
	"""数据库连接管理"""

	#----------------------------------------------------------------------
	def __init__(self, server = "192.168.105.210", port = "27017"):
		"""Constructor"""
		self.server = server
		self.port = port

	#----------------------------------------------------------------------
	def connect(self, user, pwd):
		"""数据库连接"""
		str_conn = "mongodb://{0}:{1}/".format(self.server, self.port)
		self.client = MongoClient(str_conn)  # pymongo.Connection(self.server)
		db_auth = self.client.admin
		db_auth.authenticate(user, pwd)

	#----------------------------------------------------------------------
	def close(self):
		"""数据库关闭"""
		self.client.close()

	#----------------------------------------------------------------------
	def get_client(self):
		"""取连接"""
		return self.client

	#----------------------------------------------------------------------
	def get_database(self, db_name):
		"""取数据库"""
		return self.client.get_database(db_name)

	#----------------------------------------------------------------------
	def get_collection(self, db_name, collection_name):
		"""取数据表"""
		return self.client.get_database(db_name).get_collection(collection_name)


