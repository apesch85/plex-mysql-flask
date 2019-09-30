#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
from flaskext.mysql import MySQL
from flask import Flask

mysql_username = os.environ['mysql_username']
mysql_password = os.environ['mysql_password']
mysql_db = os.environ['mysql_db']
mysql_ip = os.environ['mysql_ip']
mysql_port = int(os.environ['mysql_port'])
mysql_table = os.environ['mysql_table']


def build_app():
	
	app = Flask(__name__)

	app.config['MYSQL_DATABASE_USER'] = mysql_username
	app.config['MYSQL_DATABASE_PASSWORD'] = mysql_password
	app.config['MYSQL_DATABASE_DB'] = mysql_db
	app.config['MYSQL_DATABASE_HOST'] = mysql_ip
	app.config['MYSQL_DATABASE_PORT'] = mysql_port

	return app


def mysql_connect(app):
	
	mysql = MySQL()
	sql_query = 'SELECT * FROM %s ORDER BY RAND() LIMIT 517' % mysql_table
	 
	# MySQL configurations
	mysql.init_app(app)

	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute(sql_query)
	
	data = cursor.fetchall()
	results = [list(row) for row in data]
	for row in results:
		for index, value in enumerate(row):
			if index == 1 or index == 5:
				actual_date = value
				row[index] = actual_date
			else:
				value = value

	return results
