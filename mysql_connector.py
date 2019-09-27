import os
from flaskext.mysql import MySQL
from flask import Flask


def mysql_connector():
	mysql_username = os.environ['mysql_username']
	mysql_password = os.environ['mysql_password']
	mysql_db = os.environ['mysql_db']
	mysql_ip = os.environ['mysql_ip']
	mysql_port = int(os.environ['mysql_port'])
	mysql_table = os.environ['mysql_table']

	mysql = MySQL()
	sql_query = 'SELECT * FROM %s LIMIT 1' % mysql_table

	app = Flask(__name__)