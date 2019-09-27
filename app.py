import os
from flask import Flask, render_template
from flaskext.mysql import MySQL

mysql_username = os.environ['mysql_username']
mysql_password = os.environ['mysql_password']
mysql_db = os.environ['mysql_db']
mysql_ip = os.environ['mysql_ip']
mysql_port = int(os.environ['mysql_port'])
mysql_table = os.environ['mysql_table']

app = Flask(__name__)
mysql = MySQL()
sql_query = 'SELECT * FROM %s LIMIT 1' % mysql_table
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = mysql_username
app.config['MYSQL_DATABASE_PASSWORD'] = mysql_password
app.config['MYSQL_DATABASE_DB'] = mysql_db
app.config['MYSQL_DATABASE_HOST'] = mysql_ip
app.config['MYSQL_DATABASE_PORT'] = mysql_port
mysql.init_app(app)

conn = mysql.connect()

@app.route("/")
def main():
	cursor = conn.cursor()
	cursor.execute(sql_query)
	data = cursor.fetchone()
	print len(data)

	return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run()