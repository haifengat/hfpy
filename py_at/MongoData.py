#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/8/16'
"""

import py_at.MongoDBClient

#----------------------------------------------------------------------
def read_data_min(server, port, user, pwd, instrument):
	"""从mongo中读取分钟数据(含实时)"""
	
	#取数据
	client = py_at.MongoDBClient.DBConn(server, port)
	client.connect(user, pwd)
	db = client.get_database("future_min")
	coll = client.get_collection("future_min", instrument)
	docs = coll.find()
	coll_real = client.get_collection("future_real", instrument)
	docs_real = coll_real.find()
	ddoc = []
	for doc in docs:
		ddoc.append(doc)
	for doc in docs_real:
		ddoc.append(doc)
		
	return ddoc