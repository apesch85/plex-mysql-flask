
from flask import render_template
import mysql_connector

app = mysql_connector.build_app()

@app.route("/")
def main():
	data = mysql_connector.mysql_connect(app)
	return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run()